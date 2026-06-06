# 分支与 Pull Request

> **难度**：入门 | **阅读时间**：约 18 分钟 | **前置**：[Git 基础](01-git-basics.md) | **标签**：`git` `branch` `pr`

## 学习目标

- [ ] 理解分支用于隔离功能开发与并行实验
- [ ] 能完成 branch → commit → push → PR 协作流程
- [ ] 了解 merge 与 rebase 的基本区别（团队规范优先）

## 为什么需要分支

在 `main` 上直接改代码风险高。功能分支允许：

- 不影响稳定主线
- 多人并行开发
- Code Review 后再合并

## 分支命令

```bash
git branch feature/add-exercises    # 创建分支
git checkout feature/add-exercises  # 切换分支
git switch -c feature/add-exercises # 创建并切换（新语法）
git merge feature/add-exercises     # 合并到当前分支
git branch -d feature/add-exercises # 删除已合并分支
```

## Pull Request 流程

1. Fork 或从 `main` 切出功能分支
2. 提交改动并 push 到远程分支
3. 在 GitHub 创建 Pull Request
4. 维护者 Review，讨论修改
5. 合并后删除功能分支

本仓库流程见 [CONTRIBUTING.md](../../CONTRIBUTING.md)。

## 解决冲突

当两人修改同一处时，merge 会产生冲突标记：

```
<<<<<<< HEAD
your change
=======
their change
>>>>>>> branch
```

手动编辑保留正确内容，再 `git add` 与 `git commit`。

## merge vs rebase（简述）

| 方式 | 特点 |
|------|------|
| merge | 保留分支历史，产生 merge commit |
| rebase | 线性历史，改写 commit；**不要** rebase 已 push 的公共分支 |

团队有规范时遵循团队规范。

## 本节小结

- 功能开发用分支，合并前走 PR + Review
- 小步提交、清晰描述，降低冲突概率
- 贡献本知识库：改文档 → 分支 → PR

## 练习

1. 创建分支 `docs/fix-typo`，修改 README 一处笔误（或加注释），提交 PR 流程（本地模拟即可）
2. 故意制造简单冲突并练习解决

## 延伸阅读

- [Git 基础](01-git-basics.md)
- [05-ci-cd/](../05-ci-cd/)（计划中）— PR 触发 CI
