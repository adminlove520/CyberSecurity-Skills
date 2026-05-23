---
id: 12-010
title: "☕ Java 代码审计进阶 (Java Audit Advanced)"
category: 代码审计
category_en: Code Audit
difficulty: ★★★★
tools: "CFR, java-route-mapper, java-sql-audit"
last_updated: 2026-05
tags: ["java", "code-audit", "static-analysis", "vulnerability-research"]
subdomain: code-audit
nist_csf: ["PR.IP-12", "DE.CM-08"]
mitre_attack: ["T1059.003", "T1190"]
---
# ☕ Java 代码审计进阶 (Java Audit Advanced)

## 概述
专注于 Java 代码审计的进阶技能集合，提供自动化源码分析、路由提取、参数映射等功能，辅助安全研究人员进行 Java Web 应用的深度安全审计。

## 核心技能

### 1. 自动路由识别
自动识别 Java Web 项目中的 HTTP 路由结构，支持 Spring MVC、Servlet、JAX-RS、Struts 2 等主流框架。
- 提取 Path、Query、Body、Header、Cookie 等各类参数。
- 识别鉴权框架实现，分析鉴权绕过和越权访问风险。

### 2. 漏洞深度分析
- **SQL 注入审计**：识别 SQL 执行框架（MyBatis, Hibernate, JDBC），检测 SQL 注入漏洞风险。
- **文件操作审计**：识别文件上传与读取入口，分析路径穿越和恶意文件上传风险。
- **XXE 审计**：识别 XML 解析操作，检测外部实体注入漏洞。
- **调用链追踪**：追踪从 Controller 到 DAO 层的完整调用链，分析参数流向。

### 3. 组件漏洞检测
扫描第三方依赖（Maven, Gradle），匹配 CVE 规则，生成安全报告。

## 常用工具
| 工具 | 用途 | 链接 |
|:---|:---|:---|
| CFR | Java 反编译器 | https://www.benf.org/other/cfr/ |
| java-audit-skills | 自动化 Java 审计工具集 | https://github.com/RuoJi6/java-audit-skills |
| FindSecBugs | 静态分析插件 | https://find-sec-bugs.github.io/ |

## 参考资源
- [Java代码审计知识库](https://github.com/RuoJi6/java-audit-skills)
- [OWASP Java Security Guide](https://cheatsheetseries.owasp.org/cheatsheets/Java_Server_Faces_Security_Cheat_Sheet.html)
