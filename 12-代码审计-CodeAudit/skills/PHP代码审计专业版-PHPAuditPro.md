---
id: 12-011
title: "🐘 PHP 代码审计专业版 (PHP Code Audit Pro)"
category: 代码审计
category_en: Code Audit
difficulty: ★★★★
tools: "PHP-Code-Audit-Skill, RIPS, Seay"
last_updated: 2026-05
tags: ["php", "code-audit", "white-box", "vulnerability-discovery"]
subdomain: code-audit
nist_csf: ["PR.IP-12", "DE.CM-08"]
mitre_attack: ["T1059.006", "T1190"]
---
# 🐘 PHP 代码审计专业版 (PHP Code Audit Pro)

## 概述
面向 PHP Web 的专业白盒代码安全审计技能，覆盖从路由枚举到漏洞验证的全流程审计，适用于 Cursor/Trae 等 AI Agent 环境。

## 核心技能

### 1. 审计全流程协议
- **路由枚举**：识别所有可访问的 Web 接口。
- **鉴权建模**：分析权限控制逻辑，发现越权漏洞。
- **数据流追踪**：追踪用户输入（Source）到敏感函数（Sink）的路径。
- **证据一致性校验**：通过静态分析验证漏洞的可利用性。

### 2. 专家级漏洞审计
覆盖 21 种以上漏洞类型，包括：
- 远程代码执行 (RCE)
- 反序列化漏洞 (Deserialization)
- 变量覆盖 (Variable Overloading)
- 弱类型比较 (Weak Comparison)

## 常用工具
| 工具 | 用途 | 链接 |
|:---|:---|:---|
| PHP-Code-Audit-Skill | 专业 PHP 审计 Skill | https://github.com/0xShe/PHP-Code-Audit-Skill |
| PHP_AUDIT_SKILLS | 多智能体协作审计框架 | https://github.com/yunmengya/PHP_AUDIT_SKILLS |

## 参考资源
- [PHP代码审计实战](https://github.com/0xShe/PHP-Code-Audit-Skill)
- [PHP安全指南](https://www.php.net/manual/zh/security.php)
