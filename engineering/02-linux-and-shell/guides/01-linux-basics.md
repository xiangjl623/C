# Linux 基础命令

> **难度**：入门 | **阅读时间**：约 20 分钟 | **前置**：无 | **标签**：`linux` `shell` `cli`

## 学习目标

- [ ] 能在终端完成目录导航与文件基本操作
- [ ] 理解 Linux 权限模型（rwx、chmod）
- [ ] 会使用 gcc 编译 C 程序、ps/top 查看进程

## 文件与目录

```bash
pwd                    # 当前目录
ls -la                 # 列出文件（含隐藏、详情）
cd /path/to/dir        # 切换目录
mkdir -p proj/src      # 创建目录（含父级）
cp a.c b.c             # 复制
mv old new             # 移动/重命名
rm file                # 删除文件（谨慎）
rm -r dir              # 递归删除目录
cat file.txt           # 输出内容
less file.txt          # 分页查看
head -n 20 file        # 前 20 行
tail -f log.txt        # 跟踪日志
```

## 路径

- `/` 根目录
- `~` 当前用户家目录
- `.` 当前目录，`..` 上级
- 绝对路径从 `/` 开始；相对路径从当前目录开始

## 权限

```bash
ls -l
# -rw-r--r-- 1 user group 1234 Jun  7 10:00 hello.c
# 类型 所有者 组 其他
chmod 755 script.sh    # rwxr-xr-x
chmod u+x file         # 给所有者加执行
```

| 符号 | 含义 |
|------|------|
| r | 读 4 |
| w | 写 2 |
| x | 执行 1 |

## 编译 C 程序

```bash
gcc -Wall -o hello hello.c    # 编译
./hello                       # 运行
gcc -g hello.c -o hello       # 带调试信息
```

## 进程

```bash
ps aux | grep hello      # 查找进程
kill <pid>               # 终止进程
top                      # 动态查看资源
```

## Windows 用户

可使用 **WSL2**（Windows Subsystem for Linux）获得接近生产环境的 Linux 体验。

## 本节小结

- 命令行是服务器与 CI 环境的标准界面
- 权限与路径是常见踩坑点
- C 语言学习建议至少在 Linux 或 WSL 下用 gcc 编译一次

## 练习

1. 创建目录 `lab/c`，写入 hello.c，gcc 编译运行
2. 用 `chmod` 使脚本不可被组用户写入

## 延伸阅读

- [Shell 脚本入门](02-shell-scripting-intro.md)
- [命令速查](../references/shell-commands-cheatsheet.md)
- [C 语言环境搭建](../../languages/c/guides/01-getting-started/02-C语言开发环境搭建：从安装到Hello World.md)
- [C++ 环境搭建](../../languages/cpp/guides/01-getting-started/02-C++开发环境搭建：从安装到Hello World.md)（g++ 编译：`g++ -std=c++17 -Wall hello.cpp -o hello`）
