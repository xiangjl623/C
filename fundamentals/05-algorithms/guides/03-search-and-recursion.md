# 查找与递归

> **难度**：入门 | **阅读时间**：约 18 分钟 | **前置**：[排序算法](02-sorting-algorithms.md) | **标签**：`search` `recursion` `binary-search`

## 学习目标

- [ ] 区分线性查找与二分查找及前提条件
- [ ] 理解递归的两要素：基准情况 + 递归关系
- [ ] 能实现递归求阶乘、斐波那契（并知斐波那契朴素递归的重复计算问题）

## 线性查找

逐个比较，无序数组可用。时间 O(n)，空间 O(1)。

## 二分查找

**前提**：有序数组。每次排除一半区间。

```c
int binary_search(const int a[], int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

时间 O(log n)，空间 O(1)（迭代版）。

## 递归

函数直接或间接调用自身。

**阶乘**：

```c
long factorial(int n) {
    if (n <= 1) return 1;      /* 基准情况 */
    return n * factorial(n - 1);
}
```

**斐波那契**（朴素递归，效率低）：

```c
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);  /* O(2^n) */
}
```

考试常要求画递归调用树或改写成循环。

## 本节小结

- 二分查找必须有序；注意 mid 溢出写法 `lo + (hi-lo)/2`
- 递归必有终止条件，否则栈溢出
- C 语言期末：递归、二分、嵌套循环是程序阅读题重点

## 练习

1. 在有序数组 `{1,3,5,7,9}` 中二分查找 7，写出每步 lo/hi/mid
2. 用循环实现 factorial，对比递归版

## 延伸阅读

- [C 语言函数与递归](../../languages/c/references/05-函数.md)
- [栈与队列](../04-data-structures/guides/02-stack-and-queue.md) — 递归调用栈
