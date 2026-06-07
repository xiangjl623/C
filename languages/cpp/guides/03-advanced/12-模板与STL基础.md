
# 模板与STL基础

## 泛型编程与标准库

**模板**让代码与类型无关；**STL**（Standard Template Library）提供容器、算法和迭代器，是 C++ 最强大的特性之一。

---

## 一、函数模板

```cpp
#include <iostream>

template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << maximum(3, 5) << std::endl;
    std::cout << maximum(3.14, 2.71) << std::endl;
    return 0;
}
```

- `template<typename T>` 或 `template<class T>` 等价
- 编译器根据实参类型自动生成 `maximum<int>`、`maximum<double>` 等

---

## 二、类模板

```cpp
#include <iostream>

template<typename T>
class Box {
private:
    T content;

public:
    Box(T c) : content(c) {}
    T get() const { return content; }
    void set(T c) { content = c; }
};

int main() {
    Box<int> intBox(42);
    Box<std::string> strBox("Hello");
    std::cout << intBox.get() << std::endl;
    std::cout << strBox.get() << std::endl;
    return 0;
}
```

---

## 三、STL 容器

### 3.1 vector（动态数组）

```cpp
#include <vector>
std::vector<int> vec = {1, 2, 3};
vec.push_back(4);
vec.pop_back();
vec.size();
vec[i];
```

### 3.2 map（键值对）

```cpp
#include <map>
#include <string>

std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"] = 87;

for (const auto& pair : scores)
    std::cout << pair.first << ": " << pair.second << std::endl;
```

### 3.3 set（有序集合）

```cpp
#include <set>
std::set<int> s = {3, 1, 4, 1, 5};  // 自动去重排序
for (int x : s) std::cout << x << " ";  // 1 3 4 5
```

---

## 四、迭代器

容器提供迭代器遍历：

```cpp
std::vector<int> vec = {1, 2, 3, 4, 5};
for (auto it = vec.begin(); it != vec.end(); ++it)
    std::cout << *it << " ";

// 更简洁：范围 for
for (const auto& v : vec)
    std::cout << v << " ";
```

---

## 五、STL 算法

```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9};

    std::sort(vec.begin(), vec.end());

    auto it = std::find(vec.begin(), vec.end(), 8);
    if (it != vec.end())
        std::cout << "找到 8，位置：" << (it - vec.begin()) << std::endl;

    int count = std::count(vec.begin(), vec.end(), 2);
    std::cout << "2 出现 " << count << " 次" << std::endl;

    return 0;
}
```

| 算法 | 作用 |
|------|------|
| `sort` | 排序 |
| `find` | 查找元素 |
| `count` | 计数 |
| `reverse` | 反转 |
| `for_each` | 对每个元素执行函数 |

---

## 六、常用头文件

| 头文件 | 内容 |
|--------|------|
| `<vector>` | 动态数组 |
| `<map>` | 键值映射 |
| `<set>` | 有序集合 |
| `<string>` | 字符串 |
| `<algorithm>` | 算法 |
| `<iostream>` | 输入输出 |

---

## 七、实战练习

### 练习1：模板栈

实现类模板 `Stack<T>`，含 `push`、`pop`、`top`、`empty`。

### 练习2：map 词频统计

读入一行文本，用 `map<string, int>` 统计每个单词出现次数。

### 练习3：algorithm 综合

对 vector 排序后，用 `find` 查找指定值，用 `count` 统计某元素个数。

---

## 八、总结与延伸

### 本节重点回顾

1. **函数模板** `template<typename T>` 泛型函数
2. **类模板** `template<typename T> class Box`
3. **STL 容器**：vector、map、set
4. **STL 算法**：sort、find、count 等，需 `#include <algorithm>`

### 下节预告

进入实战阶段：《智能指针与 RAII》。

### 延伸阅读

- [fundamentals/04-data-structures/](../../../fundamentals/04-data-structures/)
- [C++ 速查 §10～12](../../references/C++常用语法汇总.md#10-模板)

---

📌 **知识点卡片**
- template<typename T> 函数/类模板
- vector/map/set；#include <algorithm>
- sort(v.begin(), v.end()); find(v.begin(), v.end(), x);

---

> 下一篇见！
