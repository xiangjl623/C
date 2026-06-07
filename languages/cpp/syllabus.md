### 专栏定位

- **目标读者**：已掌握 C 语言基础的学习者、希望学习面向对象与 STL 的开发者
- **核心价值**：在 C 语言基础上系统掌握现代 C++，理解 OOP、RAII 与标准库

> 本课程位于 monorepo 的 [languages/cpp/](README.md) 目录。教程见 `guides/`，速查见 `references/`，示例见 `examples/`。

## 文章主题规划（共 15 篇）

### 第一部分：入门基础（4 篇）

| 序号 | 主题 | 目录 | 核心内容 |
|------|------|------|----------|
| 1 | C++入门：从C到现代C++ | guides/01-getting-started/ | C++ 历史、与 C 关系、适用场景 |
| 2 | 开发环境搭建 | guides/01-getting-started/ | g++/clang++、CMake 简介、VS Code C++ 插件 |
| 3 | 程序结构 | guides/01-getting-started/ | 头文件、namespace、编译链接；链接 C 第 03 篇 |
| 4 | 数据类型、引用与auto | guides/01-getting-started/ | 基本类型、引用 vs 指针、auto、iostream |

### 第二部分：核心语法（5 篇）

| 序号 | 主题 | 目录 | 核心内容 |
|------|------|------|----------|
| 5 | 运算符与表达式 | guides/02-core-syntax/ | C 运算符 + bool、new/delete 初识 |
| 6 | 流程控制 | guides/02-core-syntax/ | 与 C 相同语法；C++ 差异标注；链接 C 第 06 篇 |
| 7 | 循环结构 | guides/02-core-syntax/ | 传统循环 + 范围 for（C++11） |
| 8 | 数组、string与容器初探 | guides/02-core-syntax/ | C 数组 + std::string + std::vector |
| 9 | 函数 | guides/02-core-syntax/ | 重载、默认参数、inline、函数模板初探 |

### 第三部分：进阶概念（3 篇）

| 序号 | 主题 | 目录 | 核心内容 |
|------|------|------|----------|
| 10 | 类与对象 | guides/03-advanced/ | class、构造/析构、封装、访问控制 |
| 11 | 继承、多态与虚函数 | guides/03-advanced/ | 继承、override、virtual、纯虚函数 |
| 12 | 模板与STL基础 | guides/03-advanced/ | 函数/类模板、vector/map/algorithm |

### 第四部分：实战与应用（3 篇）

| 序号 | 主题 | 目录 | 核心内容 |
|------|------|------|----------|
| 13 | 智能指针与RAII | guides/04-projects/ | unique_ptr/shared_ptr；链接 C 内存管理 |
| 14 | 综合实战：学生管理系统 | guides/04-projects/ | OOP 项目 + STL + 文件 I/O |
| 15 | 学习路线与资源推荐 | guides/04-projects/ | 现代 C++ 方向、cppreference |

## 格式规范

详见仓库 [CONTRIBUTING.md](../../CONTRIBUTING.md)。

## 专栏特色

1. **C 基础复用**：重叠内容链接 C 教程，聚焦 C++ 增量特性
2. **现代 C++ 导向**：以 C++11/14/17 常用特性为主
3. **原理 + 实战**：每篇包含底层原理与可运行 `.cpp` 示例
4. **互动性**：每篇结尾设置练习题

## 发布节奏

| 阶段 | 内容 | 状态 |
|------|------|------|
| 第一阶段 | 入门基础（01～04）+ 速查前 4 主题 + 示例 chapter01～04 | 已完成 |
| 第二阶段 | 核心语法～实战（05～15）+ 完整速查 + 示例 chapter05～15 | 已完成 |
| 第三阶段 | 考试题库 + certifications 专题 | 已完成 |
