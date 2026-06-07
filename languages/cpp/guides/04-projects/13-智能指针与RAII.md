
# 智能指针与RAII

## 自动管理资源

C 语言中动态内存需手动 `malloc`/`free`，容易泄漏或重复释放。C++ 的 **RAII**（Resource Acquisition Is Initialization）原则：资源在对象构造时获取，析构时自动释放。**智能指针**是 RAII 的典型应用。

> C 内存管理详见 [C 语言内存管理](../../c/guides/03-advanced/11-内存管理：堆与栈的奥秘.md)。

---

## 一、RAII 原则

```cpp
class FileGuard {
    FILE* fp;
public:
    FileGuard(const char* path) { fp = fopen(path, "r"); }
    ~FileGuard() { if (fp) fclose(fp); }
    FILE* get() { return fp; }
};

void process() {
    FileGuard guard("data.txt");
    // 使用 guard.get() ...
}  // 离开作用域，自动 fclose
```

**核心**：用对象生命周期管理资源，无需手动释放。

---

## 二、unique_ptr

独占所有权，不可复制，可移动：

```cpp
#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<int> p = std::make_unique<int>(42);
    std::cout << *p << std::endl;

    // std::unique_ptr<int> p2 = p;  // 错误：不可复制
    std::unique_ptr<int> p2 = std::move(p);  // 可移动

    return 0;
}  // 自动 delete
```

| 操作 | 说明 |
|------|------|
| `std::make_unique<T>(args)` | 创建 unique_ptr（C++14） |
| `*p` / `p->` | 解引用 |
| `p.get()` | 获取裸指针 |
| `p.release()` | 释放所有权，返回裸指针 |

---

## 三、shared_ptr

共享所有权，引用计数：

```cpp
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> p1 = std::make_shared<int>(42);
    std::shared_ptr<int> p2 = p1;  // 引用计数 = 2

    std::cout << *p1 << ", 引用计数：" << p1.use_count() << std::endl;

    p2.reset();  // 引用计数 = 1
    return 0;
}  // p1 销毁时 delete
```

---

## 四、weak_ptr

配合 shared_ptr 使用，不增加引用计数，避免循环引用：

```cpp
std::shared_ptr<int> sp = std::make_shared<int>(42);
std::weak_ptr<int> wp = sp;

if (auto locked = wp.lock())
    std::cout << *locked << std::endl;
```

---

## 五、与 C malloc/free 对比

| 特性 | malloc/free | 智能指针 |
|------|-------------|----------|
| 释放 | 手动 free | 自动析构 |
| 异常安全 | 易泄漏 | RAII 保证 |
| 所有权 | 不明确 | unique/shared 明确 |
| 推荐 | C 代码 | 现代 C++ |

---

## 六、实战练习

### 练习1：unique_ptr 管理数组

`std::unique_ptr<int[]>` 管理动态数组。

### 练习2：shared_ptr 共享

两个 shared_ptr 指向同一对象，观察 use_count 变化。

### 练习3：RAII 文件类

实现 FileRAII 类，构造打开文件，析构关闭文件。

---

## 七、总结与延伸

### 本节重点回顾

1. **RAII**：资源随对象生命周期自动管理
2. **unique_ptr**：独占所有权，不可复制
3. **shared_ptr**：共享所有权，引用计数
4. **make_unique/make_shared**：推荐创建方式

### 下节预告

下一篇：《综合实战：面向对象学生管理系统》。

### 延伸阅读

- [C 语言内存管理](../../c/guides/03-advanced/11-内存管理：堆与栈的奥秘.md)
- [C++ 速查 §14 智能指针](../../references/C++常用语法汇总.md#14-智能指针与常用头文件)

---

📌 **知识点卡片**
- #include <memory>
- unique_ptr：独占；shared_ptr：共享
- make_unique<T>() / make_shared<T>()

---

> 下一篇见！
