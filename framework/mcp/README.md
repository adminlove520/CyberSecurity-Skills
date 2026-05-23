# 🔌 MCP 工具集成指南 (Burp Suite & Kali Linux)

为了让 Agent 能够直接控制专业安全工具，我们采用 MCP (Model Context Protocol) 模式进行集成。

## 1. Burp Suite 集成
**集成方式**：通过 `BurpRestApi` 扩展。
- **端口**: 默认 `8090`
- **能力**: 
  - `GET /burp/scanner/issues`: 获取扫描到的漏洞。
  - `POST /burp/proxy/intercept/enable`: 开启/关闭拦截。
  - `GET /burp/proxy/history`: 获取代理历史。

## 2. Kali Linux 集成 (WSL / SSH)
**集成方式**：SSH 隧道 或 WSL 本地执行。
- **SSH 配置**: 在 `framework/mcp/config.json` 中定义。
- **能力**:
  - `exec_kali_cmd`: 在远程/本地 Kali 环境中执行 msfconsole, gobuster 等命令。
  - `fetch_file_from_kali`: 从 Kali 下载结果报告。

## 3. 工具连接器 (Tool Connector)
Agent 可通过以下统一接口调用：
```python
# 伪代码示例
mcp.call("kali", "exec", {"cmd": "nmap -A target.com"})
mcp.call("burp", "get_issues")
```
