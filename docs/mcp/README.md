# 🔌 MCP 工具集成 (MCP Integration)

## 1. Burp Suite 集成细节
本框架通过 `BurpRestApi` 扩展与 Burp Suite 通讯。

### 配置步骤
1. 在 Burp Suite 中安装 `REST API` 扩展。
2. 在 `framework/mcp/config.json` 中配置 API Key。
3. 确保监听端口（默认 8090）可被 Agent 访问。

### 支持的操作
- **主动扫描**: `POST /burp/scanner/scans`
- **漏洞查询**: `GET /burp/scanner/issues`
- **代理流水审计**: `GET /burp/proxy/history`

## 2. Kali Linux (WSL/SSH) 集成
Agent 可以直接在 Kali 环境中执行 Linux 指令。

### 配置方式
- **WSL (推荐)**: 确保 Windows 宿主机安装了 WSL Kali。
- **SSH**: 适用于远程 Kali 虚拟机。

### 调用逻辑
```bash
# Agent 内部调用的指令格式
python framework/mcp/kali_connector.py --cmd "nmap -sV {target}"
```
