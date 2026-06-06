# Shell 脚本入门

> **难度**：入门 | **阅读时间**：约 18 分钟 | **前置**：[Linux 基础命令](01-linux-basics.md) | **标签**：`bash` `shell`

## 学习目标

- [ ] 能编写含变量、条件、循环的 bash 脚本
- [ ] 理解 `$1` 位置参数与 `$?` 退出码
- [ ] 会用脚本批量编译或运行测试

## Shebang 与执行

```bash
#!/usr/bin/env bash
echo "Hello, Shell"
```

```bash
chmod +x run.sh
./run.sh
# 或
bash run.sh
```

## 变量

```bash
name="Dev Handbook"
count=3
echo "$name has $count pillars"
```

注意：赋值等号两侧**不能有空格**。

## 条件

```bash
if [ -f hello.c ]; then
    gcc -Wall hello.c -o hello && ./hello
else
    echo "hello.c not found"
fi
```

常用测试：

| 测试 | 含义 |
|------|------|
| `-f file` | 是普通文件 |
| `-d dir` | 是目录 |
| `-z "$s"` | 字符串为空 |
| `"$a" -eq "$b"` | 整数相等 |

## 循环

```bash
for f in *.c; do
    gcc -Wall "$f" -o "${f%.c}" && echo "built $f"
done
```

```bash
i=0
while [ "$i" -lt 5 ]; do
    echo "$i"
    i=$((i + 1))
done
```

## 函数

```bash
build() {
    gcc -Wall "$1" -o "${1%.c}" || return 1
}
build hello.c
```

## 退出码

命令成功通常为 `0`，失败非零。脚本中用 `&&` / `||` 串联：

```bash
gcc hello.c -o hello && ./hello || echo "build failed"
echo $?   # 上一条命令的退出码
```

## 本节小结

- Shell 适合胶水任务：批量编译、部署、日志处理
- 引用变量用双引号 `"$var"` 防止空格分词
- 复杂逻辑优先考虑 Python 等语言；简单自动化用 bash 足够

## 练习

1. 写脚本：遍历当前目录所有 `.c` 文件并编译
2. 写脚本：接受文件名参数，存在则 cat，否则报错退出码 1

## 延伸阅读

- [Linux 基础命令](01-linux-basics.md)
- [命令速查](../references/shell-commands-cheatsheet.md)
