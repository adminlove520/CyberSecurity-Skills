# Security Capabilities

## 🌐 DNS枚举 (DNS Enumeration)
**Category**: 信息搜集
**Tools**: dnsenum, dig, nslookup, fierce

## 🎯 主动信息搜集 (Active Reconnaissance)
**Category**: 信息搜集
**Tools**: Nmap, Masscan, Zmap

## 🔗 子域名探测 (Subdomain Discovery)
**Category**: 信息搜集
**Tools**: Subfinder, Amass, Sublist3r

## 🖥️ 目标技术栈识别 (Technology Stack Fingerprinting)
**Category**: 信息搜集
**Tools**: WhatWeb, Wappalyzer, Nmap NSE, BuiltWith

## 👥 社会工程学信息收集 (Social Engineering Information Gathering)
**Category**: 信息搜集
**Tools**: theHarvester, Sherlock, Maltego

## 🌍 网络空间搜索引擎 (Cyberspace Search Engine)
**Category**: 信息搜集
**Tools**: Fofa, ZoomEye, Shodan, Censys

## 🕵️ 被动信息搜集 (Passive Reconnaissance / OSINT)
**Category**: 信息搜集
**Tools**: Google Dork, Shodan, Maltego, theHarvester

## 🤖 AI Agent漏洞扫描 (AI Agent Vulnerability Scanning)
**Category**: 漏洞扫描
**Tools**: Garak, Nuclei, LLM Proxy, OWASP LLM

## 📡 Web漏洞扫描 (Web Vulnerability Scanning)
**Category**: 漏洞扫描
**Tools**: Burp Suite, Nikto, Acunetix, OWASP ZAP

## 🗄️ 数据库安全评估 (Database Security Assessment)
**Category**: 漏洞扫描
**Tools**: SQLMap, NoSQLMap, MDAT, AppDetective

## 🤖 漏洞扫描器自动化 (Vulnerability Scanner Automation)
**Category**: 漏洞扫描
**Tools**: Nuclei, Nikto, 自定义脚本, Jenkins

## 🌐 网络漏洞扫描 (Network Vulnerability Scanning)
**Category**: 漏洞扫描
**Tools**: Nmap, OpenVAS, Nessus, Nexpose

## 🔧 配置审计扫描 (Configuration Audit Scanning)
**Category**: 漏洞扫描
**Tools**: Lynis, OpenSCAP, CIS-CAT, ScoutSuite

## 🤖 AI Agent漏洞利用 (AI Agent Exploitation)
**Category**: 漏洞利用
**Tools**: Garak, Counterfit, LLM Proxy, ART

## 💀 Metasploit框架利用 (Metasploit Framework Exploitation)
**Category**: 漏洞利用
**Tools**: Metasploit Framework, MSFVenom

## 💉 SQL注入利用 (SQL Injection Exploitation)
**Category**: 漏洞利用
**Tools**: SQLMap, NoSQLMap, 手动注入, jSQL

## 🔗 SSRF - 服务端请求伪造 (Server-Side Request Forgery)
**Category**: 漏洞利用
**Tools**: Gopherus, SSRFmap, Burp Collaborator

## 🌐 Web漏洞利用 (Web Exploitation)
**Category**: 漏洞利用
**Tools**: Burp Suite, SQLMap, XSStrike, Nuclei

## ⚡ XSS跨站脚本攻击 (Cross-Site Scripting Exploitation)
**Category**: 漏洞利用
**Tools**: BeEF, XSStrike, 手动构造Payload

## ⌨️ 命令注入 (Command Injection)
**Category**: 漏洞利用
**Tools**: Commix, 手动Payload构造

## 📂 文件包含与上传利用 (File Inclusion & Upload Exploitation)
**Category**: 漏洞利用
**Tools**: Burp Suite, 自定义脚本, PHP filter chains

## 🔐 认证绕过与权限绕过 (Authentication Bypass & Authorization Bypass)
**Category**: 漏洞利用
**Tools**: JWT_Tool, Burp Suite, 自定义脚本

## 🐧 Linux权限提升 (Linux Privilege Escalation)
**Category**: 权限提升
**Tools**: LinPEAS, Linux Exploit Suggester, GTFO Bins

## 🪟 Windows权限提升 (Windows Privilege Escalation)
**Category**: 权限提升
**Tools**: WinPEAS, PowerUp, PrivescCheck, Seatbelt

## ⬆️ 内核漏洞与服务配置错误提权 (Kernel Exploit & Service Misconfig PrivEsc)
**Category**: 权限提升
**Tools**: 漏洞利用代码, MSF模块, 自定义exp

## 🔑 凭证窃取与利用 (Credential Theft & Exploitation)
**Category**: 权限提升
**Tools**: Mimikatz, Lazagne, LaZagne, ProcDump

## 🕵️ 后渗透信息收集与数据窃取 (Post-Exploitation Info Gathering & Data Exfil)
**Category**: 后渗透
**Tools**: 系统命令, Powerview, 自定义脚本

## 🔑 凭证转储与哈希传递 (Credential Dumping & Pass-the-Hash)
**Category**: 后渗透
**Tools**: Mimikatz, Secretsdump, Lazagne, ProcDump

## 🖥️ 远程控制与交互式Shell (Remote Control & Interactive Shell)
**Category**: 后渗透
**Tools**: Cobalt Strike, Metasploit, Empire, PoshC2

## ⌨️ 键盘记录与屏幕捕获 (Keylogging & Screen Capture)
**Category**: 后渗透
**Tools**: Powershell Keylogger, Python pynput, Metasploit post模块

## 🔁 PsExec与WMI远程执行 (PsExec & WMI Remote Execution)
**Category**: 横向移动
**Tools**: PsExec, WMI, WinRM, Impacket

## 🔗 内网代理与隧道 (Internal Proxy & Tunneling)
**Category**: 横向移动
**Tools**: Chisel, FRP, Stowaway, Ngrok, Proxychains

## 🔄 横向移动 (Lateral Movement)
**Category**: 横向移动
**Tools**: BloodHound, CrackMapExec, Impacket

## Bootkit与固件持久化 (Bootkit & Firmware Persistence)
**Category**: 持久化
**Tools**: UEFI, SPI Flash, Chipsec, Flashrom, RWEverything

## Office应用程序持久化 (Office Application Persistence)
**Category**: 持久化
**Tools**: Office, VBA, COM, Outlook, Add-in

## 启动项与登录自动执行 (Boot/Logon Autostart)
**Category**: 持久化
**Tools**: Regedit, Autoruns, schtasks, systemd, launchd

## 🔐 持久化 - 长期控制 (Persistence - Long-term Access)
**Category**: 持久化
**Tools**: MSF Venom, Cobalt Strike, 计划任务, 自启动项

## 账户创建与凭证持久化 (Account Persistence)
**Category**: 持久化
**Tools**: net user, dsquery, ssh-keygen, Azure AD, IAM

## AMSI绕过与EDR规避 (AMSI Bypass & EDR Evasion)
**Category**: 痕迹清除
**Tools**: AMSI, ETW, Sysmon, EDR, Bypass Tools

## 代码混淆与反分析 (Code Obfuscation & Anti-Analysis)
**Category**: 痕迹清除
**Tools**: ConfuserEx, Obfuscator-LLVM, UPX, VMP, dnSpy, x64dbg

## 🧹 痕迹清除 (Covering Tracks / Anti-Forensics)
**Category**: 痕迹清除
**Tools**: 日志清除, 文件隐藏, 时间戳修改, 反取证技术

## 进程注入与代码注入 (Process Injection & Code Injection)
**Category**: 痕迹清除
**Tools**: Cobalt Strike, Meterpreter, PowerSploit, Process Hollowing, APC

## 🌐 安全报告模板 - HTML格式 (Security Report Template - HTML)
**Category**: 报告撰写
**Tools**: Chart.js, HTML/CSS, Python, JavaScript

## 📄 安全报告模板 - Markdown格式 (Security Report Template - Markdown)
**Category**: 报告撰写
**Tools**: Typora, VS Code, Mermaid, Python

## 📝 安全报告模板 - Word/PDF格式 (Security Report Template - Word/PDF)
**Category**: 报告撰写
**Tools**: python-docx, LibreOffice, Word

## 📝 渗透测试报告编写 (Penetration Test Report Writing)
**Category**: 报告撰写
**Tools**: 结构化模板, 质量标准, Markdown

## 📊 漏洞评级与CVSS评分 (Vulnerability Rating & CVSS Scoring)
**Category**: 报告撰写
**Tools**: CVSS 3.1/4.0, DREAD, OWASP Risk Rating

## 📱 Android安全测试 (Android Security Testing)
**Category**: 移动安全
**Tools**: drozer, Frida, APKTool, MobSF, Jadx

## 🍎 iOS安全测试 (iOS Security Testing)
**Category**: 移动安全
**Tools**: Frida, Objection, class-dump, Ghidra, checkra1n

## 📶 Wi-Fi安全审计 (Wi-Fi Security Audit)
**Category**: 无线安全
**Tools**: Aircrack-ng, Wireshark, Airodump-ng, Hashcat

## 🤖 AI Agent代码审计 (AI Agent Code Audit)
**Category**: 代码审计
**Tools**: Semgrep, Bandit, CodeQL, Garak

## 🔧 C++代码审计 (C++ Code Audit)
**Category**: 代码审计
**Tools**: Cppcheck, Clang-Tidy, PVS-Studio, CodeQL

## ⚙️ C代码审计 (C Code Audit)
**Category**: 代码审计
**Tools**: Flawfinder, Cppcheck, ASan, Valgrind

## 🐹 Go代码审计 (Go Code Audit)
**Category**: 代码审计
**Tools**: gosec, staticcheck, govulncheck, Semgrep

## 🌐 JavaScript/Node.js代码审计 (JavaScript & Node.js Code Audit)
**Category**: 代码审计
**Tools**: ESLint, RetireJS, Semgrep, CodeQL

## ☕ Java代码审计 (Java Code Audit)
**Category**: 代码审计
**Tools**: FindSecBugs, SpotBugs, Fortify, Semgrep

## ☕ Java 代码审计进阶 (Java Audit Advanced)
**Category**: 代码审计
**Tools**: CFR, java-route-mapper, java-sql-audit

## 🔍 PHP代码审计 (PHP Code Audit)
**Category**: 代码审计
**Tools**: RIPS, phpcs, Psalm, Phan, 手动审查

## 🐘 PHP 代码审计专业版 (PHP Code Audit Pro)
**Category**: 代码审计
**Tools**: PHP-Code-Audit-Skill, RIPS, Seay

## 🐍 Python代码审计 (Python Code Audit)
**Category**: 代码审计
**Tools**: Bandit, Semgrep, Pyre, CodeQL

## 🦀 Rust代码审计 (Rust Code Audit)
**Category**: 代码审计
**Tools**: Clippy, cargo-audit, cargo-geiger, Miri

## ⚙️ 动态调试分析 (Dynamic Debug Analysis)
**Category**: 逆向工程
**Tools**: x64dbg, OllyDbg, GDB, WinDbg, Immunity

## 🦠 恶意软件分析 (Malware Analysis)
**Category**: 逆向工程
**Tools**: Cuckoo Sandbox, CAPE, YARA, Ghidra, FLOSS, PEStudio

## 🔬 静态逆向分析 (Static Reverse Engineering)
**Category**: 逆向工程
**Tools**: IDA Pro, Ghidra, Radare2, Binary Ninja

## 🤖 AI Agent安全审计 (AI Agent Security Audit)
**Category**: 安全审计
**Tools**: OWASP LLM VS, CSA CCM, Prowler, Garak

## ☁️ 云安全审计 (Cloud Security Audit)
**Category**: 安全审计
**Tools**: ScoutSuite, Prowler, CloudSploit, Pacu

## 🏗️ 安全架构审计 (Security Architecture Audit)
**Category**: 安全审计
**Tools**: 威胁建模工具, Archi, draw.io, STRIDE

## 🐳 容器安全审计 (Container Security Audit)
**Category**: 安全审计
**Tools**: Trivy, Dockle, kube-bench, Falco, Dagda

## 🏛️ 等级保护合规审计 (Classified Protection Compliance Audit)
**Category**: 安全审计
**Tools**: 等保自查工具, 合规扫描平台

## 🌐 网络安全合规评估 (Network Security Compliance Assessment)
**Category**: 安全审计
**Tools**: Nmap NSE, Wireshark, Nipper, OpenVAS

## 🔧 配置安全审计 (Configuration Security Audit)
**Category**: 安全审计
**Tools**: Lynis, OpenSCAP, CIS-CAT, Chef InSpec

## 🤖 AI安全应急响应 (AI Security Incident Response)
**Category**: 应急响应
**Tools**: AI IR Framework, MITRE ATLAS, TheHive

## 🔫 Linux 应急响应 AI 检查 (LinuxGun AI Response)
**Category**: 应急响应
**Tools**: LinuxGun, chkrootkit, rkhunter

## 📋 事件分类与优先级评估 (Incident Triage & Prioritization)
**Category**: 应急响应
**Tools**: 事件管理平台, SIRP工具, TheHive

## 📝 事件复盘与报告 (Lessons Learned & Reporting)
**Category**: 应急响应
**Tools**: 复盘模板, Root Cause分析, 5 Whys

## 🛑 事件遏制与清除 (Containment & Eradication)
**Category**: 应急响应
**Tools**: Firewall ACL, EDR隔离, GPO, 网络分段

## ☁️ 云环境应急响应 (Cloud Incident Response)
**Category**: 应急响应
**Tools**: AWS GuardDuty, Azure Sentinel, GCP Security

## 📜 日志收集与分析 (Log Collection & Analysis)
**Category**: 应急响应
**Tools**: ELK Stack, Splunk, Wazuh, Graylog

## 🌐 网络流量分析 (Network Traffic Analysis)
**Category**: 应急响应
**Tools**: Wireshark, Zeek, Suricata, tcpdump

## 🔐 AI Agent权限与访问控制 (Agent Authorization & Access Control)
**Category**: 大模型安全
**Tools**: OAuth 2.0, OIDC, RBAC, OWASP LLM-08

## 📦 AI供应链安全 (AI Supply Chain Security)
**Category**: 大模型安全
**Tools**: SBOM工具, SLSA框架, Snyk, Trivy

## ⚙️ AI应用安全配置审计 (AI Application Security Configuration Audit)
**Category**: 大模型安全
**Tools**: OWASP ASVS, CIS AI Benchmarks, Semgrep

## 🧪 LLM提示注入与安全防护 (Prompt Injection & Defense)
**Category**: 大模型安全
**Tools**: 提示注入检测工具, Garak, LLM Guard, NVIDIA NeMo

## 🔒 LLM数据泄露与隐私保护 (Data Leakage & Privacy Protection)
**Category**: 大模型安全
**Tools**: 数据脱敏工具, 隐私检测, Presidio, 差分隐私库

## 🎨 多模态AI安全 (Multimodal AI Security)
**Category**: 大模型安全
**Tools**: 对抗样本工具, 多模态检测器, CLIP, Stable Diffusion

## 🎯 大模型红队测试 (LLM Red Teaming)
**Category**: 大模型安全
**Tools**: Garak, Counterfit, ART, PyRIT, LLM Red Team

## 🛡️ 模型对抗攻击与防御 (Adversarial Attack & Defense)
**Category**: 大模型安全
**Tools**: ART, CleverHans, Foolbox, Adversarial Robustness

## 📝 模型输出安全与幻觉检测 (Output Safety & Hallucination Detection)
**Category**: 大模型安全
**Tools**: Guardrails, Nemo Guardrails, 幻觉检测模型

## 🤝 联邦学习安全 (Federated Learning Security)
**Category**: 大模型安全
**Tools**: TensorFlow Federated, PySyft, FATE, 安全聚合

## ☁️ AWS安全评估 (AWS Security Assessment)
**Category**: 云安全
**Tools**: Prowler, ScoutSuite, AWS Config, Security Hub, PacBot

## 🌤️ Azure安全评估 (Azure Security Assessment)
**Category**: 云安全
**Tools**: Azucar, ScoutSuite, Azure Security Center, Microsoft Defender for Cloud

## 🟢 GCP安全评估 (GCP Security Assessment)
**Category**: 云安全
**Tools**: Forseti Security, GCP Inspector, ScoutSuite, gcloud CLI

## 🔑 云IAM权限与访问控制审计 (Cloud IAM Audit)
**Category**: 云安全
**Tools**: AWS IAM Access Analyzer, Azure AD, gcloud IAM, Principal Mapper, Cloudsplaining

## 💾 云存储安全配置审计 (Cloud Storage Security)
**Category**: 云安全
**Tools**: S3 Scanner, CloudSploit, gsutil, Azure Storage Explorer

## 🌐 云网络与WAF安全 (Cloud Network & WAF Security)
**Category**: 云安全
**Tools**: AWS WAF, Azure WAF, Cloud Armor, Security Groups, CloudSploit

## 🔄 多云安全策略评估 (Multi-Cloud Security Strategy)
**Category**: 云安全
**Tools**: Prisma Cloud, Wiz, Orca Security, Lacework, Aqua Security

## ⚡ 无服务器架构安全 (Serverless Security)
**Category**: 云安全
**Tools**: AWS Lambda Check, Serverless Framework, PureSec, Snyk

## 🔗 CI/CD管道安全审计 (CI/CD Pipeline Security)
**Category**: 安全开发运维
**Tools**: GitLab CI Security, Jenkins Security Scanner, GitGuardian, TruffleHog

## 🌐 DAST动态应用安全测试 (Dynamic Application Security Testing)
**Category**: 安全开发运维
**Tools**: OWASP ZAP, Burp Suite, Acunetix, Arachni, Nikto

## 📦 IaC安全扫描 (Infrastructure as Code Security)
**Category**: 安全开发运维
**Tools**: Checkov, Terrascan, tfsec, KICS, cfn-nag, kube-lint

## 🔍 SAST静态应用安全测试 (Static Application Security Testing)
**Category**: 安全开发运维
**Tools**: SonarQube, Semgrep, CodeQL, Fortify, Checkmarx

## 🧠 安全需求与威胁建模 (Security Requirements & Threat Modeling)
**Category**: 安全开发运维
**Tools**: STRIDE, PASTA, Threat Dragon, OWASP Cornucopia, Microsoft TMT

## 🔗 软件供应链安全 (Software Supply Chain Security)
**Category**: 安全开发运维
**Tools**: Snyk, Dependabot, Trivy, SBOM, Sigstore, OWASP DC

## 🔧 PLC与RTU安全测试 (PLC & RTU Security Testing)
**Category**: 工控安全
**Tools**: ISF (ICS Exploitation Framework), Metasploit, Industrial Exploitation Suite, C0br4.sh

## ⚙️ SCADA系统安全评估 (SCADA System Security Assessment)
**Category**: 工控安全
**Tools**: PLCScan, Modbus/TCP Scanner, Shodan, Nmap NSE, Wireshark

## 🔒 工业防火墙与网络分段 (Industrial Firewall & Segmentation)
**Category**: 工控安全
**Tools**: Tofino Security, Claroty, Nozomi, pfSense, iptables

## 📋 工控安全合规审计 - IEC 62443 (ICS Compliance Audit - IEC 62443)
**Category**: 工控安全
**Tools**: IEC 62443 Checklist, ICS Compliant, C2M2, NIST CSF

## 🚨 工控安全应急预案 (ICS Incident Response)
**Category**: 工控安全
**Tools**: Dragos Platform, Claroty, Nozomi, Wireshark, YARA

## 🌐 工控网络协议安全 (ICS Network Protocol Security)
**Category**: 工控安全
**Tools**: Wireshark, Scapy, Zabbix, Modbus-cli, OPC UA Expert

## 💰 DeFi协议安全评估 (DeFi Protocol Security Assessment)
**Category**: 区块链安全
**Tools**: Hardhat, Foundry, DeFi-Scanner, Tenderly, Dune Analytics

## ⚡ MEV与跨链桥安全 (MEV & Cross-Chain Bridge Security)
**Category**: 区块链安全
**Tools**: MEV-Inspect, Flashbots, Bridge Audit Tools, LayerZero, Chainlink CCIP

## 🖥️ Web3前端与钱包安全 (Web3 Frontend & Wallet Security)
**Category**: 区块链安全
**Tools**: MetaMask Security, Ethers.js, Web3.js, WalletConnect, EIP-1193

## 🔗 共识机制安全分析 (Consensus Mechanism Security)
**Category**: 区块链安全
**Tools**: Prysm, Lighthouse, Teku, Eth2, Cosmos SDK Security

## 🛡️ 区块链节点安全加固 (Blockchain Node Hardening)
**Category**: 区块链安全
**Tools**: Geth, Lighthouse, Prysm, Erigon, Nethermind, Firewall

## 📝 智能合约安全审计 (Smart Contract Audit)
**Category**: 区块链安全
**Tools**: Slither, Mythril, Certora, Echidna, Foundry, Hardhat

## 📶 BLE/Zigbee/Z-Wave无线安全测试 (Wireless Protocol Security Testing)
**Category**: 物联网安全
**Tools**: BLEAH, GATTool, Z3sec, HackRF, BetterCAP, Ubertooth

## 🔧 固件逆向与分析 (Firmware Reverse Engineering)
**Category**: 物联网安全
**Tools**: Binwalk, Firmadyne, Ghidra, QEMU, GDB, JTAGulator

## ⚙️ 嵌入式设备硬件安全测试 (Embedded Hardware Security)
**Category**: 物联网安全
**Tools**: JTAGulator, OpenOCD, Saleae Logic, Bus Pirate, ChipWhisperer

## 🏠 智能家居与车联网安全 (Smart Home & Connected Vehicle Security)
**Category**: 物联网安全
**Tools**: Home Assistant, CANtact, UDSim, ICSim, OpenVehicles

## ☁️ 物联网平台与云安全 (IoT Platform & Cloud Security)
**Category**: 物联网安全
**Tools**: AWS IoT Auditor, Azure IoT Hub Security, GCP IoT Core, TLS Notary

## 🌐 物联网通信协议安全 (IoT Communication Security)
**Category**: 物联网安全
**Tools**: MQTT Pwn, MQTTSA, Wireshark, nmap, MQTTCheck

## 🛡️ DLP数据防泄漏策略 (Data Loss Prevention)
**Category**: 数据安全与隐私
**Tools**: Microsoft DLP, Symantec DLP, Digital Guardian, Forcepoint DLP, OpenDLP

## 🌍 GDPR/个保法合规评估 (Privacy Compliance Assessment)
**Category**: 数据安全与隐私
**Tools**: OneTrust, TrustArc, DPIA Toolkit, CNIL PIA Tool, Securiti.ai

## 📋 数据分类与分级保护 (Data Classification & Grading)
**Category**: 数据安全与隐私
**Tools**: Data Classification Toolkit, Varonis, Microsoft Purview, BigID, Spirion

## 🗄️ 数据库安全与加密 (Database Security & Encryption)
**Category**: 数据安全与隐私
**Tools**: Vault, CipherTrust, SQL Audit Tools, pgAudit, MySQL Audit Plugin

## 🔏 数据脱敏与匿名化 (Data Masking & Anonymization)
**Category**: 数据安全与隐私
**Tools**: ARX Data Anonymizer, Privacy Analytics, Oracle DPM, PostgreSQL Anonymizer, Delphix

## 📝 隐私影响评估(PIA) (Privacy Impact Assessment)
**Category**: 数据安全与隐私
**Tools**: CNIL PIA Tool, OneTrust DPIA, PIA Template, DPIA Toolkit

## 📊 员工安全意识评估 (Security Awareness Assessment)
**Category**: 社会工程学
**Tools**: KnowBe4, Phish Insight, CyberArk, PhishLabs, Wizer

## 🏢 物理渗透与社会工程 (Physical Social Engineering)
**Category**: 社会工程学
**Tools**: Pretexting Framework, Badge Clone, Lockpick Set, RFID Cloner

## 📞 电话诈骗与Vishing测试 (Vishing Testing)
**Category**: 社会工程学
**Tools**: SET (Social Engineering Toolkit), Twilio, Asterisk, CallerID Spoofer

## ⚙️ 钓鱼基础设施搭建 (Phishing Infrastructure)
**Category**: 社会工程学
**Tools**: GoPhish, Modlishka, Muraena, Evilginx2, Nginx

## 🎣 钓鱼邮件模拟 (Phishing Simulation)
**Category**: 社会工程学
**Tools**: GoPhish, Evilginx2, SET, Modlishka, Muraena

## 🤖 Agent 黑客技能集 (Agent Hack Skills)
**Category**: 红蓝对抗
**Tools**: HACK.SKILLS, yaklang, nuclei

## ⚡ BAS攻击模拟平台 (Breach & Attack Simulation)
**Category**: 红蓝对抗
**Tools**: Atomic Red Team, Stratus Red Team, CALDERA, AttackIQ, Picus Security

## 🟣 紫队协作评估 (Purple Team Exercise)
**Category**: 红蓝对抗
**Tools**: CALDERA, SCYTHE, AttackIQ, Atomic Red Team, PurpleSharp

## 🔴 红队评估方法论 (Red Team Assessment)
**Category**: 红蓝对抗
**Tools**: Cobalt Strike, CALDERA, Sliver, Nighthawk, Mythic

## 🔵 蓝队防御与检测 (Blue Team Defense & Detection)
**Category**: 红蓝对抗
**Tools**: Splunk, Wazuh, Elastic Security, Sentinel, Sigma Rules

## 🔄 闭环防御改进 (Defense Improvement Cycle)
**Category**: 红蓝对抗
**Tools**: Purple Team Metrics, Detection Gap Analysis, Jira, Confluence, MITRE Navigator

## 📦 SBOM生成与验证 (SBOM Generation & Verification)
**Category**: 供应链安全
**Tools**: Syft, CycloneDX, SPDX, Trivy, Dependency-Track, FOSSA

## 📝 代码签名与供应链完整性 (Code Signing & Supply Chain Integrity)
**Category**: 供应链安全
**Tools**: cosign, sigstore, GnuPG, notary, in-toto, TUF

## 🎯 供应链攻击检测与响应 (Supply Chain Attack Detection & Response)
**Category**: 供应链安全
**Tools**: GuardDog, GraphQL API Security, Falco, Network Policy, OPA

## 🏢 第三方供应商风险评估 (Third-Party Vendor Risk Assessment)
**Category**: 供应链安全
**Tools**: BitSight, SecurityScorecard, OneTrust Vendor Risk, Prevalent, Panorays

## 🔍 软件依赖与开源合规审计 (Dependency License Compliance)
**Category**: 供应链安全
**Tools**: FOSSA, Black Duck, Snyk, OWASP Dependency-Check, Scancode

## 📊 漏洞优先级与风险评估 (Vulnerability Prioritization & Risk Assessment)
**Category**: 漏洞管理
**Tools**: CVSS Calculator, EPSS, VPR, Kenna.VM, Qualys VMDR, RiskSense, Vulcan Cyber

## 🔧 漏洞修复与补丁管理 (Vulnerability Remediation & Patch Management)
**Category**: 漏洞管理
**Tools**: WSUS, SCCM, Ansible, Puppet, Satellite, Patch Manager, Tanium, Automox

## 🏆 漏洞奖励计划与安全众测 (Bug Bounty & Crowdsourced Testing)
**Category**: 漏洞管理
**Tools**: HackerOne, Bugcrowd, Synack, 补天平台, 漏洞盒子, Intigriti, YesWeHack

## 🔍 漏洞情报与CVE查询 (Vulnerability Intelligence & CVE Query)
**Category**: 漏洞管理
**Tools**: NVD API, CVE-Search, OSV.dev, Exploit-DB, Shodan, Google Dorks, VulnDB, CNNVD

## 🔄 漏洞生命周期闭环管理 (Vulnerability Lifecycle Management)
**Category**: 漏洞管理
**Tools**: DefectDojo, Archer, ServiceNow, Jira Security, Kenna.VM, Vulcan, Brinqa

## 🧪 漏洞验证与PoC测试 (Vulnerability Verification & PoC Testing)
**Category**: 漏洞管理
**Tools**: Nuclei, Metasploit, Exploit-DB, PoC-in-GitHub, VulnX, Docker, Vagrant

## Linux安全加固与基线检查 (Linux Hardening & Baseline)
**Category**: 操作系统安全
**Tools**: CIS Benchmarks, 等保2.0, Lynis, OpenSCAP, auditd, SELinux, AppArmor

## Linux攻击与权限维持技术 (Linux Attack & Persistence)
**Category**: 操作系统安全
**Tools**: LinPEAS, GTFO Bins, systemctl, kernel-exploit, Rootkit, Chisel, Ligolo

## macOS安全评估与加固 (macOS Security Assessment & Hardening)
**Category**: 操作系统安全
**Tools**: SIP, TCC, MDM, osquery, Santa, BlockBlock, KnockKnock, objective-see tools

## Windows安全加固与基线检查 (Windows Hardening & Baseline)
**Category**: 操作系统安全
**Tools**: CIS Benchmarks, 等保2.0, GPO, LGPO, Microsoft Security Compliance Toolkit, Windows Defender

## Windows攻击与横向移动技术 (Windows Attack & Lateral Movement)
**Category**: 操作系统安全
**Tools**: Impacket, Mimikatz, Rubeus, BloodHound, CrackMapExec, Responder, Certify

## 国产操作系统安全加固 (Domestic OS Security Hardening)
**Category**: 操作系统安全
**Tools**: KylinOS, UOS, openEuler, 等保2.0, SM2/SM3/SM4, kylin-security-toolkit

## 基于ATT&CK的威胁狩猎 (MITRE ATT&CK Threat Hunting)
**Category**: 威胁狩猎
**Tools**: ATT&CK Navigator, Red Canary, Atomic Red Team, Caldera, MITRE ATT&CK

## 基于Sigma规则的检测工程 (Sigma Rule Detection Engineering)
**Category**: 威胁狩猎
**Tools**: Sigma, PySigma, sigma-cli, Elastic, Splunk, QRadar

## 威胁狩猎方法论与假设驱动 (Threat Hunting Methodology & Hypothesis)
**Category**: 威胁狩猎
**Tools**: Splunk, Elastic, Jupyter, Sigma, ATT&CK Navigator

## 网络流量与日志异常检测 (Network Traffic & Log Anomaly Detection)
**Category**: 威胁狩猎
**Tools**: Zeek, Suricata, tcpdump, Elastic, Splunk, Jupyter

## APT组织分析与归因 (APT Group Analysis & Attribution)
**Category**: 威胁情报
**Tools**: ATT&CK Navigator, MISP, Malpedia, VirusTotal, PassiveTotal

## MISP平台部署与威胁情报共享 (MISP Deployment & Threat Intel Sharing)
**Category**: 威胁情报
**Tools**: MISP, Docker, Cortex, MISP Galaxy, PyMISP

## 威胁情报馈入与TAXII/STIX管理 (Threat Intelligence Feeds & TAXII/STIX)
**Category**: 威胁情报
**Tools**: TAXII, STIX, MISP, OpenCTI, MITRE CTI

## 威胁情报驱动安全运营 (Threat Intel Driven Security Operations)
**Category**: 威胁情报
**Tools**: Splunk, Elastic, MISP, TheHive, OpenCTI, Shuffle

## Linux数字取证分析 (Linux Digital Forensics)
**Category**: 数字取证
**Tools**: autopsy, sleuthkit, linux-ir, auditd, osquery, chkrootkit

## Windows数字取证分析 (Windows Digital Forensics)
**Category**: 数字取证
**Tools**: KAPE, Hayabusa, Eric Zimmerman Tools, Plaso, Event Log Explorer

## 内存取证分析 (Memory Forensics with Volatility)
**Category**: 数字取证
**Tools**: Volatility 3, Volatility 2, LiME, WinPmem, FTK Imager, Rekall, YARA

## 浏览器与邮件取证 (Browser & Email Forensics)
**Category**: 数字取证
**Tools**: BrowserHistoryView, DB Browser for SQLite, MailStore, readpst, oletools

## 磁盘镜像与证据获取 (Disk Imaging & Evidence Acquisition)
**Category**: 数字取证
**Tools**: dd, dcfldd, guymager, FTK Imager, Sleuth Kit, Autopsy, Plaso, Photorec

## SIEM告警规则与关联分析 (SIEM Alert Rules & Correlation)
**Category**: SOC运营
**Tools**: Splunk, Elastic Security, Azure Sentinel, QRadar, Sigma

## SOC事件分级与响应流程 (SOC Triage & Response)
**Category**: SOC运营
**Tools**: TheHive, ServiceNow, Jira, Splunk, IR Framework

## SOC指标与运营效能度量 (SOC Metrics & Operational KPIs)
**Category**: SOC运营
**Tools**: Splunk Dashboards, Elastic, Grafana, Power BI, SOC Dashboard

## 安全自动化与编排 (Security Automation & Orchestration - SOAR)
**Category**: SOC运营
**Tools**: Shuffle, Splunk SOAR, Tines, Palo Alto XSOAR, n8n

## AD域安全与攻击路径分析 (AD Security & Attack Path Analysis)
**Category**: 身份与访问管理
**Tools**: BloodHound, PingCastle, Purple Knight, AD Explorer, PowerView

## PAM特权账号管理 (Privileged Access Management)
**Category**: 身份与访问管理
**Tools**: CyberArk, HashiCorp Vault, BeyondTrust, ManageEngine, Teleport

## 云IAM与联邦认证 (Cloud IAM & Federation)
**Category**: 身份与访问管理
**Tools**: AWS IAM, GCP IAM, Azure RBAC, Okta, Terraform

## 企业IAM策略与架构 (Enterprise IAM Strategy & Architecture)
**Category**: 身份与访问管理
**Tools**: Okta, Azure AD, Keycloak, LDAP, FreeIPA

## Kubernetes RBAC与安全策略 (Kubernetes RBAC & Security Policy)
**Category**: 容器安全
**Tools**: kubectl, OPA/Gatekeeper, Kyverno, kube-bench, kube-hunter

## 容器运行时安全 (Container Runtime Security with Falco)
**Category**: 容器安全
**Tools**: Falco, tracee, Sysdig, Cilium Tetragon, Seccomp

## 容器逃逸检测与防御 (Container Escape Detection & Defense)
**Category**: 容器安全
**Tools**: Falco, AppArmor, Seccomp, gVisor, kata-containers

## 容器镜像安全与漏洞扫描 (Container Image Security & Scanning)
**Category**: 容器安全
**Tools**: Trivy, Grype, Docker Scout, Clair, Cosign, Syft

## API认证与授权安全 (API Authentication & Authorization Security)
**Category**: API安全
**Tools**: OAuth 2.0, OIDC, JWT, Keycloak, Auth0

## GraphQL与微服务API安全 (GraphQL & Microservice API Security)
**Category**: API安全
**Tools**: GraphQL Inspector, GraphQL Armor, WAF, Istio, Envoy

## OWASP API安全测试 (OWASP API Security Testing)
**Category**: API安全
**Tools**: Burp Suite, Postman, OWASP ZAP, k6, curl

## PKI架构与证书安全管理 (PKI Architecture & Certificate Management)
**Category**: 密码学与PKI
**Tools**: OpenSSL, EasyRSA, CFSSL, Vault PKI, EJBCA

## TLS/SSL安全配置与审计 (TLS/SSL Security Configuration & Audit)
**Category**: 密码学与PKI
**Tools**: OpenSSL, testssl.sh, nmap, certbot, SSL Labs

## 加密算法与密钥管理 (Encryption Algorithms & Key Management)
**Category**: 密码学与PKI
**Tools**: OpenSSL, GPG, HashiCorp Vault, HSM, age

## ZTNA解决方案与IAM集成 (ZTNA Solutions & IAM Integration)
**Category**: 零信任架构
**Tools**: Zscaler ZPA, Cloudflare Access, Perimeter 81, Appgate, Twingate

## 微隔离与软件定义边界 (Microsegmentation & Software-Defined Perimeter)
**Category**: 零信任架构
**Tools**: Illumio, NSX, Calico, Tailscale, WireGuard

## 零信任架构设计与实施 (Zero Trust Architecture Design & Implementation)
**Category**: 零信任架构
**Tools**: Google BeyondCorp, AWS Verified Access, Azure AD, Cloudflare Access

## EDR部署与检测规则 (EDR Deployment & Detection Rules)
**Category**: 端点安全
**Tools**: CrowdStrike Falcon, Microsoft Defender, SentinelOne, Elastic EDR, Velociraptor

## 文件less恶意软件与LOLBins检测 (Fileless Malware & LOLBins Detection)
**Category**: 端点安全
**Tools**: Sysmon, PowerShell Logging, AMSI, KAPE, Hayabusa

## 移动设备安全与MDM (Mobile Device Security & MDM)
**Category**: 端点安全
**Tools**: Intune, Jamf, MaaS360, MobileIron, Workspace ONE

## 端点加固与合规基线 (Endpoint Hardening & Compliance Baseline)
**Category**: 端点安全
**Tools**: CIS Benchmarks, Microsoft Baselines, OpenSCAP, InSpec, Ansible

## 勒索软件应急响应与恢复 (Ransomware Incident Response & Recovery)
**Category**: 勒索软件防御
**Tools**: EDR, SIEM, KAPE, Velociraptor, CyberReason

## 勒索软件攻击链分析与检测 (Ransomware Attack Chain Analysis & Detection)
**Category**: 勒索软件防御
**Tools**: YARA, Sigma, Elastic, Splunk, Any.Run, Joe Sandbox

## 反勒索软件加固与备份策略 (Anti-Ransomware Hardening & Backup Strategy)
**Category**: 勒索软件防御
**Tools**: Veeam, Azure Backup, AWS Backup, Rubrik, Cohesity

## 安全框架与合规审计 (Security Framework & Compliance Audit)
**Category**: 安全治理与合规
**Tools**: NIST CSF, ISO 27001, SOC 2, CIS Controls, AuditBoard

## 安全策略体系与安全意识 (Security Policy & Awareness)
**Category**: 安全治理与合规
**Tools**: KnowBe4, PhishER, SharePoint, Confluence, Snyk

## 风险管理与安全度量 (Risk Management & Security Metrics)
**Category**: 安全治理与合规
**Tools**: FAIR, RiskLens, Archer, Jira, Grafana

