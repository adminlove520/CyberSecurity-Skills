import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="CyberSecurity-Skills Unified CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: lint
    subparsers.add_parser("lint", help="Validate skill library structure")
    
    # Command: export
    subparsers.add_parser("export", help="Export manifests for AI platforms (OpenClaw, Trae, etc.)")
    
    # Command: graph
    subparsers.add_parser("graph", help="Build semantic skill knowledge graph")
    
    # Command: evolve
    subparsers.add_parser("evolve", help="Distill mission logs into new skills")

    # Command: mission-init
    init_parser = subparsers.add_parser("mission-init", help="Initialize a new mission")
    init_parser.add_argument("--name", required=True, help="Project name")
    init_parser.add_argument("--target", required=True, help="Target URL/IP")

    args = parser.parse_args()

    if args.command == "lint":
        os.system("python scripts/linter.py")
    elif args.command == "export":
        os.system("python scripts/platform_exporter.py")
    elif args.command == "graph":
        os.system("python scripts/build_graph.py")
    elif args.command == "mission-init":
        from framework.core.orchestrator import MissionOrchestrator
        orch = MissionOrchestrator()
        orch.initialize_mission(args.name, args.target)
        print(f"Mission '{args.name}' initialized in framework/MISSION_CONTROL.md")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
int(f"Mission '{args.name}' initialized in framework/MISSION_CONTROL.md")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
