# Shell 命令速查

## 文件

| 命令 | 说明 |
|------|------|
| `ls -la` | 列表 |
| `cd`, `pwd` | 切换/显示目录 |
| `mkdir -p` | 建目录 |
| `cp -r` | 复制 |
| `mv` | 移动/重命名 |
| `rm -rf` | 删除（危险） |
| `find . -name "*.c"` | 查找文件 |

## 文本

| 命令 | 说明 |
|------|------|
| `cat`, `less` | 查看 |
| `grep pattern file` | 搜索 |
| `grep -r pattern dir` | 递归搜索 |
| `wc -l file` | 行数 |
| `sort`, `uniq` | 排序去重 |

## 权限与进程

| 命令 | 说明 |
|------|------|
| `chmod +x f` | 加执行 |
| `ps aux`, `top` | 进程 |
| `kill PID` | 杀进程 |

## 网络（常用）

| 命令 | 说明 |
|------|------|
| `curl -I url` | HTTP 头 |
| `ping host` | 连通性 |
| `ssh user@host` | 远程登录 |

## 重定向

```bash
cmd > out.txt       # stdout 重定向
cmd 2> err.txt      # stderr
cmd >> log.txt      # 追加
cmd1 | cmd2         # 管道
```

## 教程

- [Linux 基础](../guides/01-linux-basics.md)
- [Shell 脚本](../guides/02-shell-scripting-intro.md)
