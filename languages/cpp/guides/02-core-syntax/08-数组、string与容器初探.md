
# 数组、string与容器初探

## 从 C 数组到 C++ 容器

在 [C 语言数组与字符串](../../c/guides/02-core-syntax/08-数组与字符串：批量数据处理.md) 中，我们学习了 C 数组和字符数组。C++ 保留 C 数组语法，并提供了 **std::string** 和 **std::vector** 等更安全、易用的容器。

---

## 一、C 风格数组（回顾）

C++ 完全支持 C 数组：

```cpp
int arr[5] = {1, 2, 3, 4, 5};
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};

for (int i = 0; i < 5; i++)
    std::cout << arr[i] << " ";
```

> 数组定义、遍历、作为参数传递详见 [C 第 08 篇](../../c/guides/02-core-syntax/08-数组与字符串：批量数据处理.md)。

**C++11 列表初始化：**

```cpp
int arr[]{1, 2, 3};  // 自动推断大小
```

---

## 二、std::string

### 2.1 基本用法

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s1 = "Hello";
    std::string s2("World");
    std::string s3 = s1 + ", " + s2 + "!";

    std::cout << s3 << std::endl;
    std::cout << "长度：" << s3.length() << std::endl;

    // 输入
    std::string name;
    std::cout << "请输入姓名：";
    std::cin >> name;
    std::cout << "你好，" << name << std::endl;

    return 0;
}
```

### 2.2 常用操作

| 操作 | 方法/语法 | 示例 |
|------|-----------|------|
| 长度 | `size()` / `length()` | `s.size()` |
| 拼接 | `+` 或 `+=` | `s += "!"` |
| 访问 | `[i]` 或 `at(i)` | `s[0]`（at 有边界检查） |
| 子串 | `substr(pos, len)` | `s.substr(0, 5)` |
| 查找 | `find(str)` | `s.find("lo")` |
| 比较 | `==` `!=` `<` `>` | `s1 == s2` |

### 2.3 与 C 字符串对比

| 特性 | C `char[]` | C++ `std::string` |
|------|------------|-------------------|
| 长度 | 需手动管理 | 自动 |
| 拼接 | `strcat` | `+` / `+=` |
| 内存 | 固定或动态 | 自动扩展 |
| 安全性 | 易越界 | `at()` 可检查 |

---

## 三、std::vector

### 3.1 基本用法

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    vec.push_back(6);       // 尾部添加
    vec.pop_back();         // 删除尾部

    std::cout << "大小：" << vec.size() << std::endl;
    std::cout << "第一个：" << vec.front() << std::endl;
    std::cout << "最后一个：" << vec.back() << std::endl;

    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    return 0;
}
```

### 3.2 常用操作

| 操作 | 方法 | 说明 |
|------|------|------|
| 添加 | `push_back(x)` | 尾部添加 |
| 删除 | `pop_back()` | 删除尾部 |
| 大小 | `size()` | 元素个数 |
| 清空 | `clear()` | 删除所有元素 |
| 访问 | `[i]` / `at(i)` | 下标访问 |
| 空判断 | `empty()` | 是否为空 |

### 3.3 vector 与数组

| 特性 | C 数组 | vector |
|------|--------|--------|
| 大小 | 编译期固定 | 运行期可变 |
| 内存 | 栈或手动分配 | 自动管理 |
| 传递 | 退化为指针 | 可按值/引用传递 |

---

## 四、std::array（C++11，可选）

固定大小数组的 C++ 封装：

```cpp
#include <array>
std::array<int, 5> arr = {1, 2, 3, 4, 5};
std::cout << arr.size() << std::endl;  // 5
```

---

## 五、实战练习

### 练习1：string 操作

读入一行字符串（用 `getline`），统计单词数或反转字符串。

```cpp
#include <iostream>
#include <string>
std::getline(std::cin, line);  // 读取含空格的整行
```

### 练习2：vector 动态添加

循环读入整数直到输入 0，存入 vector 并输出所有元素。

### 练习3：找最大值

用 vector 存储 n 个整数，找出最大值及其下标。

---

## 六、总结与延伸

### 本节重点回顾

1. C 数组在 C++ 中仍可用；推荐用 **std::string** 和 **std::vector**
2. **string**：自动管理长度，`+` 拼接，`size()` 求长
3. **vector**：动态数组，`push_back`/`pop_back`，范围 for 遍历
4. 大容器遍历时用 `const auto&` 避免拷贝

### 下节预告

下一篇：《函数：重载、默认参数与内联》。

### 延伸阅读

- [C 语言数组与字符串](../../c/guides/02-core-syntax/08-数组与字符串：批量数据处理.md)
- [C++ 速查 §7 数组与 string](../../references/C++常用语法汇总.md#7-数组与-string)

---

📌 **知识点卡片**
- std::string：#include <string>；+ 拼接；size() 长度
- std::vector：#include <vector>；push_back；范围 for 遍历
- getline 读整行；at() 有边界检查

---

> 下一篇见！
