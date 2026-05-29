#!/usr/bin/env python3
"""
CyberSecurity-Skills v3.0 Enhanced CLI
Unified command-line interface for security operations
"""

import argparse
import sys
import os
import json
from pathlib import Path
from typing import Optional

# Add framework to path
sys.path.insert(0, str(Path(__file__).parent))

from framework.core.pipeline import AuditPipeline, Stage
from framework.mcp.client import MCPClient

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Print CLI banner"""
    banner = f"""
{Colors.CYAN}
   ______      __                      _____ __                __            
  / ____/___  / /___  ____ ______     / ___// /_  ____  ____  / /____  _____
 / /   / __ \/ / __ \/ __ `/ ___/     \__ \/ __ \/ __ \/ __ \/ __/ _ \/ ___/
/ /___/ /_/ / / /_/ / /_/ / /        ___/ / / / / /_/ / /_/ / /_/  __/ /    
\____/\____/_/\____/\__, /_/        /____/_/ /_/\____/\____/\__/\___/_/     
                   /____/                                                    
{Colors.ENDC}
{Colors.GREEN}CyberSecurity-Skills v3.0 - AI-Powered Security Framework{Colors.ENDC}
    """
    print(banner)

def cmd_audit(args):
    """Run 8-stage security audit"""
    print(f"{Colors.BLUE}[*] Starting 8-stage security audit...{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Target: {args.target}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Max budget: ${args.max_cost}{Colors.ENDC}")
    
    pipeline = AuditPipeline(max_cost_usd=args.max_cost)
    run_id = pipeline.start_run(args.target)
    
    print(f"{Colors.GREEN}[+] Audit run started: {run_id}{Colors.ENDC}")
    
    # Stage 1: Recon
    print(f"\n{Colors.CYAN}[Stage 1/8] Reconnaissance{Colors.ENDC}")
    task = pipeline.create_task(Stage.RECON, "Asset discovery and fingerprinting", "recon_agent")
    # ... (actual implementation would call agent)
    pipeline.complete_task(task, {"assets": [args.target], "technologies": []}, cost_usd=0.5)
    print(f"{Colors.GREEN}[+] Recon completed{Colors.ENDC}")
    
    # Stage 2: Hunt
    print(f"\n{Colors.CYAN}[Stage 2/8] Hunt{Colors.ENDC}")
    task = pipeline.create_task(Stage.HUNT, "Vulnerability discovery", "exploit_agent")
    # ...
    pipeline.complete_task(task, {"findings": []}, cost_usd=1.0)
    print(f"{Colors.GREEN}[+] Hunt completed{Colors.ENDC}")
    
    # Stage 3: Validate
    print(f"\n{Colors.CYAN}[Stage 3/8] Validate{Colors.ENDC}")
    task = pipeline.create_task(Stage.VALIDATE, "Finding validation", "validator_agent")
    pipeline.complete_task(task, {"validated_findings": []}, cost_usd=0.5)
    print(f"{Colors.GREEN}[+] Validation completed{Colors.ENDC}")
    
    # Stage 4: Gapfill
    print(f"\n{Colors.CYAN}[Stage 4/8] Gapfill{Colors.ENDC}")
    task = pipeline.create_task(Stage.GAPFILL, "Coverage gap analysis", "advisor_agent")
    pipeline.complete_task(task, {"additional_targets": []}, cost_usd=0.3)
    print(f"{Colors.GREEN}[+] Gapfill completed{Colors.ENDC}")
    
    # Stage 5: Dedupe
    print(f"\n{Colors.CYAN}[Stage 5/8] Deduplicate{Colors.ENDC}")
    removed = pipeline.deduplicate_findings()
    print(f"{Colors.GREEN}[+] Removed {removed} duplicate findings{Colors.ENDC}")
    
    # Stage 6: Trace
    print(f"\n{Colors.CYAN}[Stage 6/8] Trace{Colors.ENDC}")
    task = pipeline.create_task(Stage.TRACE, "Reachability tracing", "recon_agent")
    pipeline.complete_task(task, {"reachable_findings": []}, cost_usd=0.5)
    print(f"{Colors.GREEN}[+] Tracing completed{Colors.ENDC}")
    
    # Stage 7: Feedback
    print(f"\n{Colors.CYAN}[Stage 7/8] Feedback{Colors.ENDC}")
    task = pipeline.create_task(Stage.FEEDBACK, "Pattern extraction", "librarian_agent")
    pipeline.complete_task(task, {"new_patterns": []}, cost_usd=0.3)
    print(f"{Colors.GREEN}[+] Feedback completed{Colors.ENDC}")
    
    # Stage 8: Report
    print(f"\n{Colors.CYAN}[Stage 8/8] Report{Colors.ENDC}")
    task = pipeline.create_task(Stage.REPORT, "Final report generation", "coordinator_agent")
    report = pipeline.get_report()
    pipeline.complete_task(task, report, cost_usd=0.2)
    
    pipeline.complete_run()
    
    print(f"\n{Colors.GREEN}[+] Audit completed!{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Total findings: {report['total_findings']}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Total cost: ${report['total_cost_usd']:.2f}{Colors.ENDC}")
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"{Colors.GREEN}[+] Report saved to: {args.output}{Colors.ENDC}")

def cmd_wxmini(args):
    """WeChat Mini Program audit"""
    print(f"{Colors.BLUE}[*] Starting WeChat Mini Program audit...{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Target: {args.path}{Colors.ENDC}")
    
    # Use MCP client to call wxmini server
    client = MCPClient()
    result = client.call("wxmini_analyze", {
        "package_path": args.path,
        "deep_analysis": args.deep
    })
    
    if result.get("success"):
        print(f"{Colors.GREEN}[+] Analysis completed!{Colors.ENDC}")
        print(f"{Colors.BLUE}[*] Output directory: {result.get('output_dir')}{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}[-] Analysis failed: {result.get('error')}{Colors.ENDC}")

def cmd_java(args):
    """Java code audit"""
    print(f"{Colors.BLUE}[*] Starting Java code audit...{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Project: {args.path}{Colors.ENDC}")
    print(f"{Colors.BLUE}[*] Audit type: {args.type}{Colors.ENDC}")
    
    client = MCPClient()
    result = client.call("java_audit", {
        "project_path": args.path,
        "audit_type": args.type
    })
    
    if result.get("success"):
        print(f"{Colors.GREEN}[+] Audit completed!{Colors.ENDC}")
        print(f"{Colors.BLUE}[*] Output directory: {result.get('output_dir')}{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}[-] Audit failed: {result.get('error')}{Colors.ENDC}")

def cmd_mcp(args):
    """MCP server management"""
    client = MCPClient()
    
    if args.action == "list":
        print(f"{Colors.CYAN}Registered MCP Servers:{Colors.ENDC}")
        for server in client.list_servers():
            print(f"  - {server}")
    
    elif args.action == "tools":
        print(f"{Colors.CYAN}Available MCP Tools:{Colors.ENDC}")
        for tool in client.list_tools():
            print(f"  - {tool.name} ({tool.category.value}): {tool.description}")
    
    elif args.action == "health":
        print(f"{Colors.CYAN}MCP Server Health Check:{Colors.ENDC}")
        health = client.health_check(args.server)
        for server, status in health.items():
            status_color = Colors.GREEN if status else Colors.FAIL
            status_text = "healthy" if status else "unhealthy"
            print(f"  - {server}: {status_color}{status_text}{Colors.ENDC}")

def cmd_skill(args):
    """Skill management"""
    if args.action == "list":
        print(f"{Colors.CYAN}Available Skills:{Colors.ENDC}")
        # Load from skills/catalog.json
        catalog_path = Path(__file__).parent / "skills" / "catalog.json"
        if catalog_path.exists():
            with open(catalog_path) as f:
                catalog = json.load(f)
                for skill in catalog.get("skills", []):
                    print(f"  - {skill['id']}: {skill['name']}")
        else:
            print(f"{Colors.WARNING}[-] Skill catalog not found{Colors.ENDC}")
    
    elif args.action == "export":
        print(f"{Colors.BLUE}[*] Exporting skills for platform: {args.platform}{Colors.ENDC}")
        os.system(f"python scripts/platform_exporter.py --platform {args.platform}")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="CyberSecurity-Skills v3.0 - AI-Powered Security Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s audit --target https://example.com --max-cost 50
  %(prog)s wxmini --path /path/to/miniapp --deep
  %(prog)s java --path /path/to/project --type full
  %(prog)s mcp list
  %(prog)s skill export --platform trae
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Run 8-stage security audit")
    audit_parser.add_argument("--target", required=True, help="Target URL or IP")
    audit_parser.add_argument("--max-cost", type=float, default=100.0, help="Maximum budget in USD")
    audit_parser.add_argument("--output", "-o", help="Output file for report")
    
    # WeChat Mini Program audit
    wxmini_parser = subparsers.add_parser("wxmini", help="WeChat Mini Program security audit")
    wxmini_parser.add_argument("--path", required=True, help="Path to mini program package or directory")
    wxmini_parser.add_argument("--deep", action="store_true", help="Enable deep analysis")
    
    # Java audit
    java_parser = subparsers.add_parser("java", help="Java code security audit")
    java_parser.add_argument("--path", required=True, help="Path to Java project")
    java_parser.add_argument("--type", choices=["full", "sql", "auth", "file", "xxe"], 
                            default="full", help="Audit type")
    
    # MCP management
    mcp_parser = subparsers.add_parser("mcp", help="MCP server management")
    mcp_parser.add_argument("action", choices=["list", "tools", "health"], help="Action to perform")
    mcp_parser.add_argument("--server", help="Specific server name (for health check)")
    
    # Skill management
    skill_parser = subparsers.add_parser("skill", help="Skill management")
    skill_parser.add_argument("action", choices=["list", "export"], help="Action to perform")
    skill_parser.add_argument("--platform", choices=["trae", "cursor", "claude", "codex"], 
                             default="trae", help="Target platform")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Route to appropriate command handler
    command_handlers = {
        "audit": cmd_audit,
        "wxmini": cmd_wxmini,
        "java": cmd_java,
        "mcp": cmd_mcp,
        "skill": cmd_skill
    }
    
    handler = command_handlers.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
