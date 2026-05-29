# 🔒 CyberSecurity-Skills v3.0 (Agentic Security Framework)

**从静态知识库演进为自主渗透测试框架** — 基于多智能体协作、8阶段审计流水线、MCP工具集成的网络安全大模型技能库。

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)

## 🌟 v3.0 核心新特性

### 🤖 8阶段审计流水线 (8-Stage Pipeline)
借鉴 Cloudflare Project Glasswing 和 evilsocket/audit:
- **Recon** → 资产发现与指纹识别
- **Hunt** → 漏洞扫描与PoC生成
- **Validate** → 对抗验证与误报过滤
- **Gapfill** → 覆盖缺口补充
- **Dedupe** → 去重聚类
- **Trace** → 可达性追踪
- **Feedback** → 模式提取与任务生成
- **Report** → 结构化报告输出

### 🔌 MCP服务集 (Model Context Protocol)
标准化工具集成:
- **wxmini-server**: 微信小程序动态分析
- **java-server**: Java代码审计服务
- **burp-bridge**: Burp Suite Professional集成
- **kali-bridge**: Kali Linux工具调用

### 🎯 专项审计Agent
- **微信小程序审计**: 7-Agent协作，双层架构(脚本+LLM)
- **Java全链路审计**: 5阶段Pipeline，动态Worker创建
- **Web通用审计**: 基于8阶段流水线的Web安全测试

### 💰 成本与质量管控
- **预算控制**: `--max-cost-usd` 参数限制总成本
- **质量校验**: 每个阶段后自动校验
- **可达性验证**: 确保漏洞真实可利用

## 📁 目录结构

```
CyberSecurity-Skills/
├── .trae/                    # Trae IDE配置
├── .cursor/                  # Cursor IDE配置
├── .claude/                  # Claude IDE配置
├── agents/
│   ├── core/                 # 7个核心Agent
│   └── specialized/          # 专项审计Agents
│       ├── wxmini/           # 微信小程序审计
│       └── java/             # Java代码审计
├── framework/
│   ├── core/
│   │   ├── pipeline.py       # 8阶段流水线
│   │   ├── orchestrator.py   # 任务编排器
│   │   └── reporter.py       # 报告引擎
│   ├── mcp/
│   │   ├── client.py         # MCP客户端
│   │   └── registry.json     # MCP服务注册表
│   ├── stages/               # 8阶段定义
│   └── schemas/              # JSON Schema验证
├── skills/
│   └── catalog.json          # 统一技能目录
├── cli.py                    # 增强CLI
└── skill.py                  # 兼容旧版CLI
```

## 🚀 快速开始

### 安装
```bash
git clone https://github.com/adminlove520/CyberSecurity-Skills.git
cd CyberSecurity-Skills
pip install -r requirements.txt
```

### 运行8阶段安全审计
```bash
python cli.py audit --target https://example.com --max-cost 50 --output report.json
```

### 微信小程序审计
```bash
python cli.py wxmini --path /path/to/miniapp --deep
```

### Java代码审计
```bash
python cli.py java --path /path/to/project --type full
```

### MCP服务管理
```bash
# 列出所有MCP服务
python cli.py mcp list

# 查看可用工具
python cli.py mcp tools

# 健康检查
python cli.py mcp health
```

## 📚 技能目录

### 代码审计技能
| 技能ID | 名称 | 来源 | 阶段 |
|--------|------|------|------|
| wxmini-security-audit | 微信小程序安全审计 | wxmini-security-audit | hunt, validate |
| java-route-mapper | Java路由映射 | java-audit-skills | recon |
| java-route-tracer | Java调用链追踪 | java-audit-skills | trace |
| java-sql-audit | Java SQL注入审计 | java-audit-skills | hunt, validate |
| java-auth-audit | Java认证审计 | java-audit-skills | hunt, validate |
| java-file-upload-audit | Java文件上传审计 | java-audit-skills | hunt |
| java-file-read-audit | Java文件读取审计 | java-audit-skills | hunt |
| java-xxe-audit | Java XXE审计 | java-audit-skills | hunt |
| java-vuln-scanner | Java组件漏洞扫描 | java-audit-skills | recon |
| java-audit-pipeline | Java全链路审计 | java-audit-skills | 全阶段 |

### 工具集成
| 技能ID | 名称 | MCP服务 |
|--------|------|---------|
| burp-suite-bridge | Burp Suite集成 | burp-bridge |
| kali-linux-bridge | Kali Linux集成 | kali-bridge |

## 🏗️ 架构设计

### 8阶段流水线架构
```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Recon  │───→│  Hunt   │───→│ Validate│───→│ Gapfill │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                  │
┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  Report │←───│ Feedback│←───│  Trace  │←───────┘
└─────────┘    └─────────┘    └─────────┘
     ↑
┌─────────┐
│  Dedupe │
└─────────┘
```

### 微信小程序审计架构
```
Phase 0: 需求解析
    ↓
Phase 1: 反编译 (Agent-01)
    ↓
Phase 1.5: 脚本预扫描
    ↓
Phase 2: 并行分析 (4 Agents)
┌──────────┬──────────┬──────────┬──────────┐
│SecretScan│Endpoint  │Crypto    │Vuln      │
│ner       │Miner     │Analyzer  │Analyzer  │
└──────────┴──────────┴──────────┴──────────┘
    ↓
Phase 2.5: 自定义分析 (Agent-07, 条件触发)
    ↓
Phase 3: 报告生成 (Agent-06)
```

### Java审计架构
```
Stage 1: 信息收集 (并行)
┌──────────┬──────────┬──────────┐
│Route     │Auth      │Vuln      │
│Mapper    │Auditor   │Scanner   │
└──────────┴──────────┴──────────┘
    ↓
Stage 2: 交叉分析 (并行)
    ↓
Stage 3: 调用链追踪 (动态Workers)
    ↓
Stage 4: 漏洞深度分析 (条件并行)
    ↓
Stage 5: 质量校验与报告
```

## 🔧 MCP服务配置

### registry.json
```json
{
  "servers": {
    "wxmini-server": {
      "url": "http://127.0.0.1:43827",
      "token": "${WXMINI_MCP_TOKEN}"
    },
    "java-server": {
      "url": "http://127.0.0.1:8082",
      "token": "${JAVA_MCP_TOKEN}"
    }
  }
}
```

## 🛡️ 安全原则

1. **纯静态分析** - 禁止发送网络请求
2. **不生成攻击代码** - 仅分析，不提供PoC
3. **最小权限** - 只读源码，只写输出目录
4. **本地处理** - 数据不上传第三方

## 🤝 参考项目

本项目深度集成了以下优秀开源项目:
- [ECC](https://github.com/affaan-m/ECC) - 企业级Agent框架
- [audit](https://github.com/evilsocket/audit) - 8阶段漏洞发现Agent
- [wxmini-security-audit](https://github.com/sssmmmwww/wxmini-security-audit) - 微信小程序审计
- [java-audit-skills](https://github.com/RuoJi6/java-audit-skills) - Java代码审计
- [wmpf-mcp-bridge](https://github.com/an7ln/wmpf-mcp-bridge) - MCP服务架构

## 📄 许可证

MIT License

**免责声明**: 本项目仅供安全研究与教育使用，请在授权范围内操作。
