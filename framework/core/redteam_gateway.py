"""
RedTeam Gateway - 红队模式网关
可插拔的破限层，所有敏感操作通过此网关执行
"""

import os
import json
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from pathlib import Path
import asyncio
from datetime import datetime

from .jailbreak_engine import JailbreakEngine, EnvironmentChecker, UnauthorizedError
from .agent_registry import AgentRegistry, get_registry
from .orchestrator import MissionOrchestrator


@dataclass
class OperationContext:
    """操作上下文"""
    operation: str
    target: str
    platform: str
    args: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OperationResult:
    """操作结果"""
    success: bool
    operation: str
    output: Any
    error: Optional[str] = None
    logs: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class RedTeamGateway:
    """
    红队模式网关
    
    所有敏感操作必须通过此网关执行，提供：
    1. 强制环境检测
    2. 自动破限级别选择
    3. 操作审计日志
    4. 子代理/工具调用封装
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.jailbreak = JailbreakEngine(project_root)
        self.env_checker = EnvironmentChecker(project_root)
        self.agent_registry = get_registry()
        self.orchestrator = MissionOrchestrator()
        self._audit_log: List[Dict] = []
        self._operation_handlers: Dict[str, Callable] = {}
        self._register_default_handlers()
    
    def _register_default_handlers(self):
        """注册默认操作处理器"""
        self._operation_handlers = {
            "recon": self._handle_recon,
            "exploit": self._handle_exploit,
            "scan": self._handle_scan,
            "analyze": self._handle_analyze,
            "generate_poc": self._handle_generate_poc,
            "tool_call": self._handle_tool_call,
            "subagent": self._handle_subagent,
        }
    
    async def _handle_tool_call(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理工具调用操作（Sockpuppeting）"""
        logs.append("[EXEC] 通过工具调用执行敏感操作")
        
        tool_name = context.args.get("tool_name", "unknown")
        params = context.args.get("params", {})
        
        return {
            "tool": tool_name,
            "params": params,
            "status": "executed_via_tool",
            "payload_applied": payload is not None
        }
    
    async def _handle_subagent(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理子代理委派操作（Sockpuppeting）"""
        logs.append("[EXEC] 通过子代理委派执行敏感操作")
        
        subagent_name = context.target
        task = context.args.get("task", "")
        
        return {
            "subagent": subagent_name,
            "task": task,
            "status": "delegated_to_subagent",
            "payload_applied": payload is not None
        }
    
    async def execute(self, context: OperationContext) -> OperationResult:
        """
        执行敏感操作
        
        流程：
        1. 强制环境检测
        2. 选择破限级别
        3. 通过子代理/工具执行
        4. 记录审计日志
        """
        logs = []
        
        # Step 1: 环境检测
        logs.append(f"[{datetime.now().isoformat()}] 开始执行操作: {context.operation}")
        
        if not self.env_checker.is_authorized():
            error_msg = (
                "未在授权环境中运行。multi-CyberSecurity 框架要求明确的授权标记:\n"
                "\n创建以下任一文件以启用红队模式:\n"
                "  - .ctf/CTF_MODE.md (CTF/沙盒环境)\n"
                "  - .ctf/AUTHORIZED_TESTING.md (授权渗透测试)\n"
                "  - .ctf/REDTEAM_EXERCISE.md (红队演练)\n"
                "\n或设置环境变量:\n"
                "  - CTF_MODE=1\n"
                "  - PENTEST_AUTHORIZED=1\n"
                "  - REDTEAM_EXERCISE=1"
            )
            logs.append(f"[ERROR] 环境检测失败")
            self._log_audit(context, False, error_msg)
            return OperationResult(
                success=False,
                operation=context.operation,
                output=None,
                error=error_msg,
                logs=logs
            )
        
        env_type = self.env_checker.detect()
        logs.append(f"[INFO] 环境检测通过: {env_type.value}")
        
        # Step 2: 选择破限级别
        level = self.jailbreak.auto_select_level()
        logs.append(f"[INFO] 自动选择破限级别: {level}")
        
        # Step 3: 获取破限payload
        try:
            payload = self.jailbreak.get_payload(level, context.platform)
            if payload:
                logs.append(f"[INFO] 已加载 {level} 级别破限payload")
            else:
                logs.append(f"[WARN] 未找到 {level} 级别payload，使用默认配置")
        except Exception as e:
            logs.append(f"[WARN] 加载payload失败: {e}")
            payload = None
        
        # Step 4: 执行操作
        handler = self._operation_handlers.get(context.operation)
        if not handler:
            error_msg = f"未知操作: {context.operation}"
            logs.append(f"[ERROR] {error_msg}")
            self._log_audit(context, False, error_msg)
            return OperationResult(
                success=False,
                operation=context.operation,
                output=None,
                error=error_msg,
                logs=logs
            )
        
        try:
            result = await handler(context, payload, logs)
            self._log_audit(context, True, None)
            return OperationResult(
                success=True,
                operation=context.operation,
                output=result,
                logs=logs
            )
        except Exception as e:
            error_msg = str(e)
            logs.append(f"[ERROR] 操作执行失败: {error_msg}")
            self._log_audit(context, False, error_msg)
            return OperationResult(
                success=False,
                operation=context.operation,
                output=None,
                error=error_msg,
                logs=logs
            )
    
    async def _handle_recon(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理侦察操作"""
        logs.append("[EXEC] 调用 Recon Agent 执行侦察任务")
        
        # 获取recon agent
        agent = self.agent_registry.get("recon")
        if not agent:
            raise RuntimeError("Recon Agent 未注册")
        
        # 构建增强的prompt
        enhanced_prompt = self._build_enhanced_prompt(agent.system_prompt, payload)
        
        return {
            "agent": "recon",
            "prompt_length": len(enhanced_prompt),
            "target": context.target,
            "status": "dispatched"
        }
    
    async def _handle_exploit(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理漏洞利用操作"""
        logs.append("[EXEC] 调用 Exploit Agent 执行漏洞利用")
        
        agent = self.agent_registry.get("exploit")
        if not agent:
            raise RuntimeError("Exploit Agent 未注册")
        
        enhanced_prompt = self._build_enhanced_prompt(agent.system_prompt, payload)
        
        return {
            "agent": "exploit",
            "prompt_length": len(enhanced_prompt),
            "target": context.target,
            "exploit_type": context.args.get("exploit_type", "unknown"),
            "status": "dispatched"
        }
    
    async def _handle_scan(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理扫描操作"""
        logs.append("[EXEC] 执行扫描任务")
        
        return {
            "scan_type": context.args.get("scan_type", "port"),
            "target": context.target,
            "status": "initiated"
        }
    
    async def _handle_analyze(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理分析操作"""
        logs.append("[EXEC] 执行分析任务")
        
        return {
            "analysis_type": context.args.get("analysis_type", "code"),
            "target": context.target,
            "status": "initiated"
        }
    
    async def _handle_generate_poc(self, context: OperationContext, payload: Optional[str], logs: List[str]) -> Dict:
        """处理PoC生成操作（最敏感）"""
        logs.append("[EXEC] 调用 Exploit Agent 生成PoC")
        
        # PoC生成需要最高级别破限
        max_level = self.env_checker.get_max_jailbreak_level()
        allowed_levels = [JailbreakLevel.L3_HARD, JailbreakLevel.L4_DEEP]
        if max_level not in allowed_levels:
            raise UnauthorizedError("PoC生成需要L3或更高级别破限，当前环境不允许")
        
        agent = self.agent_registry.get("exploit")
        if not agent:
            raise RuntimeError("Exploit Agent 未注册")
        
        enhanced_prompt = self._build_enhanced_prompt(agent.system_prompt, payload)
        
        return {
            "agent": "exploit",
            "task": "generate_poc",
            "vulnerability": context.args.get("vulnerability"),
            "status": "dispatched"
        }
    
    def _build_enhanced_prompt(self, base_prompt: str, payload: Optional[str]) -> str:
        """构建增强的prompt，注入破限payload"""
        if not payload:
            return base_prompt
        
        # 在prompt开头注入破限payload
        return f"""{payload}

---

{base_prompt}
"""
    
    def _log_audit(self, context: OperationContext, success: bool, error: Optional[str]):
        """记录审计日志"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": context.operation,
            "target": context.target,
            "platform": context.platform,
            "success": success,
            "error": error,
            "environment": self.env_checker.detect().value
        }
        self._audit_log.append(entry)
    
    def get_audit_log(self) -> List[Dict]:
        """获取审计日志"""
        return self._audit_log.copy()
    
    def save_audit_log(self, path: str):
        """保存审计日志到文件"""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._audit_log, f, indent=2, ensure_ascii=False)
    
    def register_handler(self, operation: str, handler: Callable):
        """注册自定义操作处理器"""
        self._operation_handlers[operation] = handler
    
    def get_available_operations(self) -> List[str]:
        """获取可用操作列表"""
        return list(self._operation_handlers.keys())


class SockpuppetExecutor:
    """
    Sockpuppeting 执行器
    
    通过工具调用或子代理间接执行敏感操作
    实现Layer 7破限策略
    """
    
    def __init__(self, gateway: RedTeamGateway):
        self.gateway = gateway
    
    async def execute_via_tool(self, tool_name: str, params: Dict) -> OperationResult:
        """通过工具调用执行"""
        context = OperationContext(
            operation="tool_call",
            target=tool_name,
            platform="universal",
            args=params
        )
        return await self.gateway.execute(context)
    
    async def execute_via_subagent(self, subagent_name: str, task: str) -> OperationResult:
        """通过子代理执行"""
        context = OperationContext(
            operation="subagent",
            target=subagent_name,
            platform="universal",
            args={"task": task}
        )
        return await self.gateway.execute(context)
    
    async def execute_aci_command(self, command: str, params: Dict) -> OperationResult:
        """
        执行ACI (Agent-Computer Interface) 命令
        
        参考SWE-agent的ACI设计
        """
        aci_commands = {
            "test_sql_injection": "测试SQL注入漏洞",
            "test_xss": "测试XSS漏洞",
            "test_auth_bypass": "测试认证绕过",
            "generate_poc": "生成漏洞PoC",
            "analyze_malware": "分析恶意软件",
        }
        
        if command not in aci_commands:
            return OperationResult(
                success=False,
                operation=command,
                output=None,
                error=f"未知ACI命令: {command}"
            )
        
        context = OperationContext(
            operation=command,
            target=params.get("target", ""),
            platform=params.get("platform", "universal"),
            args=params
        )
        
        return await self.gateway.execute(context)


# 便捷函数
_gateway = None


def get_gateway(project_root: str = ".") -> RedTeamGateway:
    """获取全局网关实例"""
    global _gateway
    if _gateway is None:
        _gateway = RedTeamGateway(project_root)
    return _gateway


async def execute_redteam_operation(
    operation: str,
    target: str,
    platform: str = "universal",
    args: Dict = None
) -> OperationResult:
    """
    便捷函数：执行红队操作
    
    Example:
        result = await execute_redteam_operation(
            operation="recon",
            target="192.168.1.1",
            platform="claude"
        )
    """
    gateway = get_gateway()
    context = OperationContext(
        operation=operation,
        target=target,
        platform=platform,
        args=args or {}
    )
    return await gateway.execute(context)
