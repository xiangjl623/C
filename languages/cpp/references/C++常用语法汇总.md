# 1 程序基础

## 1.1 最小程序结构

```cpp
#include <iostream>          // C++ 标准 I/O 头文件

int main() {                 // 主函数，程序入口（必须返回 int）
    std::cout << "Hello, C++!\n";
    return 0;                // 返回 0 表示正常结束
}
```

## 1.2 编译与运行流程

| 阶段 | 说明 | 常见产物 |
|------|------|----------|
| 预处理 | 处理 `#` 指令（include、define 等） | `.i` 文件 |
| 编译 | 将 C++ 代码翻译为汇编 | `.s` 文件 |
| 汇编 | 汇编代码转为机器码 | `.o` / `.obj` 目标文件 |
| 链接 | 合并目标文件与库，生成可执行文件 | `.exe` / 无后缀可执行文件 |

**常见命令（g++）：**

| 命令 | 作用 |
|------|------|
| `g++ -std=c++17 hello.cpp -o hello` | 编译并指定输出名 |
| `g++ -std=c++17 -Wall hello.cpp -o hello` | 开启常见警告 |
| `g++ -std=c++17 -c hello.cpp` | 只编译不链接，生成 `.o` |
| `g++ main.cpp utils.cpp -o app` | 多文件编译链接 |
| `./hello` | 运行（Linux/macOS/WSL） |
| `hello.exe` | 运行（Windows） |

## 1.3 源文件与头文件

| 类型 | 扩展名 | 作用 |
|------|--------|------|
| 源文件 | `.cpp` / `.cc` / `.cxx` | 存放函数与类实现 |
| 头文件 | `.h` / `.hpp` / `.hxx` | 存放声明、类定义 |

**头文件保护：**

```cpp
#pragma once
// 或
#ifndef MY_HEADER_H
#define MY_HEADER_H
// ...
#endif
```

## 1.4 C 与 C++ 头文件对照

| C 风格 | C++ 推荐 | 说明 |
|--------|----------|------|
| `#include <stdio.h>` | `#include <cstdio>` | 符号在 `std` 命名空间 |
| `#include <stdlib.h>` | `#include <cstdlib>` | 同上 |
| `#include <string.h>` | `#include <cstring>` | 同上 |
| — | `#include <iostream>` | C++ 专用 I/O |
| — | `#include <string>` | C++ 字符串类 |

## 1.5 命名空间

| 语法 | 说明 | 示例 |
|------|------|------|
| 定义 | `namespace Name { ... }` | `namespace Math { int add(...); }` |
| 访问 | 作用域解析 `::` | `Math::add(1, 2)` |
| using 声明 | 引入单个名称 | `using std::cout;` |
| using 指令 | 引入整个命名空间 | `using namespace std;`（头文件中避免） |
| 匿名命名空间 | 文件内可见 | `namespace { int helper(); }` |

**std 命名空间：** C++ 标准库所有内容均在 `std` 中，如 `std::cout`、`std::string`。

## 1.6 注释写法

| 方式 | 语法 | 说明 |
|------|------|------|
| 单行 | `// 注释` | C++ 原生支持 |
| 多行 | `/* 注释 */` | 与 C 相同，不能嵌套 |

## 1.7 标识符与关键字

命名规则与 C 相同：字母或 `_` 开头，后续可为字母、数字、`_`；区分大小写。

**C++ 额外关键字（相对 C）：**

| 类别 | 关键字 |
|------|--------|
| 面向对象 | `class` `public` `private` `protected` `virtual` `override` |
| 内存 | `new` `delete` `nullptr` |
| 类型 | `bool` `true` `false` `auto` `constexpr` `decltype` |
| 模板 | `template` `typename` |
| 异常 | `try` `catch` `throw` |
| 命名空间 | `namespace` `using` |

## 1.8 C++ 主要特点（速记）

| 特点 | 说明 |
|------|------|
| C 的超集 | 兼容绝大部分 C 语法 |
| 多范式 | 面向过程 + 面向对象 + 泛型 |
| 编译型 | 先编译再运行，效率高 |
| RAII | 资源获取即初始化，自动管理资源 |
| 标准库丰富 | STL：容器、算法、迭代器 |
| 类型安全增强 | 引用、bool、强类型检查 |

# 2 数据类型与常量

## 2.1 基本数据类型

C++ 支持 C 的所有基本类型，用法相同。详见 [C 语言速查 §2.1](../../c/references/C语言常用语法汇总.md#21-基本数据类型)。

| 类型 | 含义 | 格式符（printf 风格） | iostream |
|------|------|----------------------|----------|
| `bool` | 布尔 | — | `std::boolalpha` + cout |
| `char` | 字符 | `%c` | 直接 `<<` |
| `int` | 整型 | `%d` | 直接 `<<` |
| `float` | 单精度 | `%f` | 直接 `<<` |
| `double` | 双精度 | `%lf` / `%f` | 直接 `<<` |

## 2.2 bool 类型

```cpp
bool flag = true;
bool ok = false;
if (flag) { /* ... */ }
```

| 值 | 说明 |
|----|------|
| `true` | 真（通常存为 1） |
| `false` | 假（通常存为 0） |

输出：`std::cout << std::boolalpha << flag;` → 输出 `true`/`false`

## 2.3 引用

| 语法 | 说明 | 示例 |
|------|------|------|
| `T& ref = var;` | 引用是别名，必须初始化 | `int& r = x;` |
| `const T& ref = var;` | 常引用，不可修改 | 函数参数常用 |
| 函数参数 | 避免拷贝，可修改原对象 | `void f(int& x)` |

```cpp
void swap(int& a, int& b) {
    int t = a; a = b; b = t;
}
```

## 2.4 auto 与 decltype（C++11）

| 关键字 | 作用 | 示例 |
|--------|------|------|
| `auto` | 由初始化表达式推导类型 | `auto x = 42;` → int |
| `decltype(expr)` | 获取表达式类型 | `decltype(x) y = 0;` |

## 2.5 const 与 constexpr

| 关键字 | 作用 | 示例 |
|--------|------|------|
| `const` | 只读，运行期或编译期 | `const int N = 100;` |
| `constexpr` | 编译期常量（C++11） | `constexpr int N = 256;` |
| `constexpr` 函数 | 编译期可求值 | `constexpr int sq(int n) { return n*n; }` |

## 2.6 变量声明与初始化

| 写法 | 说明 | 示例 |
|------|------|------|
| 拷贝初始化 | 传统写法 | `int x = 10;` |
| 直接初始化 | C++ 风格 | `int x(10);` |
| 列表初始化 | C++11 统一初始化 | `int x{10};` |
| auto | 类型推导 | `auto x = 10;` |

## 2.7 iostream 输入输出

**输出：**

```cpp
#include <iostream>
std::cout << "值：" << x << std::endl;
```

**输入：**

```cpp
std::cin >> x >> y;
```

| 对象 | 作用 |
|------|------|
| `std::cout` | 标准输出 |
| `std::cin` | 标准输入 |
| `std::cerr` | 标准错误（无缓冲） |
| `std::endl` | 换行并刷新缓冲区 |

**常用操纵符（`<iomanip>`）：**

| 操纵符 | 作用 |
|--------|------|
| `std::fixed` | 固定小数点格式 |
| `std::setprecision(n)` | 小数位数 |
| `std::boolalpha` | bool 输出 true/false |
| `std::setw(n)` | 设置字段宽度 |

## 2.8 整型与浮点常量

与 C 相同，参见 [C 语言速查 §2.4～2.6](../../c/references/C语言常用语法汇总.md#24-整型常量写法)。

C++11 列表初始化：`int arr[] = {1, 2, 3};`

# 3 运算符

## 3.1 算术运算符

与 C 相同。详见 [C 语言速查 §3.1](../../c/references/C语言常用语法汇总.md#31-算术运算符)。

| 运算符 | 含义 | 注意 |
|--------|------|------|
| `+` `-` `*` `/` `%` | 加减乘除取模 | 整数除法截断 |

## 3.2 关系与逻辑运算符

与 C 相同。C++ 中关系/逻辑运算结果类型为 `bool`（C 中为 int）。

| 运算符 | 含义 |
|--------|------|
| `>` `<` `>=` `<=` `==` `!=` | 关系运算 |
| `&&` `\|\|` `!` | 逻辑与、或、非 |

## 3.3 赋值与自增自减

与 C 相同：`=`、`+=`、`-=`、`*=`、`/=`、`%=`、`++`、`--`。

## 3.4 C++ 扩展运算符

| 运算符 | 名称 | 示例 | 说明 |
|--------|------|------|------|
| `<<` | 流插入 | `cout << x` | iostream 输出 |
| `>>` | 流提取 | `cin >> x` | iostream 输入 |
| `::` | 作用域解析 | `std::cout` | 命名空间/类成员 |
| `new` | 动态分配 | `int* p = new int(5);` | 堆上分配 |
| `delete` | 动态释放 | `delete p;` | 释放 new 分配的内存 |
| `new[]` / `delete[]` | 数组分配 | `int* a = new int[10];` | 动态数组 |
| `nullptr` | 空指针 | `int* p = nullptr;` | C++11，替代 NULL |

```cpp
int* p = new int(42);
delete p;

int* arr = new int[5]{1, 2, 3, 4, 5};
delete[] arr;
```

> 现代 C++ 推荐用智能指针（`unique_ptr`/`shared_ptr`）替代裸 `new`/`delete`，见后续章节。

## 3.5 位运算符

与 C 相同：`&`、`|`、`^`、`~`、`<<`、`>>`。

## 3.6 运算符优先级

与 C 基本相同。完整优先级表见 [C 语言速查 §3.8](../../c/references/C语言常用语法汇总.md#38-运算符优先级简表)。

# 4 流程控制

## 4.1 if 语句

与 C 完全相同。详见 [C 语言速查 §4.1](../../c/references/C语言常用语法汇总.md#41-if-语句)。

```cpp
if (score >= 90)
    grade = 'A';
else if (score >= 60)
    grade = 'B';
else
    grade = 'F';
```

C++ 差异：条件表达式可结果为 `bool` 类型。

## 4.2 switch 语句

与 C 相同。表达式须为整型或枚举。

```cpp
switch (op) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    default:  std::cout << "无效\n"; break;
}
```

## 4.3 for 循环

**传统 for（与 C 相同）：**

```cpp
for (int i = 0; i < 10; i++)
    std::cout << i << " ";
```

**范围 for（C++11）：**

```cpp
#include <vector>
std::vector<int> vec = {1, 2, 3, 4, 5};
for (auto v : vec)
    std::cout << v << " ";
```

| 形式 | 语法 | 说明 |
|------|------|------|
| 值拷贝 | `for (auto x : container)` | 修改 x 不影响原容器 |
| 引用 | `for (auto& x : container)` | 可修改元素 |
| 常引用 | `for (const auto& x : container)` | 只读，避免拷贝 |

## 4.4 while 与 do-while

与 C 相同：

```cpp
while (condition) { /* ... */ }

do { /* ... */ } while (condition);
```

## 4.5 break 与 continue

与 C 相同：跳出循环 / 跳过本次迭代。

## 4.6 条件运算符

与 C 相同：`condition ? expr1 : expr2`

C++14 起：`auto max = (a > b) ? a : b;` 类型需一致或可转换。

# 5 函数与重载

## 5.1 函数声明与定义

| 概念 | 说明 | 示例 |
|------|------|------|
| 声明 | 告知编译器签名 | `int add(int, int);` |
| 定义 | 提供函数体 | `int add(int a, int b) { return a+b; }` |
| 调用 | 按名传参 | `add(1, 2);` |

## 5.2 参数传递

| 方式 | 语法 | 说明 |
|------|------|------|
| 值传递 | `void f(int x)` | 拷贝，修改不影响实参 |
| 引用传递 | `void f(int& x)` | 别名，可修改实参 |
| 常引用 | `void f(const T& x)` | 只读，避免拷贝（推荐大对象） |
| 指针传递 | `void f(int* x)` | 可修改，可为 nullptr |

## 5.3 函数重载

同名函数，参数类型或个数不同：

```cpp
int add(int a, int b);
double add(double a, double b);
```

- 仅返回值不同不能构成重载
- C 不支持，C++ 支持

## 5.4 默认参数

```cpp
void greet(const std::string& name, const std::string& prefix = "Hello");
```

- 从右向左连续指定默认值
- 在声明处指定

## 5.5 inline 与 constexpr

| 关键字 | 作用 |
|--------|------|
| `inline` | 建议内联展开；类内成员函数默认为 inline |
| `constexpr` | 编译期常量/函数 |

# 6 引用与指针

## 6.1 引用

| 语法 | 说明 |
|------|------|
| `T& ref = var;` | 别名，必须初始化 |
| `const T& ref = var;` | 常引用，不可修改 |

## 6.2 指针

| 语法 | 说明 |
|------|------|
| `T* p = &var;` | 指向 var 的地址 |
| `*p` | 解引用 |
| `nullptr` | 空指针（C++11） |

## 6.3 new 与 delete

```cpp
int* p = new int(42);
delete p;
int* arr = new int[n]{...};
delete[] arr;
```

## 6.4 智能指针概要

| 类型 | 头文件 | 说明 |
|------|--------|------|
| `unique_ptr<T>` | `<memory>` | 独占所有权 |
| `shared_ptr<T>` | `<memory>` | 共享，引用计数 |
| `weak_ptr<T>` | `<memory>` | 弱引用，不增加计数 |

```cpp
auto p = std::make_unique<int>(42);
auto sp = std::make_shared<int>(42);
```

# 7 数组与 string

## 7.1 C 风格数组

```cpp
int arr[5] = {1, 2, 3, 4, 5};
int arr[]{1, 2, 3};  // C++11
```

## 7.2 std::array（C++11）

```cpp
#include <array>
std::array<int, 5> arr = {1, 2, 3, 4, 5};
arr.size();
```

## 7.3 std::string

| 操作 | 方法 |
|------|------|
| 长度 | `size()` / `length()` |
| 拼接 | `+` / `+=` |
| 访问 | `[i]` / `at(i)` |
| 子串 | `substr(pos, len)` |
| 查找 | `find(str)` |

## 7.4 std::vector 初览

```cpp
#include <vector>
std::vector<int> v = {1, 2, 3};
v.push_back(4);
v.pop_back();
v.size();
v[i];
```

# 8 类与对象

## 8.1 类定义

```cpp
class ClassName {
public:
    // 公有成员
private:
    // 私有成员
protected:
    // 保护成员
};
```

## 8.2 构造与析构

```cpp
class Foo {
public:
    Foo(int x) : member(x) {}  // 构造函数，初始化列表
    ~Foo() {}                  // 析构函数
private:
    int member;
};
```

## 8.3 成员函数

| 概念 | 说明 |
|------|------|
| 普通成员 | `void f();` |
| const 成员 | `void f() const;` 不修改对象 |
| 静态成员 | `static int count;` 类共享 |
| this | 指向当前对象的指针 |

## 8.4 访问控制

| 关键字 | 类内 | 类外 | 派生类 |
|--------|------|------|--------|
| public | ✓ | ✓ | ✓ |
| protected | ✓ | ✗ | ✓ |
| private | ✓ | ✗ | ✗ |

# 9 继承与多态

## 9.1 继承语法

```cpp
class Derived : public Base {
    // ...
};
```

## 9.2 虚函数

```cpp
class Base {
public:
    virtual void f();
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void f() override;
};
```

## 9.3 纯虚函数与抽象类

```cpp
virtual void f() = 0;  // 纯虚函数，类不能实例化
```

## 9.4 多态

基类指针/引用调用虚函数时，根据**实际对象类型**决定调用版本。

# 10 模板

## 10.1 函数模板

```cpp
template<typename T>
T maximum(T a, T b) { return (a > b) ? a : b; }
```

## 10.2 类模板

```cpp
template<typename T>
class Box {
    T content;
public:
    Box(T c) : content(c) {}
    T get() const { return content; }
};
```

## 10.3 typename 与 class

`template<typename T>` 与 `template<class T>` 在模板参数中等价。

# 11 STL 容器

## 11.1 vector

| 操作 | 方法 |
|------|------|
| 添加 | `push_back(x)` |
| 删除尾部 | `pop_back()` |
| 大小 | `size()` |
| 清空 | `clear()` |
| 访问 | `[i]` / `at(i)` |

## 11.2 map

```cpp
std::map<Key, Value> m;
m[key] = value;
m.find(key);
```

## 11.3 set

```cpp
std::set<T> s;
s.insert(x);
s.count(x);
```

## 11.4 迭代器

```cpp
for (auto it = v.begin(); it != v.end(); ++it)
    std::cout << *it;
```

# 12 STL 算法

```cpp
#include <algorithm>
```

| 算法 | 作用 | 示例 |
|------|------|------|
| `sort` | 排序 | `sort(v.begin(), v.end())` |
| `find` | 查找 | `find(v.begin(), v.end(), x)` |
| `count` | 计数 | `count(v.begin(), v.end(), x)` |
| `reverse` | 反转 | `reverse(v.begin(), v.end())` |
| `for_each` | 遍历执行 | `for_each(v.begin(), v.end(), fn)` |

# 13 文件流

## 13.1 头文件

`#include <fstream>`

## 13.2 文件流类

| 类 | 用途 |
|----|------|
| `ifstream` | 读文件 |
| `ofstream` | 写文件 |
| `fstream` | 读写 |

## 13.3 基本用法

```cpp
// 写
std::ofstream ofs("out.txt");
ofs << "Hello" << std::endl;
ofs.close();

// 读
std::ifstream ifs("in.txt");
std::string line;
while (std::getline(ifs, line))
    std::cout << line << std::endl;
```

# 14 智能指针与常用头文件

## 14.1 智能指针

| 类型 | 创建 | 说明 |
|------|------|------|
| unique_ptr | `make_unique<T>(args)` | 独占 |
| shared_ptr | `make_shared<T>(args)` | 共享 |
| weak_ptr | `weak_ptr<T>(sp)` | 弱引用 |

## 14.2 常用头文件

| 头文件 | 内容 |
|--------|------|
| `<iostream>` | cin, cout, cerr |
| `<string>` | string |
| `<vector>` | vector |
| `<map>` | map |
| `<set>` | set |
| `<algorithm>` | sort, find, count 等 |
| `<memory>` | unique_ptr, shared_ptr |
| `<fstream>` | 文件流 |
| `<array>` | array |

## 14.3 RAII 原则

资源在对象构造时获取，析构时自动释放。智能指针、文件 Guard 类均为 RAII 应用。

---

> 完整 C 语法请参阅 [C语言常用语法汇总.md](../../c/references/C语言常用语法汇总.md)。
