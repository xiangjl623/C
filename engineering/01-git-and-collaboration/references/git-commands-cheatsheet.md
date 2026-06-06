# Git 命令速查

## 配置（一次性）

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 日常

| 命令 | 说明 |
|------|------|
| `git status` | 工作区状态 |
| `git diff` | 未暂存差异 |
| `git diff --staged` | 已暂存差异 |
| `git add <file>` | 暂存 |
| `git commit -m "msg"` | 提交 |
| `git log --oneline -10` | 最近 10 条提交 |

## 分支

| 命令 | 说明 |
|------|------|
| `git branch` | 列出分支 |
| `git switch <name>` | 切换分支 |
| `git switch -c <name>` | 新建并切换 |
| `git merge <branch>` | 合并 |
| `git branch -d <name>` | 删除分支 |

## 远程

| 命令 | 说明 |
|------|------|
| `git clone <url>` | 克隆 |
| `git remote -v` | 查看远程 |
| `git fetch` | 拉取不合并 |
| `git pull` | fetch + merge |
| `git push -u origin <branch>` | 首次推送分支 |

## 撤销（谨慎）

| 命令 | 说明 |
|------|------|
| `git restore <file>` | 丢弃工作区修改 |
| `git restore --staged <file>` | 取消暂存 |
| `git reset --soft HEAD~1` | 撤销最后一次 commit，保留改动 |

## 教程

- [Git 基础](../guides/01-git-basics.md)
- [分支与 PR](../guides/02-branching-and-pr.md)
