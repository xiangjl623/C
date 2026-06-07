
# 数据类型、引用与auto

## C++ 在 C 类型系统上的扩展

在 [C 语言数据类型与变量](../../c/guides/01-getting-started/04-数据类型与变量：编程的基本积木.md) 中，我们学习了 `int`、`float`、`char` 等基本类型。C++ 完全保留了这些类型，并在此基础上增加了 **bool**、**引用**、**auto** 等重要特性，同时提供了类型安全的 **iostream** 输入输出。

本篇聚焦 C++ 相对 C 的类型与 I/O 扩展；整型、浮点、字符等基础内容请参阅 C 教程。

---

## 一、C++ 基本数据类型（回顾与扩展）

### 1.1 与 C 兼容的基本类型

C++ 支持 C 的所有基本类型：`char`、`short`、`int`、`long`、`float`、`double` 等。用法与 C 相同。

> 详细说明见 [C 语言数据类型与变量](../../c/guides/01-getting-started/04-数据类型与变量：编程的基本积木.md)。

### 1.2 C++ 特有：bool 类型

C++ 内置布尔类型 `bool`，取值为 `true` 或 `false`：

```cpp
#include <iostream>

int main() {
    bool isReady = true;
    bool isEmpty = false;

    std::cout << std::boolalpha;  // 输出 true/false 而非 1/0
    std::cout << "isReady: " << isReady << std::endl;
    std::cout << "isEmpty: " << isEmpty << std::endl;

    int score = 85;
    bool passed = (score >= 60);
    std::cout << "passed: " << passed << std::endl;

    return 0;
}
```

| 对比 | C | C++ |
|------|---|-----|
| 布尔类型 | 无（用 int 0/1 模拟） | `bool`，`true`/`false` |
| 条件判断 | 非零为真 | 同左，但 bool 语义更清晰 |

---

## 二、引用（Reference）

### 2.1 什么是引用

引用是变量的别名——定义时必须初始化，且之后不能绑定到其他对象：

```cpp
#include <iostream>

int main() {
    int original = 42;
    int& ref = original;  // ref 是 original 的别名

    ref = 100;
    std::cout << "original: " << original << std::endl;  // 100
    std::cout << "ref: " << ref << std::endl;              // 100

    return 0;
}
```

### 2.2 引用 vs 指针

| 特性 | 引用 `int&` | 指针 `int*` |
|------|-------------|-------------|
| 初始化 | 必须初始化 | 可为空（NULL/nullptr） |
| 重新绑定 | 不能 | 可以指向其他对象 |
| 解引用 | 直接使用，无需 `*` | 需要 `*` 解引用 |
| 空值 | 不存在空引用 | 可以 nullptr |
| 主要用途 | 函数参数、返回值 | 动态内存、可选值 |

```cpp
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 1, y = 2;
    swap(x, y);  // 直接修改 x、y，无需传地址
    std::cout << x << ", " << y << std::endl;  // 2, 1
    return 0;
}
```

> 指针的完整讲解见 [C 语言指针](../../c/guides/03-advanced/10-指针：C语言的灵魂.md)。C++ 中优先用引用传递非空对象，用指针表示可选或动态内存。

### 2.3 const 引用

不能通过 const 引用修改原对象，常用于函数参数以避免拷贝：

```cpp
void print(const std::string& s) {
    std::cout << s << std::endl;
    // s = "other";  // 错误：不能修改
}
```

---

## 三、auto 与类型推导（C++11）

### 3.1 auto 关键字

编译器根据初始化表达式自动推导类型：

```cpp
#include <iostream>
#include <vector>

int main() {
    auto i = 42;           // int
    auto d = 3.14;         // double
    auto s = std::string("hello");  // std::string

    std::vector<int> vec = {1, 2, 3};
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

### 3.2 使用建议

| 场景 | 是否推荐 auto |
|------|---------------|
| 迭代器、复杂模板类型 | 推荐 |
| 简单整型、浮点 | 可选，显式类型更清晰 |
| 函数返回值 | 谨慎，需确保可读性 |

### 3.3 decltype

获取表达式的类型，常用于模板元编程：

```cpp
int x = 0;
decltype(x) y = 10;  // y 的类型与 x 相同，为 int
```

---

## 四、const 与 constexpr

### 4.1 const

与 C 类似，表示只读：

```cpp
const int MAX_SIZE = 100;
const double PI = 3.14159;
```

### 4.2 constexpr（C++11）

编译期常量，值在编译时确定：

```cpp
constexpr int BUFFER_SIZE = 256;
constexpr int square(int n) { return n * n; }

int main() {
    int arr[square(5)];  // 数组大小为 25，编译期确定
    return 0;
}
```

---

## 五、iostream 输入输出

### 5.1 标准输出 cout

```cpp
#include <iostream>

int main() {
    int age = 25;
    double height = 1.75;

    std::cout << "年龄：" << age << std::endl;
    std::cout << "身高：" << height << " 米" << std::endl;

    return 0;
}
```

**与 printf 对比：**

| 特性 | printf | cout |
|------|--------|------|
| 类型安全 | 需手动匹配格式符 | 编译期检查 |
| 语法 | `printf("%d", x)` | `cout << x` |
| 扩展性 | 固定 | 可重载 `<<` |

### 5.2 标准输入 cin

```cpp
#include <iostream>

int main() {
    int a, b;
    std::cout << "请输入两个整数：";
    std::cin >> a >> b;
    std::cout << "和为：" << a + b << std::endl;
    return 0;
}
```

> C 的 `scanf`/`printf` 在 C++ 中仍可用（`#include <cstdio>`），但推荐优先使用 iostream。

### 5.3 常用操纵符

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.14159265;
    std::cout << std::fixed << std::setprecision(2) << pi << std::endl;  // 3.14
    std::cout << std::boolalpha << true << std::endl;  // true
    return 0;
}
```

---

## 六、类型大小与 sizeof

与 C 相同，`sizeof` 返回类型或变量占用的字节数：

```cpp
#include <iostream>

int main() {
    std::cout << "sizeof(int): " << sizeof(int) << std::endl;
    std::cout << "sizeof(bool): " << sizeof(bool) << std::endl;
    std::cout << "sizeof(double): " << sizeof(double) << std::endl;
    return 0;
}
```

---

## 七、实战练习

### 练习1：引用交换

编写 `void swap(int& a, int& b)`，在 main 中验证交换效果。

### 练习2：auto 推导

声明多个 `auto` 变量，用 `typeid` 或编译器推断确认其类型：

```cpp
#include <typeinfo>
#include <iostream>

int main() {
    auto x = 10;
    auto y = 3.14;
    std::cout << typeid(x).name() << std::endl;
    std::cout << typeid(y).name() << std::endl;
    return 0;
}
```

### 练习3：iostream 计算器

用 `cin`/`cout` 实现两数加减乘除，对比 C 版 `scanf`/`printf` 的实现。

---

## 八、总结与延伸

### 本节重点回顾

1. C++ 保留 C 基本类型，新增 **bool** 类型
2. **引用**是别名，必须初始化，常用于函数参数避免拷贝
3. **auto** 让编译器推导类型，简化复杂类型声明
4. **iostream**（cout/cin）提供类型安全的 I/O，推荐替代 printf/scanf
5. **constexpr** 用于编译期常量与函数

### 下节预告

下一篇将进入核心语法阶段：《运算符与表达式：C++ 扩展特性》，学习 new/delete 等 C++ 运算符。

### 延伸阅读

- [C 语言数据类型与变量](../../c/guides/01-getting-started/04-数据类型与变量：编程的基本积木.md)
- [C 语言指针](../../c/guides/03-advanced/10-指针：C语言的灵魂.md)
- [C++ 速查：数据类型与引用](../../references/C++常用语法汇总.md#2-数据类型与常量)

---

📌 **知识点卡片**
- bool：`true`/`false`；引用 `T&` 必须初始化，是别名
- auto：编译期类型推导；const 引用 `const T&` 用于只读参数
- 输出：`std::cout << x << std::endl`；输入：`std::cin >> x`
- C 基础类型用法见 C 教程；C++ 增量重点在引用、bool、iostream

💡 **小技巧**
- 函数参数中，大对象用 `const T&` 传递，避免拷贝
- 简单循环变量可写 `for (auto i = 0; i < n; ++i)`

⚠️ **注意事项**
- 引用必须初始化，不能为空
- 不要返回局部变量的引用或指针（悬垂引用）
- 混用 cout 与 printf 时注意缓冲区刷新

---

> 如果你对数据类型与引用有疑问，欢迎在评论区留言！下一篇见！
