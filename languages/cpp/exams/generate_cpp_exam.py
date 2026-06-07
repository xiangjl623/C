#!/usr/bin/env python3
"""Generate C++ exam question banks (50 per type). Run from languages/cpp/exams/."""

from pathlib import Path

OUT = Path(__file__).parent

# --- Multiple choice (question, A, B, C, D, answer letter, explanation) ---
CHOICE = [
    ("C++ 源程序文件常用的扩展名是？", ".c", ".cpp", ".java", ".py", "B", "C++ 源文件通常为 .cpp/.cc/.cxx。"),
    ("C++ 中标准输出对象位于哪个命名空间？", "global", "std", "iostream", "cout", "B", "std::cout 在 std 命名空间。"),
    ("下列哪个是 C++ 特有的类型？", "int", "char", "bool", "float", "C", "bool 是 C++ 内置类型，C 用 int 模拟。"),
    ("引用变量必须？", "可为空", "必须初始化", "可重新绑定", "可为 nullptr", "B", "引用是别名，定义时必须绑定对象。"),
    ("nullptr 的类型是？", "int", "void*", "std::nullptr_t", "char*", "C", "C++11 引入 nullptr，类型为 std::nullptr_t。"),
    ("delete 与 delete[] 的区别？", "无区别", "delete[] 释放数组", "delete 更快", "只能 delete 指针", "B", "new[] 必须配对 delete[]。"),
    ("函数重载的依据是？", "返回值类型", "参数列表", "函数名长度", "是否 inline", "B", "参数类型或个数不同构成重载。"),
    ("默认参数应从哪侧开始指定？", "左侧", "右侧", "任意", "中间", "B", "默认参数从右向左连续。"),
    ("class 中 private 成员？", "类内外均可访问", "仅类内可访问", "派生类可访问", "全局可访问", "B", "private 仅本类可访问。"),
    ("构造函数的名字？", "Constructor", "与类名相同", "init", "任意", "B", "构造函数名与类名相同，无返回类型。"),
    ("析构函数名前加？", "~", "!", "-", "&", "A", "析构函数为 ~ClassName()。"),
    ("virtual 关键字的作用是？", "静态绑定", "运行时多态", "内联", "常量", "B", "virtual 实现运行时多态。"),
    ("override 用于？", "隐藏基类函数", "显式标记重写虚函数", "定义纯虚函数", "静态函数", "B", "C++11 override 标记虚函数重写。"),
    ("纯虚函数的写法？", "virtual void f();", "virtual void f() = 0;", "void f() override;", "abstract void f();", "B", "纯虚函数 = 0，类为抽象类。"),
    ("std::vector 的 push_back 作用？", "删除尾部", "尾部添加元素", "排序", "清空", "B", "push_back 在尾部追加。"),
    ("std::string 拼接常用？", "+ 或 +=", "strcat", "append only", "concat", "A", "string 支持 + 和 +=。"),
    ("范围 for 循环语法？", "for(i in v)", "for(auto x : v)", "foreach x in v", "for x : v", "B", "C++11: for (auto x : container)。"),
    ("auto 关键字作用？", "自动释放内存", "类型推导", "定义常量", "内联", "B", "auto 由初始化表达式推导类型。"),
    ("iostream 中 cout 属于？", "stderr", "stdout 对应流", "文件流", "字符串流", "B", "cout 为标准输出流。"),
    ("#include <iostream> 与 #include <stdio.h> 在 C++ 中推荐？", "stdio.h", "iostream", "都可以无差别", "都不推荐", "B", "C++ 风格用 iostream 和 std::。"),
    ("const 成员函数表示？", "函数是常量", "不修改对象状态", "静态函数", "内联函数", "B", "const 成员函数不能修改非 mutable 成员。"),
    ("静态成员变量属于？", "某个对象", "整个类共享", "栈", "仅 main", "B", "static 成员为类所有对象共享。"),
    ("继承方式 public 表示？", "is-a 关系", "has-a", "private 继承", "无关系", "A", "public 继承表达 is-a。"),
    ("基类指针指向派生类对象，调用 virtual 函数？", "调用基类版本", "调用派生类版本", "编译错误", "随机", "B", "虚函数运行时绑定派生类实现。"),
    ("模板函数定义？", "template<typename T>", "generic T", "typename template", "T template", "A", "template<typename T> 或 template<class T>。"),
    ("std::map 存储？", "仅值", "键值对", "仅键", "指针", "B", "map 为关联容器，存 key-value。"),
    ("algorithm 中 sort 需要？", "#include <sort>", "#include <algorithm>", "#include <vector> only", "无需头文件", "B", "sort 在 <algorithm> 中。"),
    ("unique_ptr 的特点？", "可复制", "独占所有权", "引用计数", "无析构", "B", "unique_ptr 独占，不可复制。"),
    ("shared_ptr 使用引用计数？", "否", "是", "仅 Windows", "仅 Linux", "B", "shared_ptr 共享所有权，use_count。"),
    ("RAII 的含义？", "资源获取即初始化", "随机访问", "运行时类型", "递归算法", "A", "构造获取资源，析构释放。"),
    ("using namespace std 在头文件中？", "推荐", "应避免", "必须", "仅 cpp 文件禁止", "B", "头文件中 using namespace std 会污染包含者。"),
    ("pragma once 作用？", "编译优化", "防止头文件重复包含", "定义宏", "命名空间", "B", "头文件保护。"),
    ("static_cast 用于？", "动态多态转换", "编译期可检查转换", "任意指针转换", "去除 const", "B", "static_cast 编译期静态转换。"),
    ("dynamic_cast 用于？", "整型转换", "多态类型安全向下转换", "浮点转换", "数组转换", "B", "dynamic_cast 用于多态类指针/引用。"),
    ("成员初始化列表语法？", ": member(val)", "= member(val)", "member(val) in body", "init member", "A", "构造函数 : member(val) {}。"),
    ("this 指针指向？", "基类", "当前对象", "全局", "nullptr", "B", "this 指向调用成员函数的对象。"),
    ("enum class 与 enum 相比？", "可隐式转 int", "作用域更强", "不能 switch", "更快", "B", "enum class 为强类型枚举。"),
    ("std::vector 与 C 数组相比？", "大小固定", "大小可变", "不能遍历", "无 []", "B", "vector 动态数组，可 push_back。"),
    ("fstream 读文件用？", "ofstream", "ifstream", "cout", "ostringstream", "B", "ifstream 输入文件流。"),
    ("make_unique 在哪个头文件？", "<utility>", "<memory>", "<vector>", "<unique>", "B", "C++14 make_unique 在 <memory>。"),
    ("函数模板实例化发生在？", "链接时", "编译时", "运行时", "加载时", "B", "模板在编译期实例化。"),
    ("虚析构函数的作用？", "加速析构", "多态 delete 时正确析构派生类", "禁止继承", "内联", "B", "基类指针 delete 需 virtual ~Base()。"),
    ("对象切片 (slicing) 发生在？", "值传递派生类给基类", "指针传递", "引用传递", "virtual 函数", "A", "按值赋/传基类会截断派生部分。"),
    ("std::find 返回？", "bool", "迭代器", "int", "void", "B", "find 返回迭代器，end() 表示未找到。"),
    ("const 引用参数常用于？", "修改实参", "避免拷贝且只读", "传递指针", "返回引用", "B", "const T& 大对象只读传参。"),
    ("inline 函数建议？", "所有函数", "短小的频繁调用函数", "递归函数", "虚函数", "B", "inline 建议短小函数；编译器可忽略。"),
    ("namespace 的作用是？", "加速编译", "避免命名冲突", "内存管理", "类型转换", "B", "namespace 组织标识符。"),
    ("C++ 中 main 返回值类型？", "void", "int", "任意", "bool", "B", "main 必须返回 int。"),
    ("std::endl 的作用？", "仅换行", "换行并刷新缓冲区", "清空 cout", "关闭流", "B", "endl 换行并 flush。"),
    ("weak_ptr 配合哪种指针？", "unique_ptr", "shared_ptr", "裸指针 only", "auto_ptr", "B", "weak_ptr 观察 shared_ptr，不增计数。"),
    ("C++ 与 C 的关系？", "完全无关", "C++ 是 C 的超集（几乎）", "C 是 C++ 子集", "互斥", "B", "C++ 兼容绝大部分 C 语法。"),
]

EXTRA_CHOICE = [
    ("下列不能构成函数重载？", "int f(int)", "double f(double)", "int f(int) const", "void f(int) 与 int f(int)", "D", "仅返回值不同不能重载。"),
    ("protected 成员谁可访问？", "仅 public", "类内和派生类", "全局", "仅派生类", "B", "protected: 本类与派生类。"),
    ("std::set 元素特点？", "可重复", "唯一且有序", "无序", "键值对", "B", "set 元素唯一，默认升序。"),
    ("lambda 表达式引入于？", "C++98", "C++11", "C++03", "C99", "B", "lambda 为 C++11 特性。"),
    ("移动语义主要为了？", "兼容 C", "减少不必要的拷贝", "增加指针", "禁用 RAII", "B", "C++11 move 减少拷贝开销。"),
    ("constexpr 函数？", "仅运行期", "编译期可求值", "等同 inline", "等同 virtual", "B", "constexpr 编译期常量/函数。"),
    ("std::array 与 vector 区别？", "array 固定大小", "array 在堆", "vector 固定", "无区别", "A", "array<N> 编译期固定大小。"),
    ("多继承可能引发？", "更快", "菱形继承歧义", "无影响", "禁止多态", "B", "多继承需注意虚继承与歧义。"),
    ("operator<< 重载常用于？", "cin", "cout 等流", "delete", "new", "B", "流插入运算符 <<。"),
    ("异常处理关键字？", "try catch throw", "try except", "raise handle", "error recover", "A", "C++: try/catch/throw。"),
    ("std::pair 常用于？", "map 的键值", "仅 vector", "指针", "数组", "A", "map 元素类型为 pair<const Key, T>。"),
    ("迭代器 end() 表示？", "最后一个元素", "尾后位置", "首元素", "空指针", "B", "end() 为尾后迭代器，非末元素。"),
    ("头文件中应放？", "函数实现（通常）", "声明与 inline 小函数", "main", "全局变量定义", "B", "实现放 cpp；模板常放头文件。"),
    ("g++ 编译 C++ 推荐标准？", "C++98 only", "C++17", "C89", "无标准", "B", "本教程推荐 -std=c++17。"),
    ("auto_ptr 在 C++11 后？", "推荐使用", "已弃用，用 unique_ptr", "等同 shared_ptr", "新增", "B", "auto_ptr 已弃用。"),
    ("const int* p 表示？", "p 不可改", "*p 不可改", "都不可改", "都可改", "B", "const int* 指向常量的指针。"),
    ("int* const p 表示？", "p 不可改", "*p 不可改", "都不可改", "p 可改指向", "A", "int* const 常量指针。"),
    ("STL 核心三组件？", "类、函数、宏", "容器、算法、迭代器", "输入输出文件", "指针数组", "B", "STL: 容器、算法、迭代器。"),
    ("virtual 函数表用于？", "编译速度", "运行时多态", "内存对齐", "模板", "B", "虚表实现动态绑定。"),
    ("std::getline 用于？", "读单个词", "读整行", "读整数", "写文件", "B", "getline(cin, line) 读含空格行。"),
    ("类默认访问控制？", "public", "private", "protected", "无", "B", "class 默认 private；struct 默认 public。"),
    ("struct 与 class 主要区别？", "无", "默认访问权限", "不能继承", "不能模板", "B", "struct 默认 public，class 默认 private。"),
    ("友元函数？", "成员函数", "可访问类 private 的非成员", "静态函数", "虚函数", "B", "friend 函数可访问私有成员。"),
    ("拷贝构造函数参数通常是？", "值", "const 类名&", "指针", "void", "B", "拷贝构造常用 const T&。"),
    ("深拷贝与浅拷贝区别？", "无", "是否复制指针指向资源", "速度", "语法", "B", "含指针成员需深拷贝。"),
    ("模板类 vector<int> 中 int 是？", "变量", "模板参数", "函数", "命名空间", "B", "模板实参。"),
    ("algorithm::count 返回？", "void", "元素个数", "迭代器", "bool", "B", "count 返回匹配次数。"),
    ("文件打开失败应检查？", "good()", "fail()/is_open()", "eof only", "无需", "B", "检查流状态和 is_open()。"),
    ("智能指针解决的主要问题？", "速度慢", "内存泄漏与所有权", "不能多态", "不能 STL", "B", "智能指针 RAII 管理堆内存。"),
    ("C++ 注释方式？", "仅 /* */", "// 与 /* */", "仅 #", "仅 --", "B", "C++ 支持 // 单行注释。"),
]

if len(CHOICE) >= 50:
    CHOICE = CHOICE[:50]
else:
    CHOICE = CHOICE + EXTRA_CHOICE[: 50 - len(CHOICE)]

def write_choice():
    q_lines = ["# C++ 语言期末考试 — 选择题（50 道）", "", "> 涵盖程序结构、引用、OOP、STL、智能指针等", "", "---", ""]
    a_lines = ["# C++ 语言期末考试 — 选择题参考答案与解析", "", "---", ""]
    for i, (q, a, b, c, d, ans, exp) in enumerate(CHOICE, 1):
        q_lines += [f"## {i}. {q}", "", f"A. {a}", f"B. {b}", f"C. {c}", f"D. {d}", ""]
        opts = {"A": a, "B": b, "C": c, "D": d}
        a_lines += [
            f"## 第 {i} 题", "", f"**题目：** {q}", "", "**选项：**", "",
            f"A. {a}" + (" ✓" if ans == "A" else ""),
            f"B. {b}" + (" ✓" if ans == "B" else ""),
            f"C. {c}" + (" ✓" if ans == "C" else ""),
            f"D. {d}" + (" ✓" if ans == "D" else ""),
            "", f"**答案：** {ans}. {opts[ans]}", "", f"**考点解析：** {exp}", "", "---", "",
        ]
    (OUT / "选择题.md").write_text("\n".join(q_lines), encoding="utf-8")
    (OUT / "选择题_参考答案.md").write_text("\n".join(a_lines), encoding="utf-8")


FILL = [
    ("C++ 源文件常用扩展名是 ______ 。", ".cpp"),
    ("标准命名空间名是 ______ 。", "std"),
    ("C++ 布尔类型关键字是 ______ 。", "bool"),
    ("布尔真值写作 ______ 。", "true"),
    ("空指针字面量 ______ 替代 NULL。", "nullptr"),
    ("动态分配单个对象用 ______ ，释放用 ______ 。", "new, delete"),
    ("动态数组释放必须用 ______ 。", "delete[]"),
    ("引用定义时必须 ______ 。", "初始化"),
    ("auto 用于 ______ 。", "类型推导"),
    ("iostream 中标准输出对象是 ______ 。", "cout"),
    ("iostream 中标准输入对象是 ______ 。", "cin"),
    ("头文件保护常用 ______ 。", "#pragma once"),
    ("作用域解析运算符是 ______ 。", "::"),
    ("函数重载依据 ______ 不同。", "参数列表"),
    ("默认参数从 ______ 侧开始指定。", "右"),
    ("inline 建议用于 ______ 函数。", "短小"),
    ("class 默认成员访问权限是 ______ 。", "private"),
    ("构造函数名与 ______ 相同。", "类名"),
    ("析构函数名前加 ______ 。", "~"),
    ("const 成员函数不能修改 ______ 。", "对象状态/非mutable成员"),
    ("virtual 函数实现 ______ 多态。", "运行时"),
    ("纯虚函数写法 virtual void f() = ______ 。", "0"),
    ("override 用于标记 ______ 。", "重写虚函数"),
    ("public 继承表达 ______ 关系。", "is-a"),
    ("基类指针指向派生类，virtual 调用 ______ 类版本。", "派生"),
    ("模板定义 template<______ T>", "typename"),
    ("vector 尾部添加用 ______ 。", "push_back"),
    ("string 拼接可用 ______ 运算符。", "+"),
    ("范围 for 语法 for (auto x : ______)", "container"),
    ("sort 在头文件 ______ 中。", "<algorithm>"),
    ("map 存储 ______ 对。", "键值"),
    ("unique_ptr ______ 复制。", "不可"),
    ("shared_ptr 使用 ______ 计数。", "引用"),
    ("RAII 即资源获取即 ______ 。", "初始化"),
    ("make_unique 在 ______ 头文件。", "<memory>"),
    ("ifstream 用于读 ______ 。", "文件"),
    ("ofstream 用于 ______ 文件。", "写"),
    ("this 指向 ______ 对象。", "当前"),
    ("静态成员属于 ______ 而非某个对象。", "整个类"),
    ("enum class 是 ______ 类型枚举。", "强"),
    ("constexpr 用于 ______ 期常量。", "编译"),
    ("static_cast 是 ______ 期转换。", "编译"),
    ("dynamic_cast 用于 ______ 类型转换。", "多态"),
    ("迭代器 end() 表示尾 ______ 位置。", "后"),
    ("STL 三组件：容器、算法、______ 。", "迭代器"),
    ("虚析构函数用于 ______ delete 时正确析构。", "多态"),
    ("对象切片发生在 ______ 传递派生类。", "值"),
    ("weak_ptr 配合 ______ 使用。", "shared_ptr"),
    ("getline 可读取含 ______ 的整行。", "空格"),
    ("g++ 推荐标准 ______ 。", "C++17"),
]

FILL = FILL[:50]

def write_fill():
    q_lines = ["# C++ 语言期末考试 — 填空题（50 道）", "", "---", ""]
    a_lines = ["# C++ 语言期末考试 — 填空题参考答案与解析", "", "---", ""]
    for i, (q, ans) in enumerate(FILL, 1):
        q_lines.append(f"{i}. {q}")
        q_lines.append("")
        a_lines += [f"## 第 {i} 题", "", f"**题目：** {q}", "", f"**答案：** {ans}", "", f"**考点解析：** 见 C++ 教程相关章节。", "", "---", ""]
    (OUT / "填空题.md").write_text("\n".join(q_lines), encoding="utf-8")
    (OUT / "填空题_参考答案.md").write_text("\n".join(a_lines), encoding="utf-8")


QA = [
    "简述 C++ 与 C 的主要区别。",
    "什么是引用？与指针有何不同？",
    "解释 RAII 原则及其意义。",
    "什么是函数重载？重载规则是什么？",
    "解释构造函数和析构函数的作用。",
    "什么是封装？如何实现？",
    "解释 public、private、protected 访问控制。",
    "什么是多态？编译期与运行期多态区别？",
    "virtual 函数如何实现运行时多态？",
    "什么是纯虚函数和抽象类？",
    "解释 override 与 overload 的区别。",
    "什么是对象切片？如何避免？",
    "为什么多态基类需要虚析构函数？",
    "简述模板函数与模板类。",
    "STL 由哪三部分组成？",
    "vector 与 list 的适用场景比较。",
    "map 与 unordered_map 的区别（概念层面）。",
    "unique_ptr 与 shared_ptr 的区别。",
    "new/delete 与 malloc/free 的区别。",
    "解释 namespace 的作用。",
    "iostream 与 stdio.h 在 C++ 中的选择。",
    "const 成员函数的意义。",
    "静态成员变量与静态成员函数特点。",
    "初始化列表的优点。",
    "this 指针的作用。",
    "enum class 相比 enum 的优势。",
    "范围 for 循环的语法与适用场景。",
    "auto 关键字的使用注意。",
    "深拷贝与浅拷贝的概念。",
    "友元函数与友元类的作用。",
    "继承方式 public/protected/private 的含义。",
    "什么是菱形继承问题？",
    "迭代器的作用。",
    "algorithm 中 sort 的使用前提。",
    "fstream 读写文件基本步骤。",
    "异常处理 try-catch-throw 流程。",
    "constexpr 与 const 的区别。",
    "static_cast 与 dynamic_cast 用途。",
    "pragma once 与 include guard。",
    "using 声明与 using 指令区别。",
    "string 与 C 字符数组比较。",
    "push_back 与 emplace_back 概念（C++11）。",
    "weak_ptr 解决什么问题？",
    "make_unique/make_shared 的优点。",
    "C++ 程序编译链接四阶段。",
    "头文件与源文件如何分工？",
    "inline 函数的作用与限制。",
    "默认参数与重载的潜在冲突。",
    "智能指针为何优于裸 new/delete？",
    "学完 C++ 基础后推荐的进阶方向。",
]

QA_ANS = [
    "C++ 在 C 基础上增加 OOP、模板、STL、异常、namespace 等；兼容大部分 C 语法。",
    "引用是别名，必须初始化，不能空，不能重绑；指针存地址，可为空，可改指向。",
    "构造获取资源，析构释放；保证异常安全，减少泄漏。",
    "同名不同参；参数类型或个数须不同，不能仅靠返回值区分。",
    "构造初始化对象，析构清理资源；对象创建/销毁时自动调用。",
    "隐藏实现细节，仅暴露接口；private 数据 + public 方法。",
    "public 内外可访问；private 仅本类；protected 本类与派生类。",
    "同一接口不同行为；编译期如重载、模板；运行期靠 virtual。",
    "通过虚表指针在运行时查表调用派生类重写版本。",
    "纯虚函数 =0，含纯虚函数的类不能实例化，需派生实现。",
    "override 重写基类虚函数；overload 同名不同参。",
    "派生类对象按值赋给基类会丢失派生部分；用指针/引用或 virtual。",
    "基类指针 delete 派生对象时，无 virtual 析构只调基类析构，可能泄漏。",
    "template<typename T> 定义与类型无关的函数/类，编译期实例化。",
    "容器、算法、迭代器。",
    "vector 随机访问快；list 中间插入删除快（本教程以 vector 为主）。",
    "map 有序（红黑树）；unordered_map 哈希平均 O(1)（C++11）。",
    "unique_ptr 独占；shared_ptr 共享引用计数。",
    "new/delete 类型安全、调构造析构；malloc/free 不调用构造析构。",
    "将标识符分组，避免命名冲突；std 为标准库。",
    "推荐 iostream 与 std 命名空间，类型更安全。",
    "承诺不修改对象成员（mutable 除外）。",
    "属于类而非对象；静态函数无 this，只能访问静态成员。",
    "直接初始化成员，效率高于构造体内赋值；const/引用成员必须用。",
    "指向当前对象，用于成员函数内访问成员、链式调用。",
    "限定作用域，不能隐式转 int，类型更安全。",
    "for (auto x : range)，简化容器遍历。",
    "简化复杂类型；简单类型可显式写出更清晰。",
    "浅拷贝共享指针；深拷贝复制所指向资源。",
    "非成员可访问类 private，破坏封装但用于运算符重载等。",
    "public is-a；protected 实现继承；private 隐藏基类接口。",
    "多路径继承同一基类导致歧义；可用虚继承。",
    "统一访问容器元素，连接算法与容器。",
    "需随机访问迭代器；vector 可用，list 不可用 sort。",
    "ofstream 写，ifstream 读，打开后检查 is_open，用完 close。",
    "try 可能抛异常代码，catch 捕获，throw 抛出。",
    "constexpr 编译期常量；const 只读，可能运行期初始化。",
    "static_cast 一般转换；dynamic_cast 多态向下转换。",
    "均防止重复包含；pragma once 简洁，include guard 更 portable。",
    "using std::cout 引入单个；using namespace std 引入全部。",
    "string 自动管理长度，操作更安全；C 数组需手动管理 \\0。",
    "emplace_back 原地构造，可能减少拷贝（C++11）。",
    "打破 shared_ptr 循环引用。",
    "异常安全，避免裸 new；make_shared 一次分配控制块。",
    "预处理、编译、汇编、链接。",
    "头文件声明，cpp 实现；模板常放头文件。",
    "建议编译器内联展开，减少调用开销；递归/虚函数不宜。",
    "默认参影响匹配，可能产生歧义，需谨慎设计。",
    "自动释放、异常安全、所有权明确。",
    "Effective Modern C++、STL 深入、系统编程、项目实践。",
]

def write_qa():
    q_lines = ["# C++ 语言期末考试 — 问答题（50 道）", "", "---", ""]
    a_lines = ["# C++ 语言期末考试 — 问答题参考答案与解析", "", "---", ""]
    for i, (q, a) in enumerate(zip(QA, QA_ANS), 1):
        q_lines += [f"## {i}. {q}", ""]
        a_lines += [f"## 第 {i} 题", "", f"**题目：** {q}", "", f"**参考答案：** {a}", "", "**考点解析：** 见 C++ 教程对应章节。", "", "---", ""]
    (OUT / "问答题.md").write_text("\n".join(q_lines), encoding="utf-8")
    (OUT / "问答题_参考答案.md").write_text("\n".join(a_lines), encoding="utf-8")


FIX = [
    ("#include <iostream>\nint main() {\n    int& r;\n    return 0;\n}", "引用必须初始化"),
    ("#include <iostream>\nint main() {\n    int* p = new int[10];\n    delete p;\n    return 0;\n}", "数组应 delete[]"),
    ("class Base { public: ~Base() {} };\nclass Derived : public Base { public: ~Derived() {} };\nint main() { Base* p = new Derived(); delete p; }", "基类析构应 virtual"),
    ("#include <iostream>\nusing namespace std;\nint main() { cout << \"Hi\" }", "语句缺分号"),
    ("#include <vector>\nint main() { std::vector<int> v; v[0] = 1; }", "未 push_back 就 v[0] 越界"),
    ("void f(int x = 1, int y) {}\nint main() { f(); }", "默认参数应从右连续"),
    ("class A { int x; };\nint main() { A a; a.x = 1; }", "x 为 private 不可外访"),
    ("#include <iostream>\nint main() { std::cout << std::endl }", "缺分号"),
    ("int* p = nullptr;\n*p = 5;", "解引用空指针"),
    ("#include <string>\nstd::string s = 'A';", "应用双引号字符串"),
    ("template<typename T>\nT add(T a, T b) { return a+b; }\nint main() { add(1, 2.0); }", "模板参数类型不一致"),
    ("class B : A {};", "继承缺 public/private 关键字，class 默认 private 继承"),
    ("#include <memory>\nauto p = std::unique_ptr<int>(new int(1));\nauto q = p;", "unique_ptr 不可复制"),
    ("void f(int arr[]) { sizeof(arr); }", "数组参数退化为指针，sizeof 非数组大小"),
    ("#include <iostream>\nnamespace N { int x; }\nint x;\nint main() { std::cout << x; }", "可能歧义，应 N::x"),
    ("class C { virtual void f(); };\nint main() { C c; }", "含虚函数的类需实现或纯虚"),
    ("#include <vector>\nfor (auto it = v.begin(); it != v.end(); ++it) {}", "v 未定义"),
    ("const int MAX = 100;\nMAX = 200;", "const 不可修改"),
    ("#include <fstream>\nstd::ifstream f(\"a.txt\");\nf << \"data\";", "ifstream 不能 << 写"),
    ("int& f() { int x=0; return x; }", "返回局部变量引用悬垂"),
    ("delete nullptr;", "合法但前面若 new 需配对"),
    ("class D: public Base { void f() override; }; // Base 无 virtual f", "override 但基类无 virtual f"),
    ("std::cout << \"n=\" << n;", "n 未声明"),
    ("#include <iostream>\nmain() { return 0; }", "main 缺 int 返回类型"),
    ("enum Color { Red, Green }; int x = Red::Green;", "普通 enum 无作用域限定"),
    ("#include <vector>\nstd::vector<int>& ref = std::vector<int>{1,2};", "绑定临时对象需 const 引用"),
    ("class X { X(); };", "构造函数 private 且无友元，外部无法创建"),
    ("void swap(int a, int b) { int t=a; a=b; b=t; }", "值传递无法交换实参"),
    ("#include <string>\nif (s = \"ok\") {}", "应用 == 比较，= 是赋值"),
    ("class A { public: A(int); }; A a;", "无默认构造但无 int 实参"),
    ("#include <algorithm>\nstd::list<int> L; std::sort(L.begin(), L.end());", "list 迭代器非随机访问，不能 sort"),
    ("shared_ptr<int> p; p.reset(); *p = 1;", "reset 后为空，不能解引用"),
    ("virtual void f() const;", "若类无 const 版本虚函数，派生 override 需匹配"),
    ("#include <iostream>\nstd::cin >> std::cout;", "不能从 cout 读"),
    ("class B { B(const B&); }; B b2 = b1;", "若拷贝构造 private 且非 friend 则错误"),
    ("throw \"error\";", "可编译但 catch 需匹配类型，建议 std::exception"),
    ("#include <memory>\nstd::auto_ptr<int> p(new int(1));", "auto_ptr 已弃用"),
    ("namespace std { int hack; }", "禁止在 std 加声明"),
    ("#define CLASS class\nCLASS Foo {};", "宏污染，应用 class"),
    ("int* p=new int(1); delete p; delete p;", "double delete 未定义行为"),
    ("class Base {}; class Der: public Base {};\nvoid f(Base b) {}\nint main(){ Der d; f(d); }", "值传递导致切片，应 Base& 或 Base*"),
    ("template<class T> void g(T x) {}\ng(1, 2);", "参数个数错误"),
    ("#include <map>\nstd::map<int,int> m; m[1.5]=2;", "键类型应为 int"),
    ("constexpr int f() { return n; } int n=1;", "constexpr 需编译期，依赖运行时 n"),
    ("#include <vector>\nstd::vector<int> v(5); v.push_back() ", "push_back 需参数"),
    ("friend void fn(); class C { friend void fn(); int x; }; void fn(){ C c; c.x=0; }", "fn 需声明 C 或定义在 C 后"),
    ("static int s; int main(){ s=1; }", "static 成员需类外定义"),
    ("#include <iostream>\nusing namespace std; using namespace std;", "重复 using 无害但冗余"),
    ("class A { virtual void f()=0; }; int main(){ A a; }", "抽象类不能实例化"),
    ("#include <string>\nstd::string s=\"abc\"; s[10];", "越界应用 at 或检查 size"),
]

FIX_ANS = [note for _, note in FIX]

def write_fix():
    q_lines = ["# C++ 语言期末考试 — 纠错题（50 道）", "", "> 找出并改正代码中的错误", "", "---", ""]
    a_lines = ["# C++ 语言期末考试 — 纠错题参考答案与解析", "", "---", ""]
    for i, (code, note) in enumerate(FIX, 1):
        q_lines += [f"## 第 {i} 题", "", "```cpp", code, "```", ""]
        a_lines += [f"## 第 {i} 题", "", "**原代码：**", "", "```cpp", code, "```", "", f"**错误分析：** {note}", "", f"**改正要点：** 根据错误分析修正语法或逻辑。", "", "---", ""]
    (OUT / "纠错题.md").write_text("\n".join(q_lines), encoding="utf-8")
    (OUT / "纠错题_参考答案.md").write_text("\n".join(a_lines), encoding="utf-8")


PROG = [
    "用 cin/cout 输入两个整数，输出和、差、积、商。",
    "输入姓名（string），输出问候语。",
    "用 vector 存储 n 个整数，输出最大值。",
    "判断输入年份是否为闰年。",
    "用 string 反转字符串。",
    "统计 string 中元音字母个数。",
    "实现函数重载：print(int) 与 print(double)。",
    "实现 swap(int&, int&) 交换两整数。",
    "定义 Circle 类，含半径与 area() 方法。",
    "定义 Student 类，含 name、id 与 display()。",
    "用 vector<Student> 存储并遍历输出。",
    "派生 Dog 继承 Animal，重写 speak() 虚函数。",
    "用 map 统计单词出现次数（简化：以空格分隔）。",
    "用 sort 对 vector<int> 升序排序。",
    "用 find 在 vector 中查找指定值。",
    "文件写入三行文本到 out.txt。",
    "从 in.txt 读取并输出所有行。",
    "unique_ptr 管理 int 动态对象并输出。",
    "shared_ptr 共享对象，打印 use_count。",
    "模板函数 maximum(T,T) 返回较大值。",
    "类模板 Box<T> 存单个值并提供 get/set。",
    "const 成员函数 getX() 返回坐标。",
    "静态成员计数创建对象个数。",
    "构造函数初始化列表初始化成员。",
    "析构函数输出对象销毁信息（RAII 演示）。",
    "enum class 表示星期，switch 输出名称。",
    "范围 for 遍历 vector<string>。",
    "auto 推导并输出变量类型大小（typeid/sizeof）。",
    "默认参数 greet(name, prefix=\"Hello\")。",
    "深拷贝：含 char* 成员的类实现拷贝构造（简化用 string）。",
    "抽象类 Shape 派生 Rectangle 实现 area()。",
    "多态：基类指针数组调用 virtual draw()。",
    "operator+ 重载复数类（实部虚部）。",
    "friend 函数访问类 private 数据。",
    "vector 去重（先 sort 再 unique erase）。",
    "set 插入元素并遍历输出。",
    "stringstream 解析 \"123 456\" 为两个 int。",
    "getline 读整行含空格。",
    "fstream 追加模式打开文件写一行。",
    "检查文件 is_open 再读写。",
    "类 BankAccount：deposit/withdraw/getBalance。",
    "继承 Person 派生 Employee 增加工号。",
    "override 重写基类 virtual print()。",
    "纯虚函数接口 Printable 派生实现。",
    "weak_ptr 观察 shared_ptr 是否过期。",
    "make_unique 创建 vector<int> 并填充 1..n。",
    "algorithm count 统计 vector 中某值个数。",
    "二维 vector 表示矩阵并输出。",
    "StudentManager 简化版：add/list（单文件）。",
    "综合：读文件学生列表到 vector，按学号查找。",
]

PROG_SNIPPETS = [
'''#include <iostream>
int main() {
    int a, b; std::cin >> a >> b;
    std::cout << a+b << " " << a-b << " " << a*b << " " << a/b << std::endl;
    return 0;
}''',
'''#include <iostream>
#include <string>
int main() {
    std::string name; std::getline(std::cin, name);
    std::cout << "Hello, " << name << "!" << std::endl;
    return 0;
}''',
'''#include <iostream>
#include <vector>
#include <algorithm>
int main() {
    int n; std::cin >> n; std::vector<int> v(n);
    for (int& x : v) std::cin >> x;
    std::cout << *std::max_element(v.begin(), v.end()) << std::endl;
    return 0;
}''',
'''#include <iostream>
int main() {
    int y; std::cin >> y;
    bool leap = (y%4==0 && y%100!=0) || (y%400==0);
    std::cout << (leap ? "yes" : "no") << std::endl;
    return 0;
}''',
'''#include <iostream>
#include <string>
#include <algorithm>
int main() {
    std::string s; std::cin >> s;
    std::reverse(s.begin(), s.end());
    std::cout << s << std::endl;
    return 0;
}''',
'''#include <iostream>
#include <string>
int main() {
    std::string s; std::cin >> s; int c=0;
    for (char ch : s)
        if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||
            ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U') c++;
    std::cout << c << std::endl;
    return 0;
}''',
'''#include <iostream>
void print(int x){ std::cout<<"int:"<<x<<std::endl; }
void print(double x){ std::cout<<"double:"<<x<<std::endl; }
int main(){ print(1); print(3.14); return 0; }''',
'''#include <iostream>
void swap(int& a, int& b){ int t=a; a=b; b=t; }
int main(){ int x=1,y=2; swap(x,y); std::cout<<x<<" "<<y; return 0; }''',
'''#include <iostream>
class Circle {
    double r;
public:
    Circle(double radius): r(radius) {}
    double area() const { return 3.14159*r*r; }
};
int main(){ Circle c(5); std::cout<<c.area(); return 0; }''',
'''#include <iostream>
#include <string>
class Student {
public:
    std::string name, id;
    void display() const { std::cout << id << " " << name << std::endl; }
};
int main(){ Student s{"Alice","001"}; s.display(); return 0; }''',
]

# Fill remaining with chapter references + minimal stubs
_DEFAULT = '''// 见 languages/cpp/examples/ 对应章节与 guides 文末练习
#include <iostream>
int main() { /* 按题目要求实现 */ return 0; }'''

while len(PROG_SNIPPETS) < len(PROG):
    PROG_SNIPPETS.append(_DEFAULT)

def write_prog():
    q_lines = ["# C++ 语言期末考试 — 编程题（50 道）", "", "---", ""]
    a_lines = ["# C++ 语言期末考试 — 编程题参考答案与解析", "", "---", ""]
    for i, (q, code) in enumerate(zip(PROG, PROG_SNIPPETS[:len(PROG)]), 1):
        q_lines.append(f"{i}. {q}")
        q_lines.append("")
        a_lines += [f"## 第 {i} 题", "", f"**题目：** {q}", "", "**参考实现：**", "", "```cpp", code, "```", "", "**思路：** 见 [examples/chapter08+](../examples/) 及对应 guides。", "", "---", ""]
    (OUT / "编程题.md").write_text("\n".join(q_lines), encoding="utf-8")
    (OUT / "编程题_参考答案.md").write_text("\n".join(a_lines), encoding="utf-8")


if __name__ == "__main__":
    write_choice()
    write_fill()
    write_qa()
    write_fix()
    write_prog()
    print("Generated C++ exam files in", OUT)
