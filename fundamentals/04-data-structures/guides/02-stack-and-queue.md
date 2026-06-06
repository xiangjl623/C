# 栈与队列

> **难度**：入门 | **阅读时间**：约 15 分钟 | **前置**：[数组与链表](01-arrays-and-linked-lists.md) | **标签**：`stack` `queue`

## 学习目标

- [ ] 理解栈 LIFO 与队列 FIFO 的语义
- [ ] 知道数组实现栈/队列时的环形队列思想
- [ ] 识别表达式求值、BFS 等典型应用场景

## 栈（Stack）— 后进先出

只允许在一端（栈顶）进行 push / pop：

```
push(3) push(2) push(1)  →  栈顶: 1
pop() → 1, pop() → 2
```

**典型应用**：

- 函数调用栈（递归）
- 括号匹配、表达式求值
- 浏览器后退、撤销操作

数组实现示例（栈顶指针 `top`）：

```c
#define MAX 100
int stack[MAX];
int top = -1;

void push(int x) { stack[++top] = x; }
int pop(void) { return stack[top--]; }
```

## 队列（Queue）— 先进先出

一端入队（rear），另一端出队（front）：

**典型应用**：

- 任务调度、消息队列
- BFS 广度优先搜索
- 打印队列

## 复杂度

| 结构 | push/enqueue | pop/dequeue | 查栈顶/队头 |
|------|--------------|-------------|-------------|
| 数组栈 | O(1) | O(1) | O(1) |
| 链表栈 | O(1) | O(1) | O(1) |
| 数组队列 | O(1)* | O(1)* | O(1) |

*普通数组实现 dequeue 可能 O(n)；环形队列可均摊 O(1)。

## 本节小结

- 栈 = LIFO，队列 = FIFO
- 二者都可用数组或链表实现
- 识别场景比死记实现更重要

## 练习

1. 用栈检查括号 `()[]{}` 是否匹配
2. 用队列模拟 Josephus 环问题（n 人报数出列）

## 延伸阅读

- [树与图入门](03-trees-and-graphs-intro.md) — BFS 使用队列
- [C 语言函数与递归](../../languages/c/references/05-函数.md)
