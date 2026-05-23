# 🧬 自主进化机制 (Evolution Mechanism)

## 1. 学习闭环 (Learning Loop)

```mermaid
graph LR
    Log[Mission Logs] -->|Analyze| Librarian[Librarian Agent]
    Librarian -->|Extract| Patterns[Attack Patterns]
    Patterns -->|Update| Skills[Skill Library]
    Skills -->|Empower| Future[Future Missions]
```

## 2. 知识蒸馏逻辑
`LibrarianAgent` 在任务结束后会执行以下逻辑：
1. **成功因子提取**：分析 `MISSION_CONTROL.md` 中标记为 `Verified` 的任务。
2. **脱敏处理**：移除特定目标的 IP、域名和凭证。
3. **抽象化**：将成功的命令序列转化为通用的技能 MD 模板。
4. **验证与存证**：将新技能存入 `framework/memory/patterns/`。

## 3. 手动触发
用户可以随时通过 CLI 启动进化引擎：
```bash
python skill.py evolve
```
