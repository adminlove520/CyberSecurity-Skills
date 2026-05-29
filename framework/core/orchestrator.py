"""
Mission Orchestrator for multi-CyberSecurity
Coordinates multi-agent security operations
"""

import os
import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

class MissionOrchestrator:
    """Orchestrates security missions with multi-agent coordination"""
    
    def __init__(self, mission_file="framework/MISSION_CONTROL.md"):
        self.mission_file = mission_file
        self.mission_data = {
            "project_name": "",
            "target": "",
            "start_time": "",
            "current_stage": "",
            "tasks": [],
            "findings": [],
            "agents": []
        }
        self._ensure_framework_dir()
    
    def _ensure_framework_dir(self):
        """Ensure framework directory exists"""
        framework_dir = os.path.dirname(self.mission_file)
        if framework_dir and not os.path.exists(framework_dir):
            os.makedirs(framework_dir, exist_ok=True)
    
    def initialize_mission(self, project_name: str, target: str, mission_type: str = "web") -> str:
        """
        Initialize a new security mission
        
        Args:
            project_name: Name of the project/mission
            target: Target URL/IP to assess
            mission_type: Type of mission (web, mobile, code-audit, etc.)
        
        Returns:
            Mission ID string
        """
        mission_id = f"mission_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        self.mission_data = {
            "mission_id": mission_id,
            "project_name": project_name,
            "target": target,
            "mission_type": mission_type,
            "start_time": datetime.now().isoformat(),
            "current_stage": "Recon",
            "status": "active",
            "tasks": [],
            "findings": [],
            "agents": [],
            "budget": {
                "allocated": 0.0,
                "spent": 0.0
            }
        }
        
        content = f"""# 🕹️ 任务控制台 (Mission Control)

## 基本信息
| 字段 | 值 |
|------|-----|
| **任务ID** | {mission_id} |
| **项目名称** | {project_name} |
| **目标** | {target} |
| **任务类型** | {mission_type} |
| **启动时间** | {datetime.now().strftime('%Y-%m-%d %H:%M')} |
| **当前阶段** | Recon |
| **状态** | 🟢 Active |

## 预算控制
| 分配预算 | 已花费 | 剩余 |
|----------|--------|------|
| $0.00 | $0.00 | $0.00 |

## 任务看板 (Kanban)
| ID | 任务描述 | 负责人 | 状态 | 交付物 | 成本 |
|:---|:---------|:-------|:-----|:-------|:-----|
| T01 | 资产发现与指纹识别 | Recon | ⏳ Pending | recon_results.json | - |

## 发现汇总
| 严重程度 | 数量 |
|:---------|:-----|
| 🔴 Critical | 0 |
| 🟠 High | 0 |
| 🟡 Medium | 0 |
| 🟢 Low | 0 |
| ⚪ Info | 0 |

## 活动日志
- [{datetime.now().strftime('%H:%M')}] Mission initialized: {mission_id}
"""
        
        with open(self.mission_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        return mission_id
    
    def add_task(self, task_id: str, description: str, agent: str, 
                 status: str = "Pending", deliverable: str = "", 
                 estimated_cost: float = 0.0) -> Dict:
        """Add a new task to the mission"""
        task = {
            "id": task_id,
            "description": description,
            "agent": agent,
            "status": status,
            "deliverable": deliverable,
            "estimated_cost": estimated_cost,
            "actual_cost": 0.0,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        
        self.mission_data["tasks"].append(task)
        self._update_mission_file()
        
        return task
    
    def update_task_status(self, task_id: str, status: str, 
                          deliverable: str = None, actual_cost: float = None):
        """Update task status and optionally deliverable/cost"""
        for task in self.mission_data["tasks"]:
            if task["id"] == task_id:
                task["status"] = status
                if deliverable:
                    task["deliverable"] = deliverable
                if actual_cost is not None:
                    task["actual_cost"] = actual_cost
                    self.mission_data["budget"]["spent"] += actual_cost
                if status in ["Completed", "Done", "✅ Done"]:
                    task["completed_at"] = datetime.now().isoformat()
                break
        
        self._update_mission_file()
        self._append_log(f"Task {task_id} updated to {status}")
    
    def add_finding(self, finding_id: str, title: str, severity: str,
                   description: str, evidence: Dict[str, Any]) -> Dict:
        """Add a security finding"""
        finding = {
            "id": finding_id,
            "title": title,
            "severity": severity,
            "description": description,
            "evidence": evidence,
            "status": "Open",
            "created_at": datetime.now().isoformat(),
            "validated": False,
            "reachable": False
        }
        
        self.mission_data["findings"].append(finding)
        self._update_mission_file()
        
        severity_emoji = {
            "critical": "🔴",
            "high": "🟠",
            "medium": "🟡",
            "low": "🟢",
            "info": "⚪"
        }.get(severity.lower(), "⚪")
        
        self._append_log(f"New finding added: {title} ({severity_emoji} {severity})")
        
        return finding
    
    def update_finding_status(self, finding_id: str, validated: bool = None, 
                             reachable: bool = None, status: str = None):
        """Update finding validation/reachability status"""
        for finding in self.mission_data["findings"]:
            if finding["id"] == finding_id:
                if validated is not None:
                    finding["validated"] = validated
                if reachable is not None:
                    finding["reachable"] = reachable
                if status:
                    finding["status"] = status
                break
        
        self._update_mission_file()
    
    def set_budget(self, allocated: float):
        """Set mission budget"""
        self.mission_data["budget"]["allocated"] = allocated
        self._update_mission_file()
        self._append_log(f"Budget allocated: ${allocated:.2f}")
    
    def add_cost(self, cost: float):
        """Add to spent budget"""
        self.mission_data["budget"]["spent"] += cost
        self._update_mission_file()
    
    def check_budget(self, estimated_cost: float = 0.0) -> bool:
        """Check if remaining budget is sufficient"""
        allocated = self.mission_data["budget"]["allocated"]
        spent = self.mission_data["budget"]["spent"]
        remaining = allocated - spent
        return remaining >= estimated_cost
    
    def set_stage(self, stage: str):
        """Update current mission stage"""
        old_stage = self.mission_data["current_stage"]
        self.mission_data["current_stage"] = stage
        self._update_mission_file()
        self._append_log(f"Stage transition: {old_stage} → {stage}")
    
    def complete_mission(self, summary: str = ""):
        """Mark mission as completed"""
        self.mission_data["status"] = "completed"
        self.mission_data["end_time"] = datetime.now().isoformat()
        self._update_mission_file()
        self._append_log(f"Mission completed. {summary}")
    
    def log_advisor_recommendation(self, recommendation: str):
        """Log advisor recommendation"""
        self._append_log(f"💡 Advisor: {recommendation}")
    
    def trigger_reflexion(self, task_id: str, failure_reason: str):
        """Trigger reflexion for failed task"""
        self._append_log(f"🔄 Reflexion triggered for {task_id}: {failure_reason}")
        self.log_advisor_recommendation(f"Analysis of {task_id} failure: {failure_reason}")
    
    def _update_mission_file(self):
        """Update the mission control markdown file"""
        # Calculate statistics
        findings_by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        for finding in self.mission_data["findings"]:
            sev = finding["severity"].lower()
            if sev in findings_by_severity:
                findings_by_severity[sev] += 1
        
        # Build task table
        task_rows = []
        for task in self.mission_data["tasks"]:
            status_emoji = {
                "pending": "⏳", "in_progress": "🔄", "completed": "✅",
                "done": "✅", "failed": "❌", "blocked": "🚫"
            }.get(task["status"].lower(), "⏳")
            
            cost_str = f"${task['actual_cost']:.2f}" if task['actual_cost'] > 0 else "-"
            task_rows.append(
                f"| {task['id']} | {task['description']} | {task['agent']} | "
                f"{status_emoji} {task['status']} | {task['deliverable']} | {cost_str} |"
            )
        
        tasks_table = "\n".join(task_rows) if task_rows else "| - | No tasks yet | - | - | - | - |"
        
        # Budget
        allocated = self.mission_data["budget"]["allocated"]
        spent = self.mission_data["budget"]["spent"]
        remaining = allocated - spent
        
        status_emoji = "🟢" if self.mission_data["status"] == "active" else "✅"
        
        content = f"""# 🕹️ 任务控制台 (Mission Control)

## 基本信息
| 字段 | 值 |
|------|-----|
| **任务ID** | {self.mission_data.get('mission_id', 'N/A')} |
| **项目名称** | {self.mission_data.get('project_name', 'N/A')} |
| **目标** | {self.mission_data.get('target', 'N/A')} |
| **任务类型** | {self.mission_data.get('mission_type', 'N/A')} |
| **启动时间** | {self.mission_data.get('start_time', 'N/A')} |
| **当前阶段** | {self.mission_data.get('current_stage', 'N/A')} |
| **状态** | {status_emoji} {self.mission_data.get('status', 'unknown').upper()} |

## 预算控制
| 分配预算 | 已花费 | 剩余 |
|----------|--------|------|
| ${allocated:.2f} | ${spent:.2f} | ${remaining:.2f} |

## 任务看板 (Kanban)
| ID | 任务描述 | 负责人 | 状态 | 交付物 | 成本 |
|:---|:---------|:-------|:-----|:-------|:-----|
{tasks_table}

## 发现汇总
| 严重程度 | 数量 |
|:---------|:-----|
| 🔴 Critical | {findings_by_severity['critical']} |
| 🟠 High | {findings_by_severity['high']} |
| 🟡 Medium | {findings_by_severity['medium']} |
| 🟢 Low | {findings_by_severity['low']} |
| ⚪ Info | {findings_by_severity['info']} |
| **总计** | **{sum(findings_by_severity.values())}** |

## 发现详情
"""
        
        # Add findings
        if self.mission_data["findings"]:
            for finding in self.mission_data["findings"]:
                sev_emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", 
                           "low": "🟢", "info": "⚪"}.get(finding['severity'].lower(), "⚪")
                
                validated = "✅" if finding.get('validated') else "⏳"
                reachable = "✅" if finding.get('reachable') else "⏳"
                
                content += f"""
### {finding['id']}: {finding['title']}
- **严重程度**: {sev_emoji} {finding['severity']}
- **状态**: {finding['status']}
- **验证状态**: {validated} Validated | {reachable} Reachable
- **描述**: {finding['description']}
"""
        else:
            content += "\n_No findings recorded yet._\n"
        
        # Add log section
        content += """
## 活动日志
"""
        
        with open(self.mission_file, "r", encoding="utf-8") as f:
            existing_content = f.read()
        
        # Extract existing logs
        log_pattern = r'## 活动日志\n(.*?)(?=\n## |\Z)'
        log_match = re.search(log_pattern, existing_content, re.DOTALL)
        existing_logs = log_match.group(1).strip() if log_match else ""
        
        content += existing_logs
        
        with open(self.mission_file, "w", encoding="utf-8") as f:
            f.write(content)
    
    def _append_log(self, message: str):
        """Append a log entry to the mission file"""
        timestamp = datetime.now().strftime('%H:%M')
        log_entry = f"\n- [{timestamp}] {message}"
        
        with open(self.mission_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
    
    def get_mission_summary(self) -> Dict[str, Any]:
        """Get mission summary statistics"""
        findings_by_severity = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        for finding in self.mission_data["findings"]:
            sev = finding["severity"].lower()
            if sev in findings_by_severity:
                findings_by_severity[sev] += 1
        
        tasks_by_status = {}
        for task in self.mission_data["tasks"]:
            status = task["status"]
            tasks_by_status[status] = tasks_by_status.get(status, 0) + 1
        
        return {
            "mission_id": self.mission_data.get("mission_id"),
            "project_name": self.mission_data.get("project_name"),
            "target": self.mission_data.get("target"),
            "status": self.mission_data.get("status"),
            "current_stage": self.mission_data.get("current_stage"),
            "findings": findings_by_severity,
            "total_findings": sum(findings_by_severity.values()),
            "tasks": tasks_by_status,
            "total_tasks": len(self.mission_data["tasks"]),
            "budget": self.mission_data["budget"]
        }

if __name__ == "__main__":
    # Example usage
    orchestrator = MissionOrchestrator()
    mission_id = orchestrator.initialize_mission("Test Audit", "https://example.com")
    print(f"Mission initialized: {mission_id}")
    
    orchestrator.set_budget(100.0)
    orchestrator.add_task("T01", "Reconnaissance", "Recon Agent", deliverable="assets.json")
    orchestrator.update_task_status("T01", "Completed", "assets.json", 5.0)
    orchestrator.add_finding("F01", "SQL Injection", "high", "SQLi in login form", {"url": "/login"})
    
    summary = orchestrator.get_mission_summary()
    print(f"Summary: {json.dumps(summary, indent=2)}")
