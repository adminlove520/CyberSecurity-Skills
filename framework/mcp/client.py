"""
MCP Client for multi-CyberSecurity
Unified interface for MCP tool calls
"""

import json
import requests
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from enum import Enum

class MCPToolCategory(Enum):
    RECON = "recon"
    SCAN = "scan"
    EXPLOIT = "exploit"
    REPORT = "report"
    UTILS = "utils"

@dataclass
class MCPTool:
    name: str
    description: str
    category: MCPToolCategory
    server: str
    parameters: Dict[str, Any]
    required_auth: List[str]

class MCPClient:
    """Client for interacting with MCP servers"""
    
    def __init__(self, registry_path: str = "framework/mcp/registry.json"):
        self.registry_path = registry_path
        self.servers: Dict[str, Dict] = {}
        self.tools: Dict[str, MCPTool] = {}
        self._load_registry()
    
    def _load_registry(self):
        """Load MCP server registry"""
        try:
            with open(self.registry_path, 'r', encoding='utf-8') as f:
                registry = json.load(f)
                self.servers = registry.get('servers', {})
                self._index_tools()
        except FileNotFoundError:
            self.servers = {}
    
    def _index_tools(self):
        """Index all available tools from registered servers"""
        for server_name, server_config in self.servers.items():
            for tool in server_config.get('tools', []):
                tool_name = tool['name']
                self.tools[tool_name] = MCPTool(
                    name=tool_name,
                    description=tool.get('description', ''),
                    category=MCPToolCategory(tool.get('category', 'utils')),
                    server=server_name,
                    parameters=tool.get('parameters', {}),
                    required_auth=tool.get('required_auth', [])
                )
    
    def list_servers(self) -> List[str]:
        """List all registered MCP servers"""
        return list(self.servers.keys())
    
    def list_tools(self, category: Optional[MCPToolCategory] = None) -> List[MCPTool]:
        """List all available tools, optionally filtered by category"""
        tools = list(self.tools.values())
        if category:
            tools = [t for t in tools if t.category == category]
        return tools
    
    def call(self, tool_name: str, params: Dict[str, Any], auth: Optional[Dict] = None) -> Dict:
        """Call an MCP tool"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found in registry")
        
        tool = self.tools[tool_name]
        server = self.servers.get(tool.server)
        
        if not server:
            raise ValueError(f"Server '{tool.server}' not found")
        
        # Check authentication
        for auth_key in tool.required_auth:
            if not auth or auth_key not in auth:
                raise PermissionError(f"Missing required auth: {auth_key}")
        
        # Build request
        url = f"{server['url']}/tools/{tool_name}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {server.get('token', '')}"
        }
        
        # Add auth params
        request_body = {
            "params": params,
            "auth": auth or {}
        }
        
        # Make request
        try:
            response = requests.post(url, json=request_body, headers=headers, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e),
                "tool": tool_name
            }
    
    def call_sync(self, tool_name: str, params: Dict[str, Any], auth: Optional[Dict] = None) -> Dict:
        """Synchronous wrapper for call"""
        return self.call(tool_name, params, auth)
    
    def health_check(self, server_name: Optional[str] = None) -> Dict[str, bool]:
        """Check health of MCP servers"""
        results = {}
        servers_to_check = [server_name] if server_name else list(self.servers.keys())
        
        for name in servers_to_check:
            if name not in self.servers:
                results[name] = False
                continue
            
            server = self.servers[name]
            try:
                response = requests.get(
                    f"{server['url']}/health",
                    headers={"Authorization": f"Bearer {server.get('token', '')}"},
                    timeout=5
                )
                results[name] = response.status_code == 200
            except:
                results[name] = False
        
        return results

# Convenience functions for common operations
def recon_scan_target(target: str, scan_type: str = "full") -> Dict:
    """Reconnaissance scan on target"""
    client = MCPClient()
    return client.call("recon_scan", {
        "target": target,
        "scan_type": scan_type
    })

def burp_get_issues(scan_id: Optional[str] = None) -> Dict:
    """Get Burp Suite scan issues"""
    client = MCPClient()
    return client.call("burp_get_issues", {
        "scan_id": scan_id
    }, auth={"burp_api_key": "${BURP_API_KEY}"})

def kali_exec_command(command: str, timeout: int = 300) -> Dict:
    """Execute command on Kali Linux"""
    client = MCPClient()
    return client.call("kali_exec", {
        "command": command,
        "timeout": timeout
    }, auth={"kali_ssh_key": "${KALI_SSH_KEY}"})

def wxmini_analyze(package_path: str, deep_analysis: bool = False) -> Dict:
    """Analyze WeChat Mini Program package"""
    client = MCPClient()
    return client.call("wxmini_analyze", {
        "package_path": package_path,
        "deep_analysis": deep_analysis
    })

def java_audit_project(project_path: str, audit_type: str = "full") -> Dict:
    """Audit Java project"""
    client = MCPClient()
    return client.call("java_audit", {
        "project_path": project_path,
        "audit_type": audit_type
    })
