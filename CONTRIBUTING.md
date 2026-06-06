# 贡献指南

感谢你愿意改进 Dev Handbook。本仓库定位为**公开教程体系**，贡献时请保持内容准确、结构一致、链接有效。

## 如何贡献

1. Fork 本仓库，从 `main` 创建功能分支（如 `add/python-basics`）
2. 按 [docs/style-guide.md](docs/style-guide.md) 编写或修改内容
3. 确保相对链接正确，代码示例可运行
4. 提交 Pull Request，说明改动范围与动机

## 内容类型

| 类型 | 目录 | 说明 |
|------|------|------|
| 系统教程 | `*/guides/` | 完整章节，遵循 [article-template.md](docs/article-template.md) |
| 速查参考 | `*/references/` | 表格、清单、对比，篇幅精炼 |
| 练习题库 | `*/exercises/`、`*/exams/` | 题目与参考答案分文件存放 |
| 代码示例 | `*/examples/` | 可独立编译运行 |

## 新增语言教程

复制 [languages/_template/](languages/_template/) 到新语言目录（如 `languages/python/`），填写 `syllabus.md` 与 `README.md` 后开始写作。

## 新增考试专题

在 `certifications/university/` 或 `certifications/industry/` 下建目录，使用 [certifications/_shared/exam-template.md](certifications/_shared/exam-template.md) 作为起点。

## Pull Request 检查清单

- [ ] 新增或修改的目录包含 `README.md` 入口
- [ ] 教程文末含「本节小结 / 练习 / 延伸阅读」
- [ ] 无敏感信息（密钥、公司内部数据、个人隐私）
- [ ] 文件名使用英文 slug，正文中文

## Issue 类型

- **内容纠错**：指出事实错误或代码 bug
- **内容建议**：提议新章节或改进学习路径
- **结构讨论**：目录组织、命名规范相关
