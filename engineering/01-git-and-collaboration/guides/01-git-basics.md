# Git 基础

> **难度**：入门 | **阅读时间**：约 20 分钟 | **前置**：无 | **标签**：`git` `version-control`

## 学习目标

- [ ] 理解 Git 跟踪的是「快照」而非单纯文件差异
- [ ] 能完成 init → add → commit → log 基本流程
- [ ] 会使用 remote、clone、pull、push 与 GitHub 同步

## 核心概念

| 概念 | 说明 |
|------|------|
| 仓库 (repository) | 项目历史与文件的集合 |
| 工作区 | 当前编辑的文件 |
| 暂存区 (staging) | `git add` 后待提交的内容 |
| 提交 (commit) | 一次快照，含作者、时间、说明 |

```
工作区 --git add--> 暂存区 --git commit--> 本地仓库 --git push--> 远程
```

## 常用命令

```bash
git init                          # 初始化仓库
git status                        # 查看状态
git add file.c                    # 暂存文件
git add .                         # 暂存所有变更
git commit -m "feat: add hello"   # 提交
git log --oneline                 # 查看历史
git clone <url>                   # 克隆远程仓库
git pull                          # 拉取并合并
git push                          # 推送到远程
```

## 提交信息建议

使用简洁说明，推荐格式：

```
<type>: <summary>

feat: 添加链表练习
fix: 修正 scanf 格式符
docs: 更新 README 导航
```

## .gitignore

忽略不应入库的文件：

```
*.o
*.exe
.env
__pycache__/
```

## 本节小结

- Git 是本地优先；远程（GitHub）用于备份与协作
- 提交粒度宜小、信息宜清晰
- 本仓库 [CONTRIBUTING.md](../../CONTRIBUTING.md) 描述了 PR 协作流程

## 练习

1. 在本地创建仓库，提交 [languages/c/examples/](../../languages/c/examples/) 中一个 `.c` 文件
2. 创建 GitHub 仓库并 push，查看 commit 历史

## 延伸阅读

- [分支与 Pull Request](02-branching-and-pr.md)
- [Git 命令速查](../references/git-commands-cheatsheet.md)
- [Pro Git 官方书（中文）](https://git-scm.com/book/zh/v2)
