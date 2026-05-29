# 🛡️ multi-CyberSecurity v3.2

### *AI驱动的网络安全智能体框架*

[![Version](https://img.shields.io/badge/version-3.0.0-blue?style=flat-square)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.8+-green?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/adminlove520/multi-CyberSecurity?style=flat-square&logo=github)](https://github.com/adminlove520/multi-CyberSecurity/stargazers)
[![Forks](https://img.shields.io/github/forks/adminlove520/multi-CyberSecurity?style=flat-square&logo=github)](https://github.com/adminlove520/multi-CyberSecurity/network/members)

---

<div align="center">

![Banner](./assets/banner.png)

**🚀 8阶段审计流水线 | 🤖 7核心智能体 | 🔌 MCP服务集 | 📱 专项审计**

</div>

---

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🤖 **多智能体协作** | 7个专家智能体协同工作 (Coordinator, Advisor, Recon, Exploit, Validator, Blue, Librarian) |
| 🎯 **8阶段审计流水线** | Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report |
| 🔌 **MCP服务集** | wxmini-server, java-server, burp-bridge, kali-bridge |
| 📱 **专项审计** | 微信小程序审计 (7-Agent), Java代码审计 (5阶段Pipeline) |
| 💰 **成本管控** | 预算控制与实时成本追踪 |
| ✅ **质量校验** | 每阶段自动校验，确保准确性 |
| 🌐 **多IDE支持** | Trae, Hermes, OpenClaw, Cursor, Claude, Codex |

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/adminlove520/multi-CyberSecurity.git
cd multi-CyberSecurity

# 安装依赖
pip install -r requirements.txt
```

### 快速命令

```bash
# 8阶段安全审计
python cli.py audit --target https://example.com --max-cost 50

# 微信小程序审计
python cli.py wxmini --path /path/to/miniapp --deep

# Java代码审计
python cli.py java --path /path/to/project --type full

# MCP服务管理
python cli.py mcp list
python cli.py mcp health

# 技能导出
python cli.py skill export --platform trae
```

---

## 🏗️ 架构概览

```
┌─────────────────────────────────────────────────────────────────┐
│                     multi-CyberSecurity v3.2                   │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │    .trae   │  │   .hermes   │  │  .openclaw  │  ← 平台配置  │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                        agents/                             │ │
│  │  core/              │  specialized/                      │ │
│  │  ├── Coordinator    │  ├── wxmini/ (7-Agent)            │ │
│  │  ├── Advisor         │  └── java/ (5-Stage)             │ │
│  │  ├── Recon           │                                   │ │
│  │  ├── Exploit         │                                   │ │
│  │  ├── Validator       │                                   │ │
│  │  ├── Blue            │                                   │ │
│  │  └── Librarian       │                                   │ │
│  └─────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                      framework/                             │ │
│  │  core/              │  mcp/              │  memory/        │ │
│  │  ├── pipeline.py    │  ├── client.py     │  ├── ...        │ │
│  │  ├── orchestrator  │  ├── registry.json│                 │ │
│  │  └── reporter      │  └── servers/     │                 │ │
│  └─────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                       skills/ (39个模块)                      │ │
│  │  01-信息搜集  │  12-代码审计  │  16-大模型安全  │ ...       │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 8阶段审计流水线

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Recon  │───→│  Hunt   │───→│Validate │───→│ Gapfill │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                 │
┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  Report │←───│Feedback │←───│  Trace  │←──────┘
└─────────┘    └─────────┘    └─────────┘
     ↑
┌─────────┐
│  Dedupe │
└─────────┘
```

| 阶段 | 功能 | 智能体 | 产出 |
|------|------|--------|------|
| Recon | 资产发现 | Recon Agent | 资产清单、技术栈 |
| Hunt | 漏洞扫描 | Exploit Agent | 漏洞列表 |
| Validate | 验证去误 | Validator Agent | 有效漏洞 |
| Gapfill | 缺口补充 | Advisor Agent | 补充发现 |
| Dedupe | 去重聚类 | Librarian Agent | 唯一漏洞 |
| Trace | 可达性追踪 | Recon Agent | 可利用漏洞 |
| Feedback | 模式提取 | Librarian Agent | 新扫描任务 |
| Report | 报告生成 | Coordinator Agent | 安全报告 |

---

## 📱 专项审计能力

### 微信小程序审计

```
Phase 0: 需求解析
    ↓
Phase 1: 反编译 (Agent-01)
    ↓
Phase 1.5: 脚本预扫描 (Python正则)
    ↓
Phase 2: 并行分析 (4路)
┌──────────┬──────────┬──────────┬──────────┐
│SecretScan│Endpoint  │Crypto    │Vuln      │
│ner       │Miner    │Analyzer  │Analyzer  │
└──────────┴──────────┴──────────┴──────────┘
    ↓
Phase 2.5: 自定义分析 (条件触发)
    ↓
Phase 3: 报告生成
```

### Java代码审计

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

---

## 🔌 MCP服务集

| 服务 | 端口 | 功能 |
|------|------|------|
| wxmini-server | 43827 | 微信小程序动态分析 |
| java-server | 8082 | Java代码审计 |
| burp-bridge | 8090 | Burp Suite集成 |
| kali-bridge | 8081 | Kali Linux工具 |

---

## 📚 技能目录

| 分类 | 数量 | 示例 |
|------|------|------|
| Web安全 | 20+ | SQL注入、XSS、CSRF |
| 移动安全 | 5+ | Android、iOS、小程序 |
| 代码审计 | 10+ | Java、Python、PHP、Go |
| 云安全 | 8+ | AWS、Azure、GCP |
| 应急响应 | 8+ | 取证、事件响应、溯源 |
| ... | ... | 39个安全领域全覆盖 |

---

## 🌐 多平台支持

| 平台 | 配置目录 | 状态 |
|------|----------|------|
| Trae | `.trae/` | ✅ 已支持 |
| Hermes | `.hermes/` | ✅ 已支持 |
| OpenClaw | `.openclaw/` | ✅ 已支持 |
| Cursor | `.cursor/` | 🔄 待扩展 |
| Claude | `.claude/` | 🔄 待扩展 |
| Codex | `.codex/` | 🔄 待扩展 |

---

## 🛡️ 安全原则

1. **纯静态分析** - 禁止发送未经授权的网络请求
2. **不生成攻击代码** - 仅分析，不提供武器化PoC
3. **最小权限** - 只读源码，只写输出目录
4. **本地处理** - 数据不上传任何第三方

---

## 📖 文档

- [📘 用户指南](./docs/guide/README.md)
- [🏗️ 架构文档](./docs/architecture/README.md)
- [🤖 Agent协作协议](./docs/workflow/README.md)
- [🔌 MCP集成指南](./docs/mcp/README.md)
- [📝 CLI参考](./docs/reference/CLI_REFERENCE.md)

---

## 🤝 参考项目

本项目整合了以下优秀开源项目:

| 项目 | 来源 | 功能 |
|------|------|------|
| [ECC](https://github.com/affaan-m/ECC) | affaan-m | 多平台适配架构 |
| [audit](https://github.com/evilsocket/audit) | evilsocket | 8阶段漏洞发现流水线 |
| [wxmini-security-audit](https://github.com/sssmmmwww/wxmini-security-audit) | sssmmmwww | 微信小程序审计Agent |
| [java-audit-skills](https://github.com/RuoJi6/java-audit-skills) | RuoJi6 | Java代码审计Pipeline |
| [wmpf-mcp-bridge](https://github.com/an7ln/wmpf-mcp-bridge) | an7ln | MCP服务架构 |

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

**⚠️ 免责声明**: 本项目仅供安全研究与教育使用，请在授权范围内操作。使用者需遵守相关法律法规。

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给它一个Star！**

[![Star](https://img.shields.io/github/stars/adminlove520/multi-CyberSecurity?style=social)](https://github.com/adminlove520/multi-CyberSecurity/stargazers)

</div>
