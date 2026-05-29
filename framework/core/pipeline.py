"""
8-Stage Vulnerability Discovery Pipeline
Inspired by Cloudflare's Project Glasswing and evilsocket/audit
"""

import json
import sqlite3
import time
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

class Stage(Enum):
    RECON = "recon"
    HUNT = "hunt"
    VALIDATE = "validate"
    GAPFILL = "gapfill"
    DEDUPE = "dedupe"
    TRACE = "trace"
    FEEDBACK = "feedback"
    REPORT = "report"

@dataclass
class Task:
    id: str
    stage: Stage
    description: str
    agent: str
    status: str = "pending"
    output: Optional[Dict] = None
    cost_usd: float = 0.0
    created_at: str = ""
    completed_at: Optional[str] = None
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

@dataclass
class Finding:
    id: str
    task_id: str
    title: str
    severity: str
    description: str
    evidence: Dict
    validated: bool = False
    reachable: bool = False
    dedupe_key: Optional[str] = None
    created_at: str = ""
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

class AuditPipeline:
    """8-Stage vulnerability discovery pipeline"""
    
    def __init__(self, db_path: str = "framework/state.db", max_cost_usd: float = 100.0):
        self.db_path = db_path
        self.max_cost_usd = max_cost_usd
        self.current_cost = 0.0
        self.run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self._init_db()
    
    def _init_db(self):
        """Initialize SQLite state store"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Runs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                id TEXT PRIMARY KEY,
                target TEXT,
                status TEXT,
                max_cost_usd REAL,
                actual_cost_usd REAL DEFAULT 0,
                created_at TEXT,
                completed_at TEXT
            )
        """)
        
        # Tasks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                run_id TEXT,
                stage TEXT,
                description TEXT,
                agent TEXT,
                status TEXT,
                output TEXT,
                cost_usd REAL,
                created_at TEXT,
                completed_at TEXT,
                FOREIGN KEY (run_id) REFERENCES runs(id)
            )
        """)
        
        # Findings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS findings (
                id TEXT PRIMARY KEY,
                run_id TEXT,
                task_id TEXT,
                title TEXT,
                severity TEXT,
                description TEXT,
                evidence TEXT,
                validated INTEGER DEFAULT 0,
                reachable INTEGER DEFAULT 0,
                dedupe_key TEXT,
                created_at TEXT,
                FOREIGN KEY (run_id) REFERENCES runs(id),
                FOREIGN KEY (task_id) REFERENCES tasks(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def start_run(self, target: str) -> str:
        """Start a new audit run"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO runs (id, target, status, max_cost_usd, created_at) VALUES (?, ?, ?, ?, ?)",
            (self.run_id, target, "running", self.max_cost_usd, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return self.run_id
    
    def check_budget(self, estimated_cost: float = 0.0) -> bool:
        """Check if we're still within budget"""
        return (self.current_cost + estimated_cost) <= self.max_cost_usd
    
    def add_cost(self, cost: float):
        """Add to current cost"""
        self.current_cost += cost
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE runs SET actual_cost_usd = ? WHERE id = ?",
            (self.current_cost, self.run_id)
        )
        conn.commit()
        conn.close()
    
    def create_task(self, stage: Stage, description: str, agent: str) -> Task:
        """Create a new task"""
        task_id = f"{self.run_id}_{stage.value}_{int(time.time())}"
        task = Task(
            id=task_id,
            stage=stage,
            description=description,
            agent=agent
        )
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO tasks (id, run_id, stage, description, agent, status, cost_usd, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (task.id, self.run_id, task.stage.value, task.description, 
             task.agent, task.status, task.cost_usd, task.created_at)
        )
        conn.commit()
        conn.close()
        
        return task
    
    def complete_task(self, task: Task, output: Dict, cost_usd: float = 0.0):
        """Mark task as completed"""
        task.status = "completed"
        task.output = output
        task.cost_usd = cost_usd
        task.completed_at = datetime.now().isoformat()
        
        self.add_cost(cost_usd)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tasks SET status = ?, output = ?, cost_usd = ?, completed_at = ?
               WHERE id = ?""",
            (task.status, json.dumps(output), task.cost_usd, task.completed_at, task.id)
        )
        conn.commit()
        conn.close()
    
    def add_finding(self, finding: Finding):
        """Add a finding"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO findings (id, run_id, task_id, title, severity, description, 
               evidence, validated, reachable, dedupe_key, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (finding.id, self.run_id, finding.task_id, finding.title, finding.severity,
             finding.description, json.dumps(finding.evidence), 
             int(finding.validated), int(finding.reachable), finding.dedupe_key, finding.created_at)
        )
        conn.commit()
        conn.close()
    
    def update_finding_validation(self, finding_id: str, validated: bool):
        """Update finding validation status"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE findings SET validated = ? WHERE id = ?",
            (int(validated), finding_id)
        )
        conn.commit()
        conn.close()
    
    def update_finding_reachability(self, finding_id: str, reachable: bool):
        """Update finding reachability status"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE findings SET reachable = ? WHERE id = ?",
            (int(reachable), finding_id)
        )
        conn.commit()
        conn.close()
    
    def get_findings(self, stage: Optional[Stage] = None, validated_only: bool = False) -> List[Finding]:
        """Get findings with optional filters"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT * FROM findings WHERE run_id = ?"
        params = [self.run_id]
        
        if validated_only:
            query += " AND validated = 1"
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        
        findings = []
        for row in rows:
            finding = Finding(
                id=row[0],
                task_id=row[2],
                title=row[3],
                severity=row[4],
                description=row[5],
                evidence=json.loads(row[6]),
                validated=bool(row[7]),
                reachable=bool(row[8]),
                dedupe_key=row[9],
                created_at=row[10]
            )
            findings.append(finding)
        
        return findings
    
    def deduplicate_findings(self) -> int:
        """Deduplicate findings and return count of removed duplicates"""
        findings = self.get_findings()
        
        # Group by dedupe_key
        groups: Dict[str, List[Finding]] = {}
        for f in findings:
            key = f.dedupe_key or f.title
            if key not in groups:
                groups[key] = []
            groups[key].append(f)
        
        # Mark duplicates (keep first, mark rest as duplicates)
        removed = 0
        for key, group in groups.items():
            if len(group) > 1:
                # Keep the one with highest severity or most evidence
                sorted_group = sorted(group, key=lambda x: (x.severity, len(x.evidence)), reverse=True)
                for dup in sorted_group[1:]:
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM findings WHERE id = ?", (dup.id,))
                    conn.commit()
                    conn.close()
                    removed += 1
        
        return removed
    
    def complete_run(self):
        """Complete the audit run"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE runs SET status = ?, completed_at = ? WHERE id = ?",
            ("completed", datetime.now().isoformat(), self.run_id)
        )
        conn.commit()
        conn.close()
    
    def get_report(self) -> Dict:
        """Generate final report"""
        findings = self.get_findings(validated_only=True)
        
        severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        for f in findings:
            if f.severity.lower() in severity_counts:
                severity_counts[f.severity.lower()] += 1
        
        return {
            "run_id": self.run_id,
            "total_findings": len(findings),
            "severity_breakdown": severity_counts,
            "total_cost_usd": self.current_cost,
            "findings": [asdict(f) for f in findings]
        }

# Stage-specific schemas for validation
STAGE_SCHEMAS = {
    Stage.RECON: {
        "type": "object",
        "properties": {
            "assets": {"type": "array", "items": {"type": "string"}},
            "technologies": {"type": "array", "items": {"type": "string"}},
            "scope": {"type": "object"}
        },
        "required": ["assets"]
    },
    Stage.HUNT: {
        "type": "object",
        "properties": {
            "findings": {"type": "array"},
            "attack_surface": {"type": "object"}
        },
        "required": ["findings"]
    },
    Stage.VALIDATE: {
        "type": "object",
        "properties": {
            "validated_findings": {"type": "array"},
            "false_positives": {"type": "array"}
        },
        "required": ["validated_findings"]
    },
    Stage.TRACE: {
        "type": "object",
        "properties": {
            "reachable_findings": {"type": "array"},
            "unreachable_findings": {"type": "array"}
        },
        "required": ["reachable_findings"]
    },
    Stage.REPORT: {
        "type": "object",
        "properties": {
            "executive_summary": {"type": "string"},
            "findings": {"type": "array"},
            "recommendations": {"type": "array"}
        },
        "required": ["executive_summary", "findings"]
    }
}
