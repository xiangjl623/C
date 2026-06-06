# 编程语言

按语言组织的系统教程、速查表、示例代码与考试题库。

## 语言选型指南

| 目标 | 推荐语言 | 入口 |
|------|----------|------|
| 理解底层、备考期末 | C | [c/](c/) |
| 快速上手、数据分析 | Python | 计划中 |
| Web 全栈 | JavaScript | 计划中 |
| 企业后端 | Java | 计划中 |
| 云原生 / 基础设施 | Go | 计划中 |

**建议路径**：C 语言打基础 → 任选一门高级语言深入 → 按岗位补专项语言。

## 已发布语言

| 语言 | 教程 | 速查 | 示例 | 考试 |
|------|------|------|------|------|
| C | [guides](c/guides/) | [references](c/references/) | [examples](c/examples/) | [exams](c/exams/) |

## 新增语言

复制 [\_template/](_template/) 目录，重命名为语言 slug 后开始编写。详见 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 目录结构（每种语言）

```
languages/<lang>/
├── README.md
├── syllabus.md
├── guides/
├── references/
├── exercises/
├── examples/
└── exams/          # 可选
```
