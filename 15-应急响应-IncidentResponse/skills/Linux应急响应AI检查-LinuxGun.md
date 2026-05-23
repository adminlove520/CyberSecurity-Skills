---
id: 15-008
title: "🔫 Linux 应急响应 AI 检查 (LinuxGun AI Response)"
category: 应急响应
category_en: Incident Response
difficulty: ★★★★
tools: "LinuxGun, chkrootkit, rkhunter"
last_updated: 2026-05
tags: ["linux", "incident-response", "malware-analysis", "ai-security"]
subdomain: incident-response
nist_csf: ["RS.RP-01", "RS.AN-01"]
mitre_attack: ["T1070", "T1078", "T1543"]
---
# 🔫 Linux 应急响应 AI 检查 (LinuxGun AI Response)

## 概述
基于 AI 的 Linux 应急响应检查技能，通过渐进式披露原则，系统化排查系统信息、用户信息、进程、网络、文件等 16 个领域的风险。

## 核心技能

### 1. 系统性排查流程
- **用户信息排查**：分析 UID=0 用户、异常登录记录、隐藏账号。
- **恶意进程分析**：识别隐藏进程、高 CPU 占用进程、反弹 Shell 进程。
- **网络连接检测**：检查异常外联端口、建立的非法连接。
- **持久化检查**：审计 Cron 任务、启动脚本、SSH 后门。

### 2. 风险评估与处置
- **时间线构建**：通过文件改动时间（MAC time）构建攻击者行为时间线。
- **威胁分级**：根据风险评估矩阵判定威胁等级（高危、中危、低危）。

## 常用工具
| 工具 | 用途 | 链接 |
|:---|:---|:---|
| LinuxGun-skill | AI 应急响应技能集 | https://github.com/sun977/LinuxGun-skill |
| Volatility | 内存取证工具 | https://github.com/volatilityfoundation/volatility |

## 参考资源
- [Linux 应急响应 Checklist](https://github.com/sun977/LinuxGun-skill)
- [NIST Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf)
