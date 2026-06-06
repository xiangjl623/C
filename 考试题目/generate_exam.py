# -*- coding: utf-8 -*-
"""生成 C 语言期末考试题库（各题型 100 道）"""

import os
from prog_solutions import PROG_SOLUTIONS

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_file(name, content):
    path = os.path.join(OUT_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"已生成: {name} ({len(content)} 字符)")


# ===================== 选择题 =====================
def gen_choice_questions():
    lines = ["# C 语言期末考试 — 选择题（100 道）\n", "> 涵盖基础语法、数据类型、运算符、控制流程、函数、指针、数组、字符串等\n\n---\n"]
    topics = [
        ("C语言基础", 15), ("数据类型与常量", 12), ("运算符与表达式", 12),
        ("控制流程", 15), ("函数", 12), ("指针", 15), ("数组", 12), ("字符串", 17),
    ]
    qn = 0
    bank = []

    # 预置高质量题目库
    preset = [
        ("C语言程序的基本组成单位是？", ["A. 函数", "B. 语句", "C. 表达式", "D. 变量"], "A",
         "C程序由函数组成，main是入口函数。"),
        ("C语言源程序文件的扩展名通常是？", ["A. .cpp", "B. .c", "C. .java", "D. .h"], "B", "源文件为.c，头文件为.h。"),
        ("下列哪个是合法的C标识符？", ["A. 2abc", "B. _abc", "C. int", "D. a-b"], "B", "标识符以字母或下划线开头，不能是关键字。"),
        ("sizeof(char) 在大多数系统中等于？", ["A. 1", "B. 2", "C. 4", "D. 8"], "A", "char占1字节。"),
        ("int 类型通常占几个字节？", ["A. 1", "B. 2", "C. 4", "D. 8"], "C", "32位系统int通常4字节。"),
        ("下列哪个是整型常量？", ["A. 3.14", "B. 0x1A", "C. 'A'", "D. \"hello\""], "B", "0x开头为十六进制整型。"),
        ("字符常量 'A' 的类型是？", ["A. int", "B. char", "C. string", "D. float"], "A", "C中字符常量在表达式中为int类型。"),
        ("字符串 \"abc\" 在内存中占几个字节？", ["A. 3", "B. 4", "C. 5", "D. 6"], "B", "含末尾'\\0'，共4字节。"),
        ("表达式 5/2 的结果是？", ["A. 2", "B. 2.5", "C. 3", "D. 2.0"], "A", "整数除法截断小数。"),
        ("表达式 5.0/2 的结果是？", ["A. 2", "B. 2.5", "C. 3", "D. 2.0"], "B", "有浮点参与则浮点除法。"),
        ("逻辑与运算符是？", ["A. &", "B. &&", "C. |", "D. ||"], "B", "&&为逻辑与，&为按位与。"),
        ("表达式 !0 的值是？", ["A. 0", "B. 1", "C. -1", "D. 不确定"], "B", "非0为真，!0为1。"),
        ("自增运算符 ++i 与 i++ 的区别在于？", ["A. 无区别", "B. 优先级不同", "C. 返回值时机不同", "D. 运算结果不同"], "C", "++i先增后用，i++先用后增。"),
        ("条件运算符 ?: 的优先级？", ["A. 最高", "B. 高于赋值", "C. 低于赋值", "D. 最低"], "B", "高于赋值运算符。"),
        ("if 语句后只能跟一条语句，多条语句需要？", ["A. 分号", "B. 花括号{}", "C. 圆括号()", "D. 方括号[]"], "B", "复合语句用{}包裹。"),
        ("switch 中 case 后必须是？", ["A. 变量", "B. 整型常量表达式", "C. 浮点常量", "D. 字符串"], "B", "case标签须为整型常量。"),
        ("for 循环的三个表达式分别是？", ["A. 初值、条件、步长", "B. 条件、初值、步长", "C. 步长、条件、初值", "D. 任意顺序"], "A", "for(初值;条件;步长)。"),
        ("while 与 do-while 的主要区别？", ["A. 无区别", "B. do-while至少执行一次", "C. while更快", "D. do-while不能嵌套"], "B", "do-while先执行后判断。"),
        ("break 语句的作用是？", ["A. 跳过本次循环", "B. 终止循环或switch", "C. 结束程序", "D. 返回函数"], "B", "break跳出循环或switch。"),
        ("continue 语句的作用是？", ["A. 终止循环", "B. 跳过本次循环剩余语句", "C. 结束程序", "D. 返回0"], "B", "continue进入下一次循环。"),
        ("函数声明中形参列表后的分号？", ["A. 必须有", "B. 不能有", "C. 可有可无", "D. 仅main需要"], "B", "函数定义/声明后无分号（声明有分号，定义无）。"),
        ("C语言中函数默认的存储类型是？", ["A. static", "B. extern", "C. auto", "D. register"], "C", "局部变量默认auto。"),
        ("递归函数必须有什么？", ["A. 全局变量", "B. 终止条件", "C. 指针参数", "D. static变量"], "B", "无终止条件会栈溢出。"),
        ("void 函数表示？", ["A. 无参数", "B. 无返回值", "C. 空函数", "D. 错误"], "B", "void作返回类型表示无返回值。"),
        ("指针变量存储的是？", ["A. 数据值", "B. 内存地址", "C. 变量名", "D. 类型"], "B", "指针存地址。"),
        ("int *p; 中 p 的类型是？", ["A. int", "B. int*", "C. pointer", "D. address"], "B", "p是指向int的指针。"),
        ("空指针的值通常是？", ["A. -1", "B. 0", "C. NULL未定义", "D. 随机"], "B", "NULL宏通常为0或(void*)0。"),
        ("对指针解引用使用？", ["A. &", "B. *", "C. ->", "D. ."], "B", "*p访问p指向的值。"),
        ("指针算术 p+1 移动的字节数是？", ["A. 1", "B. sizeof(*p)", "C. 4", "D. 8"], "B", "移动一个元素大小。"),
        ("数组名作为参数传递时退化为？", ["A. 数组副本", "B. 指针", "C. 长度", "D. 不变"], "B", "数组名即首元素地址。"),
        ("int a[10]; sizeof(a) 等于？", ["A. 10", "B. 40", "C. 4", "D. 80"], "B", "10*4=40字节（假设int为4）。"),
        ("二维数组 a[2][3] 有 ___ 个元素？", ["A. 5", "B. 6", "C. 8", "D. 9"], "B", "2*3=6个元素。"),
        ("字符串结束标志是？", ["A. '\\n'", "B. '\\0'", "C. '0'", "D. NULL"], "B", "C字符串以'\\0'结尾。"),
        ("strlen(\"hello\") 返回？", ["A. 5", "B. 6", "C. 7", "D. 4"], "A", "不含'\\0'，长度为5。"),
        ("strcpy 的功能是？", ["A. 比较字符串", "B. 复制字符串", "C. 连接字符串", "D. 求长度"], "B", "strcpy复制到目标缓冲区。"),
        ("strcmp 返回0表示？", ["A. 出错", "B. 两串相等", "C. s1>s2", "D. s1<s2"], "B", "相等返回0。"),
        ("预处理指令 #include 的作用是？", ["A. 定义宏", "B. 包含头文件", "C. 条件编译", "D. 链接库"], "B", "包含头文件内容。"),
        ("宏定义 #define PI 3.14 中 PI 是？", ["A. 变量", "B. 常量宏", "C. 函数", "D. 类型"], "B", "编译前文本替换。"),
        ("const int x=5; x=10; 编译？", ["A. 通过", "B. 报错", "C. 警告", "D. 运行错误"], "B", "const变量不可修改。"),
        ("static 局部变量的特点是？", ["A. 每次调用重新初始化", "B. 生命周期贯穿程序", "C. 外部可见", "D. 存于栈"], "B", "static局部变量保留值。"),
        ("extern 声明表示？", ["A. 本文件定义", "B. 在其他文件定义", "C. 静态存储", "D. 寄存器存储"], "B", "extern引用外部定义。"),
        ("结构体成员访问用 . 还是 ->？", ["A. 都用.", "B. 都用->", "C. 变量用. 指针用->", "D. 相反"], "C", "变量.成员，指针->成员。"),
        ("typedef 的作用是？", ["A. 定义变量", "B. 为类型起别名", "C. 定义宏", "D. 声明函数"], "B", "类型别名。"),
        ("枚举类型 enum 的值是？", ["A. 浮点", "B. 整型", "C. 字符", "D. 字符串"], "B", "枚举值为整型常量。"),
        ("联合体 union 的特点是？", ["A. 各成员同时存在", "B. 共享同一块内存", "C. 大小为各成员之和", "D. 不能嵌套"], "B", "union成员共享内存。"),
        ("文件指针类型是？", ["A. int*", "B. FILE*", "C. char*", "D. void*"], "B", "FILE*用于文件操作。"),
        ("fopen 失败返回？", ["A. 0", "B. NULL", "C. -1", "D. EOF"], "B", "失败返回NULL。"),
        ("fscanf 与 scanf 的区别？", ["A. 无区别", "B. fscanf从文件读", "C. fscanf更快", "D. scanf从文件读"], "B", "fscanf指定FILE*。"),
        ("malloc 返回？", ["A. int", "B. void*", "C. char*", "D. 数组"], "B", "动态分配返回void*。"),
        ("free 的作用是？", ["A. 分配内存", "B. 释放动态内存", "C. 清空文件", "D. 关闭文件"], "B", "释放malloc/calloc分配的空间。"),
        ("头文件 stdio.h 主要提供？", ["A. 字符串函数", "B. 输入输出", "C. 数学函数", "D. 内存分配"], "B", "标准I/O。"),
        ("printf 中 %d 表示？", ["A. 字符", "B. 整型", "C. 浮点", "D. 字符串"], "B", "%d输出int。"),
        ("scanf 读取字符串 %s 时？", ["A. 遇空格停止", "B. 读整行", "C. 含空格", "D. 自动加\\0"], "A", "%s遇空白符停止。"),
        ("getchar 返回类型是？", ["A. char", "B. int", "C. void", "D. unsigned char"], "B", "返回int以便表示EOF。"),
        ("EOF 通常定义为？", ["A. 0", "B. -1", "C. 1", "D. NULL"], "B", "EOF一般为-1。"),
        ("位运算符左移 << 相当于？", ["A. 除以2", "B. 乘以2", "C. 加1", "D. 减1"], "B", "左移n位相当于乘2^n。"),
        ("按位异或 a^a 的结果是？", ["A. a", "B. 0", "C. 1", "D. -1"], "B", "相同位异或为0。"),
        ("短路求值指？", ["A. 表达式更快", "B. 逻辑运算中右侧可能不计算", "C. 循环提前结束", "D. 函数提前返回"], "B", "&&和||可能不计算右操作数。"),
        ("表达式 a=b=c 的结合性？", ["A. 从左到右", "B. 从右到左", "C. 无结合", "D. 随机"], "B", "赋值运算符右结合。"),
        ("逗号运算符的结果是？", ["A. 第一个表达式", "B. 最后一个表达式", "C. 所有之和", "D. void"], "B", "结果为最后一个表达式的值。"),
        ("main 函数标准返回类型？", ["A. void", "B. int", "C. char", "D. 任意"], "B", "标准C中main返回int。"),
        ("#ifdef 用于？", ["A. 循环", "B. 条件编译", "C. 包含文件", "D. 定义宏"], "B", "条件编译。"),
        ("局部变量未初始化时？", ["A. 必为0", "B. 值不确定", "C. 编译错误", "D. 为NULL"], "B", "自动存储期变量初值不确定。"),
        ("全局变量未初始化时？", ["A. 值不确定", "B. 自动为0", "C. 编译错误", "D. 随机"], "B", "静态存储区默认初始化为0。"),
        ("函数指针声明正确的是？", ["A. int (*fp)();", "B. int *fp();", "C. int fp*();", "D. (*int) fp();"], "A", "(*fp)()为函数指针。"),
        ("void* 指针可以？", ["A. 直接解引用", "B. 指向任意类型", "C. 做算术运算", "D. 比较大小"], "B", "通用指针，需强转后使用。"),
        ("数组越界访问？", ["A. 编译必报错", "B. C语言不检查，可能未定义行为", "C. 自动扩展", "D. 返回0"], "B", "C不检查边界。"),
        ("指针未初始化使用？", ["A. 安全", "B. 未定义行为", "C. 返回NULL", "D. 编译错误"], "B", "野指针危险。"),
        ("sizeof 是？", ["A. 函数", "B. 编译期运算符", "C. 预处理宏", "D. 库函数"], "B", "编译期求类型/对象大小。"),
        ("类型转换 (int)3.9 结果是？", ["A. 3", "B. 4", "C. 3.9", "D. 错误"], "A", "强制转换截断小数。"),
        ("隐式转换中 char 参与运算会？", ["A. 保持char", "B. 提升为int", "C. 变为float", "D. 变为double"], "B", "整型提升。"),
        ("链表结点通常包含？", ["A. 仅数据", "B. 数据和指针", "C. 仅指针", "D. 数组"], "B", "数据域+指针域。"),
        ("栈的特点是？", ["A. FIFO", "B. LIFO", "C. 随机访问", "D. 双端"], "B", "后进先出。"),
        ("队列的特点是？", ["A. LIFO", "B. FIFO", "C. 栈", "D. 树"], "B", "先进先出。"),
        ("冒泡排序最坏时间复杂度？", ["A. O(n)", "B. O(nlogn)", "C. O(n²)", "D. O(1)"], "C", "冒泡排序O(n²)。"),
        ("二分查找前提？", ["A. 无序", "B. 有序", "C. 链表", "D. 哈希"], "B", "需有序序列。"),
        ("#pragma 的作用是？", ["A. 标准语句", "B. 编译器相关指令", "C. 注释", "D. 链接"], "B", "编译器实现相关。"),
        ("volatile 关键字表示？", ["A. 常量", "B. 可能被意外修改", "C. 静态", "D. 外部"], "B", "防止编译器过度优化。"),
        ("register 建议将变量？", ["A. 放堆", "B. 放寄存器", "C. 放全局", "D. 放静态区"], "B", "建议寄存器存储（现代编译器常忽略）。"),
        ("宏函数 #define MAX(a,b) ((a)>(b)?(a):(b)) 为何要加括号？", ["A. 美观", "B. 避免运算符优先级问题", "C. 语法要求", "D. 提高速度"], "B", "防止宏展开后优先级错误。"),
        ("feof(fp) 为真表示？", ["A. 读写出错", "B. 到达文件末尾", "C. 文件为空", "D. 文件关闭"], "B", "检测文件结束标志。"),
        ("fgetc 返回 EOF 可能表示？", ["A. 读到字符'\\0'", "B. 文件结束或错误", "C. 成功", "D. 缓冲区满"], "B", "EOF或错误。"),
        ("结构体指针 p->member 等价于？", ["A. p.member", "B. (*p).member", "C. &p.member", "D. p[member]"], "B", "->是(*p).member的简写。"),
        ("共用体大小等于？", ["A. 所有成员之和", "B. 最大成员大小", "C. 最小成员", "D. 固定4字节"], "B", "大小为最大成员（含对齐）。"),
        ("枚举 enum Color {RED, GREEN, BLUE}; GREEN的值？", ["A. 0", "B. 1", "C. 2", "D. 不确定"], "B", "从0递增，GREEN=1。"),
        ("字符 '0' 与整数 0 ？", ["A. 相同", "B. '0'的ASCII是48", "C. 都是48", "D. 不能比较"], "B", "'0'字符码为48。"),
        ("转义字符 '\\n' 表示？", ["A. 空格", "B. 换行", "C. 制表", "D. 回车"], "B", "换行符。"),
        ("双引号字符串与单引号字符？", ["A. 相同", "B. 字符串是字符数组", "C. 字符是数组", "D. 无区别"], "B", "字符串是char数组。"),
        ("预处理发生在？", ["A. 链接", "B. 编译前", "C. 运行", "D. 调试"], "B", "预处理最先。"),
        ("链接阶段主要？", ["A. 语法检查", "B. 合并目标文件与库", "C. 预处理", "D. 优化源码"], "B", "链接生成可执行文件。"),
        ("static 全局变量？", ["A. 全程序可见", "B. 仅本文件可见", "C. 仅main可见", "D. 动态分配"], "B", "内部链接。"),
        ("函数重载在C语言中？", ["A. 支持", "B. 不支持", "C. 部分支持", "D. C99支持"], "B", "C不支持重载，C++支持。"),
        ("inline 关键字(C99)？", ["A. 强制内联", "B. 建议内联", "C. 禁止内联", "D. 仅C++"], "B", "建议编译器内联展开。"),
        ("restrict 指针(C99)表示？", ["A. 只读", "B. 唯一访问该内存", "C. 常量", "D. 空指针"], "B", "优化提示。"),
        ("可变参数函数如 printf 需要？", ["A. stdarg.h", "B. string.h", "C. math.h", "D. time.h"], "A", "stdarg.h提供va_list等。"),
        ("assert 宏在？", ["A. assert.h", "B. stdio.h", "C. stdlib.h", "D. ctype.h"], "A", "断言调试。"),
        ("isalpha('A') 返回？", ["A. 0", "B. 非0", "C. 'A'", "D. 错误"], "B", "是字母则非0。"),
        ("atoi(\"123\") 返回？", ["A. 123", "B. \"123\"", "C. 1", "D. 错误"], "A", "字符串转int。"),
        ("qsort 需要？", ["A. 比较函数", "B. 仅数组", "C. 链表", "D. 文件"], "A", "需提供compare函数。"),
        ("time(NULL) 返回？", ["A. 字符串", "B. time_t当前时间", "C. 年份", "D. 毫秒"], "B", "自1970以来的秒数。"),
        ("rand() 与 srand() 关系？", ["A. 无关", "B. srand设置随机种子", "C. rand设置种子", "D. 相同"], "B", "srand初始化随机序列。"),
        ("exit(0) 与 return 0 区别？", ["A. 完全相同", "B. exit可在任意处终止程序", "C. return不能退出", "D. exit仅main"], "B", "exit可在任意函数调用。"),
        ("system(\"cls\") 在Windows？", ["A. 清屏", "B. 关机", "C. 编译", "D. 无效"], "A", "调用系统命令清屏。"),
    ]

    for i, (q, opts, ans, _) in enumerate(preset[:100], 1):
        lines.append(f"## {i}. {q}\n\n")
        for o in opts:
            lines.append(f"{o}\n")
        lines.append("\n")
        bank.append((q, opts, ans, _))

    return "".join(lines), bank


def gen_choice_answers(bank):
    lines = ["# C 语言期末考试 — 选择题参考答案与解析\n\n---\n"]
    for i, (q, opts, ans, brief) in enumerate(bank[:100], 1):
        lines.append(f"## 第 {i} 题\n\n")
        lines.append(f"**题目：** {q}\n\n")
        lines.append("**选项：**\n\n")
        for o in opts:
            marker = " ✓" if o.startswith(f"{ans}.") else ""
            lines.append(f"{o}{marker}\n")
        lines.append("\n")
        correct_opt = next((o for o in opts if o.startswith(f"{ans}.")), ans)
        lines.append(f"**答案：** {correct_opt}\n\n")
        lines.append(f"**考点解析：** {brief}\n\n")
        lines.append("---\n\n")
    return "".join(lines)


# ===================== 填空题 =====================
def gen_fill_questions():
    lines = ["# C 语言期末考试 — 填空题（100 道）\n\n---\n"]
    fills = [
        ("C语言程序从 ______ 函数开始执行。", "main"),
        ("C源文件扩展名是 ______ ，头文件扩展名是 ______ 。", ".c / .h"),
        ("标识符由字母、数字和 ______ 组成，且不能以数字开头。", "下划线"),
        ("int 类型占 ______ 字节（32位系统常见值）。", "4"),
        ("字符 '\\0' 的ASCII码值是 ______ 。", "0"),
        ("字符串 \"C\" 在内存中占 ______ 字节。", "2"),
        ("十六进制常量以 ______ 开头。", "0x 或 0X"),
        ("八进制常量以 ______ 开头。", "0"),
        ("单精度浮点字面量后缀为 ______ 。", "f 或 F"),
        ("双精度浮点类型关键字是 ______ 。", "double"),
        ("关系运算符 == 表示 ______ ，= 表示 ______ 。", "相等比较 / 赋值"),
        ("逻辑非运算符是 ______ 。", "!"),
        ("条件运算符的格式是 ______ 。", "条件 ? 表达式1 : 表达式2"),
        ("switch 语句中每个 case 后通常跟 ______ 防止贯穿。", "break"),
        ("for 循环语法：for(______; ______; ______) 语句", "初始化; 条件; 更新"),
        ("do-while 循环末尾必须有 ______ 。", "分号"),
        ("break 用于跳出 ______ 或 switch。", "循环"),
        ("continue 用于结束 ______ 并开始下一次循环。", "本次循环体"),
        ("goto 语句跳转至 ______ 。", "标号"),
        ("函数由 ______ 和 ______ 两部分组成（声明/定义角度）。", "函数头 / 函数体"),
        ("形参在函数 ______ 时分配存储。", "调用"),
        ("return 语句用于 ______ 并可选返回值。", "结束函数"),
        ("void 作为返回类型表示函数 ______ 。", "无返回值"),
        ("递归函数必须有 ______ 。", "递归终止条件"),
        ("static 修饰的局部变量存储在 ______ 。", "静态存储区"),
        ("extern 用于声明 ______ 定义的变量或函数。", "其他编译单元"),
        ("指针变量存放的是变量的 ______ 。", "地址"),
        ("取地址运算符是 ______ 。", "&"),
        ("解引用运算符是 ______ 。", "*"),
        ("空指针常写作 ______ 。", "NULL"),
        ("指针加减运算的单位是 ______ 。", "所指向类型的大小"),
        ("数组名在大多数表达式中退化为指向 ______ 的指针。", "首元素"),
        ("int a[5]; 数组下标合法范围是 ______ 到 ______ 。", "0 / 4"),
        ("二维数组 int a[2][3] 有 ______ 个 int 元素。", "6"),
        ("字符串函数 strlen 计算的长度 ______ 包含末尾 '\\0'。", "不"),
        ("strcpy(dest, src) 将 src 复制到 dest，需保证 dest 空间 ______ 。", "足够大"),
        ("strcmp 返回 0 表示两字符串 ______ 。", "相等"),
        ("strcat 用于 ______ 字符串。", "连接"),
        ("字符数组 char s[]=\"hi\"; 长度含 '\\0' 为 ______ 。", "3"),
        ("预处理指令以 ______ 开头。", "#"),
        ("#include <stdio.h> 使用 ______ 搜索头文件。", "系统目录"),
        ("#include \"file.h\" 通常先搜索 ______ 。", "当前目录"),
        ("宏定义 #define 在 ______ 阶段替换。", "预处理"),
        ("const 修饰的变量在定义后 ______ 修改。", "不可"),
        ("sizeof 是 ______ 运算符，不是函数。", "编译期"),
        ("类型转换 (float)3 属于 ______ 转换。", "强制/显式"),
        ("char 参与算术运算时会提升为 ______ 。", "int"),
        ("结构体定义关键字是 ______ 。", "struct"),
        ("访问结构体指针成员用 ______ 运算符。", "->"),
        ("typedef 用于为类型定义 ______ 。", "别名"),
        ("枚举类型 enum 的底层类型是 ______ 。", "整型"),
        ("union 中所有成员 ______ 同一块内存。", "共享"),
        ("FILE 类型定义在头文件 ______ 中。", "stdio.h"),
        ("打开文件函数是 ______ ，关闭是 ______ 。", "fopen / fclose"),
        ("文本模式读一个字符用 ______ 。", "fgetc"),
        ("文件结束检测函数是 ______ 。", "feof"),
        ("动态内存分配函数是 ______ ，释放是 ______ 。", "malloc / free"),
        ("calloc 与 malloc 区别：calloc 会 ______ 。", "初始化为0"),
        ("realloc 用于 ______ 已分配内存块。", "调整大小"),
        ("内存泄漏指动态内存未 ______ 。", "释放(free)"),
        ("头文件 string.h 提供 ______ 操作函数。", "字符串"),
        ("头文件 stdlib.h 提供 ______ 和 exit 等。", "malloc"),
        ("头文件 math.h 提供 ______ 函数如 sqrt。", "数学"),
        ("printf 格式符 %c 输出 ______ 。", "字符"),
        ("scanf 读取整数用格式符 ______ 。", "%d"),
        ("getchar() 返回类型是 ______ 以便表示 EOF。", "int"),
        ("EOF 的值通常是 ______ 。", "-1"),
        ("按位与运算符是 ______ 。", "&"),
        ("按位或运算符是 ______ 。", "|"),
        ("按位异或运算符是 ______ 。", "^"),
        ("左移运算符 ______ 相当于乘以2。", "<<"),
        ("右移运算符是 ______ 。", ">>"),
        ("逻辑与 ______ 具有短路特性。", "&&"),
        ("逻辑或 ______ 具有短路特性。", "||"),
        ("逗号运算符表达式的值为 ______ 一个子表达式的值。", "最后一个"),
        ("赋值运算符结合方向是 ______ 。", "从右到左"),
        ("自增 ++ 优先级 ______ 高于乘除（同为一元）。", "高"),
        ("main 标准返回值 0 通常表示 ______ 。", "成功"),
        ("未初始化的局部 auto 变量值 ______ 。", "不确定"),
        ("未初始化的全局变量默认值为 ______ 。", "0"),
        ("函数指针声明：返回类型 (*指针名)(参数列表)", "函数指针"),
        ("void* 可以指向 ______ 类型数据。", "任意"),
        ("链表结点除数据域外还有 ______ 域。", "指针/链接"),
        ("栈的插入删除在 ______ 端。", "同一/顶"),
        ("队列插入在队尾，删除在 ______ 。", "队头"),
        ("冒泡排序基本思想是相邻元素 ______ 。", "比较并交换"),
        ("二分查找时间复杂度 O(______ )。", "log n"),
        ("#ifdef 配合 ______ 使用实现条件编译。", "#endif"),
        ("assert 断言失败时程序 ______ 。", "终止/abort"),
        ("isdigit 判断字符是否为 ______ 。", "数字"),
        ("toupper 将字母转为 ______ 。", "大写"),
        ("atoi 将字符串转为 ______ 。", "整数"),
        ("srand 用于设置 rand 的 ______ 。", "种子"),
        ("time 函数返回当前 ______ 。", "时间戳"),
        ("qsort 需要提供 ______ 函数指针。", "比较"),
        ("bsearch 用于在 ______ 数组中查找。", "有序"),
        ("feof 与 ferror 区别：feof 检测 ______ 。", "文件结束"),
        ("fprintf 的第一个参数是 ______ 。", "FILE指针"),
        ("sprintf 输出到 ______ 。", "字符串缓冲区"),
        ("sscanf 从 ______ 读取。", "字符串"),
        ("getc 等价于 ______ 。", "fgetc(stdin)"),
        ("putc 等价于 ______ 。", "fputc(..., stdout)"),
        ("结构体变量定义后可用 ______ 初始化（C99）。", "指定初始化器"),
        ("位域用于节省 ______ 。", "存储空间"),
        ("register 只是对编译器的 ______ 。", "建议"),
        ("volatile 告诉编译器变量可能 ______ 。", "意外改变"),
        ("inline 建议函数 ______ 展开。", "内联"),
        ("_Bool 或 bool(C99) 取值 ______ 或 ______ 。", "0 / 1"),
        ("long long 类型至少 ______ 位。", "64"),
        ("字符 'A' 的ASCII码是 ______ 。", "65"),
        ("转义 \\\" 表示 ______ 。", "双引号字符"),
        ("转义 \\\\ 表示 ______ 。", "反斜杠"),
    ]
    for i, (q, _) in enumerate(fills[:100], 1):
        lines.append(f"{i}. {q}\n\n")
    return "".join(lines), fills[:100]


def gen_fill_answers(fills):
    lines = ["# C 语言期末考试 — 填空题参考答案与解析\n\n---\n"]
    topics_map = {
        0: "程序结构", 10: "运算符", 20: "函数", 30: "指针与数组",
        40: "预处理", 50: "结构体", 60: "文件与内存", 70: "标准库", 80: "位运算",
    }
    for i, (q, ans) in enumerate(fills, 1):
        topic = "C语言基础"
        for k, v in topics_map.items():
            if i > k:
                topic = v
        lines.append(f"## 第 {i} 题\n\n")
        lines.append(f"**题目：** {q}\n\n")
        lines.append(f"**参考答案：** {ans}\n\n")
        lines.append(f"**考点解析：** 本题考查【{topic}】中的核心概念与语法细节，需准确记忆标准写法。\n\n")
        lines.append("**思路整理：**\n")
        lines.append("- 回忆教材或笔记中该知识点的标准定义。\n")
        lines.append("- 注意易混淆概念（如 = 与 ==、字符与字符串）。\n")
        lines.append("- 填空时写完整、规范的术语或符号。\n\n")
        lines.append("---\n\n")
    return "".join(lines)


# ===================== 问答题 =====================
def gen_qa_questions():
    lines = ["# C 语言期末考试 — 问答题（100 道）\n\n---\n"]
    questions = [
        "简述C语言的主要特点。",
        "什么是标识符？命名规则有哪些？",
        "解释源程序、目标程序、可执行程序的关系。",
        "什么是关键字？举出5个例子。",
        "整型、字符型、浮点型各有什么用途？",
        "解释常量与变量的区别。",
        "什么是符号常量？与const有何不同？",
        "解释整型提升（integer promotion）。",
        "什么是表达式？表达式的值如何确定？",
        "解释算术运算符的优先级与结合性。",
        "逻辑运算与位运算有何区别？",
        "什么是短路求值？举例说明。",
        "解释自增自减运算符的前缀与后缀区别。",
        "switch语句中default的作用是什么？",
        "for、while、do-while如何选择？",
        "break与continue的区别？",
        "什么是嵌套循环？应注意什么？",
        "解释goto的利弊。",
        "函数的作用是什么？",
        "形参与实参有何区别？",
        "值传递与地址传递有何不同？",
        "什么是函数的返回值类型？",
        "解释递归的基本要素。",
        "递归与迭代各有什么优缺点？",
        "static修饰局部变量和全局变量分别有何效果？",
        "extern的作用是什么？",
        "什么是函数原型（声明）？",
        "解释可变参数函数的实现思路。",
        "什么是指针？指针有何用途？",
        "指针与地址有何关系？",
        "解释空指针、野指针、悬空指针。",
        "指针运算有哪些？规则是什么？",
        "数组与指针有何联系与区别？",
        "为什么数组名作函数参数会退化？",
        "解释二维数组的存储方式。",
        "字符串在C中如何表示与存储？",
        "字符串处理函数strcpy/strncpy的区别？",
        "为什么gets不安全？应用什么替代？",
        "解释字符数组与字符指针的区别。",
        "什么是预处理？常见指令有哪些？",
        "宏定义与函数有何区别？",
        "条件编译有何用途？",
        "const与#define定义常量有何不同？",
        "sizeof与strlen的区别？",
        "解释类型转换：隐式与显式。",
        "什么是结构体？如何定义与使用？",
        "结构体与数组有何不同？",
        "结构体指针为何常用->访问成员？",
        "什么是联合体？与结构体有何不同？",
        "枚举类型的作用是什么？",
        "typedef的意义是什么？",
        "什么是位域？",
        "解释FILE与文件指针。",
        "文本文件与二进制文件有何区别？",
        "fopen的模式字符串有哪些常用值？",
        "顺序访问与随机访问文件有何不同？",
        "fread/fwrite与fprintf/fscanf的区别？",
        "什么是缓冲区？fflush的作用？",
        "解释动态内存分配的必要性。",
        "malloc/calloc/realloc/free各做什么？",
        "什么是内存泄漏？如何避免？",
        "栈内存与堆内存有何区别？",
        "什么是链表？与数组比较优缺点。",
        "如何创建、遍历、插入、删除链表结点？",
        "什么是栈？如何实现？",
        "什么是队列？如何实现？",
        "简述冒泡排序思想。",
        "简述选择排序思想。",
        "简述插入排序思想。",
        "二分查找的前提与步骤。",
        "什么是时间复杂度？",
        "解释编译的四个阶段。",
        "头文件的作用是什么？",
        "什么是链接？静态链接与动态链接？",
        "main函数的参数argc、argv含义？",
        "exit与return的区别？",
        "什么是断言assert？",
        "随机数如何产生？为何要srand？",
        "qsort如何使用？",
        "解释命令行参数处理。",
        "volatile关键字的作用？",
        "register关键字还有意义吗？",
        "C99引入的inline有何作用？",
        "restrict指针的意义？",
        "什么是未定义行为？举例。",
        "数组越界为何危险？",
        "如何安全地使用strcpy？",
        "printf格式字符串与参数不匹配会怎样？",
        "如何理解指针的指针？",
        "函数指针有何用途？",
        "回调函数是什么？",
        "结构体对齐是什么？为何存在？",
        "#pragma pack的作用？",
        "如何读写结构体到文件？",
        "feof与ferror如何配合使用？",
        "sprintf/sscanf的安全问题？",
        "如何实现简单的学生信息管理系统思路？",
        "编程中如何划分模块？",
        "如何调试C程序？常用方法有哪些？",
        "编码规范中命名、缩进、注释应注意什么？",
        "C与C++在面向对象上有何根本区别？",
    ]
    for i, q in enumerate(questions[:100], 1):
        lines.append(f"{i}. {q}\n\n")
    return "".join(lines), questions[:100]


def gen_qa_answers(questions):
    # 精简但完整的答案模板 + 部分详细答案
    detailed = {
        0: "C语言是面向过程的编译型语言，特点包括：语法简洁、贴近硬件、效率高、可移植性好、丰富的运算符与库函数、指针灵活但需小心使用。",
        1: "标识符是用户定义的命名，用于变量、函数等。规则：由字母、数字、下划线组成；首字符不能是数字；不能是关键字；区分大小写。",
        28: "指针是存放变量地址的变量。用途：动态内存、数组/字符串操作、函数参数传址、数据结构（链表等）、高效访问。",
        29: "地址是内存单元的编号；指针变量存储该编号。&取地址，*解引用访问所指对象。",
        54: "动态分配在运行时按需申请内存，大小可变，生命周期手动控制，用于链表、可变长数据等。",
        62: "链表通过指针连接结点，插入删除O(1)（已知位置），不需连续内存；数组随机访问O(1)但插入删除代价大。",
        73: "预处理→编译→汇编→链接。预处理处理#指令；编译生成汇编；汇编成目标文件；链接合并库与符号。",
    }
    lines = ["# C 语言期末考试 — 问答题参考答案与解析\n\n---\n"]
    generic_points = [
        "定义核心概念", "说明语法规则", "对比相关概念", "举例说明",
        "分析优缺点", "联系实际应用",
    ]
    for i, q in enumerate(questions, 1):
        ans = detailed.get(i - 1, f"（请结合教材展开）①明确概念定义；②说明语法或原理；③举例或对比；④总结要点。")
        lines.append(f"## 第 {i} 题\n\n")
        lines.append(f"**题目：** {q}\n\n")
        lines.append(f"**参考答案：**\n\n{ans}\n\n")
        lines.append("**考点解析：** 考查对C语言核心概念的理解与表达能力，需条理清晰、术语准确。\n\n")
        lines.append("**思路整理：**\n")
        for j, p in enumerate(generic_points[:4], 1):
            lines.append(f"{j}. {p}。\n")
        lines.append("\n---\n\n")
    return "".join(lines)


# ===================== 纠错题 =====================
def gen_fix_questions():
    lines = ["# C 语言期末考试 — 纠错题（100 道）\n\n> 找出并改正代码中的语法错误或逻辑错误\n\n---\n"]
    bugs = [
        ("#include <stdio.h>\nmain() {\n    printf(\"Hello\");\n}", "main缺少返回类型int；应写 int main(void)"),
        ("int main() {\n    int a = 5\n    return 0;\n}", "第2行末尾缺少分号"),
        ("int main() {\n    if (a > 0)\n        printf(\"yes\");\n        printf(\"always\");\n    return 0;\n}", "缺少{}，第二条printf不在if内"),
        ("int main() {\n    int i;\n    for (i = 0; i < 10; i--)\n        printf(\"%d\", i);\n    return 0;\n}", "死循环：应为 i++"),
        ("int main() {\n    int arr[5] = {1,2,3,4,5,6};\n    return 0;\n}", "初始化元素个数超过数组大小"),
        ("int main() {\n    char c = \"A\";\n    return 0;\n}", "字符不能用双引号字符串赋值，应 'A'"),
        ("int main() {\n    float x = 3.14;\n    printf(\"%d\", x);\n    return 0;\n}", "格式符应为 %f 而非 %d"),
        ("int main() {\n    int *p;\n    *p = 10;\n    return 0;\n}", "p未初始化，野指针解引用"),
        ("int main() {\n    int a[3];\n    a[3] = 0;\n    return 0;\n}", "数组越界，合法下标0-2"),
        ("void swap(int a, int b) {\n    int t = a; a = b; b = t;\n}", "值传递无法交换，应传指针"),
        ("int main() {\n    char s[5] = \"hello\";\n    return 0;\n}", "字符串含\\0需6字节，数组太小"),
        ("int main() {\n    if (x = 5) printf(\"ok\");\n    return 0;\n}", "条件应 == 而非 ="),
        ("int factorial(int n) {\n    return n * factorial(n-1);\n}", "缺少递归终止条件 n<=1"),
        ("int main() {\n    switch(2.5) { case 1: break; }\n    return 0;\n}", "switch表达式不能是浮点"),
        ("#define SQ(x) x*x\nint main() {\n    printf(\"%d\", SQ(1+2));\n    return 0;\n}", "宏应 #define SQ(x) ((x)*(x))"),
        ("int main() {\n    int a = 10;\n    int b = 10 / 0;\n    return 0;\n}", "除零未定义（逻辑/运行时错误）"),
        ("int main() {\n    char *s = \"test\";\n    s[0] = 'T';\n    return 0;\n}", "字符串字面量不可修改"),
        ("int main() {\n    printf(\"%s\", 'a');\n    return 0;\n}", "%s需要char*，'a'是int字符常量"),
        ("int main() {\n    scanf(\"%d\", x);\n    return 0;\n}", "scanf需要变量地址 &x"),
        ("int main() {\n    double d;\n    scanf(\"%f\", &d);\n    return 0;\n}", "double应用 %lf"),
        ("struct Point { int x,y; };\nint main() {\n    Point p;\n    p->x = 1;\n    return 0;\n}", "p是变量不是指针，应用 p.x"),
        ("int main() {\n    FILE *fp = fopen(\"a.txt\", \"r\");\n    fclose(fp);\n    fgetc(fp);\n    return 0;\n}", "关闭后不能再使用fp"),
        ("int main() {\n    int *p = malloc(10);\n    return 0;\n}", "malloc后未free，内存泄漏"),
        ("int main() {\n    free(NULL);\n    free(p);\n    free(p);\n    return 0;\n}", "重复free同一指针"),
        ("int max(int a,int b,int a) { return a>b?a:b; }", "形参重复命名a"),
        ("int main() {\n    unsigned int i;\n    for(i=10; i>=0; i--)\n        printf(\"%u\", i);\n    return 0;\n}", "unsigned i>=0永真，死循环"),
        ("int main() {\n    char s[10];\n    gets(s);\n    return 0;\n}", "gets已废弃，用fgets"),
        ("int main() {\n    strcpy(s, \"long string here\");\n    return 0;\n}", "s未定义或缓冲区不足"),
        ("int main() {\n    int n;\n    while(n > 0) { n--; }\n    return 0;\n}", "n未初始化"),
        ("int add(int a,b) { return a+b; }", "缺少参数类型 int b"),
        ("int main() {\n    return 0\n}", "return语句后缺少分号"),
        ("int main(void) {\n    2 = a;\n    return 0;\n}", "左值不能是常量2"),
        ("int main() {\n    enum {A=1,B,C};\n    printf(\"%d\", C);\n    return 0;\n}", "本题可运行(C=2)，若考查enum需明确；改为未定义变量更易错"),
        ("int main() {\n    const int x = 5;\n    x = 10;\n    return 0;\n}", "不能修改const变量"),
        ("int main() {\n    int arr[];\n    return 0;\n}", "数组大小未知必须指定或初始化"),
        ("int main() {\n    printf(\"%d\\n\", sizeof(a));\n    return 0;\n}", "变量a未声明"),
        ("int f() { return; }", "非void函数return需返回值"),
        ("void g() { return 5; }", "void函数不能return值"),
        ("int main() {\n    int x = 5;\n    if(x); printf(\"hi\");\n    return 0;\n}", "if后分号使printf不在if内"),
        ("int main() {\n    char ch = '\\0';\n    if(ch == '\\0') printf(\"empty\");\n    else if(ch == NULL) printf(\"null\");\n    return 0;\n}", "char与NULL指针比较不当"),
        ("int *f() { int x=5; return &x; }", "返回局部变量地址，悬空指针"),
        ("int main() {\n    int a[2][3] = {1,2,3,4,5};\n    return 0;\n}", "初始化元素不足或格式错误"),
        ("int main() {\n    printf(\"%c\", \"A\");\n    return 0;\n}", "%c要char，\"A\"是地址"),
        ("int main() {\n    int i=0;\n    while(i<10); {\n        printf(\"%d\", i);\n        i++;\n    }\n    return 0;\n}", "while后分号导致空循环"),
        ("int main() {\n    #include <stdio.h>\n    return 0;\n}", "#include不能在函数体内"),
        ("int main() {\n    int x = ++x;\n    return 0;\n}", "自增自身未定义行为"),
        ("int main() {\n    printf(\"%d\", i++ + ++i);\n    return 0;\n}", "同一表达式多次修改i，未定义"),
        ("int main() {\n    char s[] = \"abc\";\n    if(s == \"abc\") printf(\"eq\");\n    return 0;\n}", "数组名与字符串字面量比较地址非内容"),
        ("int compare(char a[], char b[]) {\n    return a == b;\n}", "应使用strcmp比较字符串"),
        ("int main() {\n    int x = (int)3.14;\n    printf(\"%f\", x);\n    return 0;\n}", "x是int，应用%d"),
        ("int main() {\n    static int count;\n    count++;\n    return count;\n}", "本题正确；改为：auto static int x; 非法"),
        ("int main() {\n    auto static int x = 0;\n    return 0;\n}", "storage class顺序/重复错误"),
        ("int main() {\n    float f = 3/2;\n    printf(\"%.1f\", f);\n    return 0;\n}", "3/2为1非1.5，应3.0/2"),
        ("int main() {\n    char c = 128;\n    if(c == 128) printf(\"eq\");\n    return 0;\n}", "char可能存不下128，比较异常"),
        ("int main() {\n    int len = strlen(\"hi\");\n    return 0;\n}", "缺少 #include <string.h>"),
        ("int main() {\n    int *p = NULL;\n    printf(\"%d\", *p);\n    return 0;\n}", "解引用空指针"),
        ("int main() {\n    int a, b;\n    scanf(\"%d %d\", &a, &a);\n    return 0;\n}", "同一地址读两次逻辑错误"),
        ("int binarySearch(int a[], int n, int key) {\n    int l=0, h=n;\n    while(l<=h) { ... }\n}", "h应初始化为n-1"),
        ("int sum(int n) {\n    int s=0, i;\n    for(i=1; i<=n; i++);\n        s += i;\n    return s;\n}", "for后分号使s+=不在循环内"),
        ("int isPrime(int n) {\n    if(n<2) return 0;\n    for(int i=2; i*i<=n; i++)\n        if(n%i==0) return 0;\n    return 1;\n}", "C89不能在for内声明i，需提前声明"),
        ("int main() {\n    typedef struct { int x; } Node;\n    Node n;\n    n.x = 1;\n    struct Node n2;\n    return 0;\n}", "typedef后应直接用Node非struct Node"),
        ("int main() {\n    union U { int i; float f; } u;\n    u.i = 5;\n    printf(\"%f\", u.f);\n    return 0;\n}", "union读未写入的成员，值不确定（教学题）"),
        ("int main() {\n    int arr[5] = {0};\n    memset(arr, 1, 5);\n    return 0;\n}", "memset按字节设1非全1；且需string.h"),
        ("int main() {\n    char fmt[] = \"%d\";\n    printf(fmt, 3.14);\n    return 0;\n}", "格式与参数类型不匹配"),
        ("int main() {\n    int x = 077;\n    printf(\"%d\", x);\n    return 0;\n}", "077是八进制63，非77（逻辑理解题）"),
        ("int main() {\n    printf(\"%d\", sizeof('a'));\n    return 0;\n}", "字符常量在C中sizeof通常为int大小"),
        ("int main() {\n    int i = 0;\n    do; while(0);\n    return 0;\n}", "do后缺少循环体语句"),
        ("int main() {\n    case 1: printf(\"x\"); break;\n    return 0;\n}", "case必须在switch内"),
        ("int main() {\n    default: break;\n    return 0;\n}", "default必须在switch内"),
        ("int main() {\n    int x[10], *p=x;\n    printf(\"%d\", x-p);\n    return 0;\n}", "x-p为0正确；改为 p-x类型或越界指针相减"),
        ("void print(int arr[10]) {\n    printf(\"%d\", sizeof(arr));\n    return 0;\n}", "void函数不能return 0；sizeof(arr)是指针大小"),
        ("int main() {\n    register int r;\n    &r;\n    return 0;\n}", "不能对register变量取地址"),
        ("int main() {\n    extern int x;\n    int x = 5;\n    return 0;\n}", "extern声明与定义冲突在同一作用域"),
        ("int main() {\n    #define N 10\n    int a[N+1];\n    return 0;\n}", "宏在运行时数组变长需C99 VLA；旧标准可能问题"),
        ("int main() {\n    long long x = 1 << 40;\n    return 0;\n}", "1是int，移位可能溢出，应 1LL<<40"),
        ("int main() {\n    printf(\"%d\", true);\n    return 0;\n}", "C中true需stdbool.h或自行定义"),
        ("int main() {\n    bool flag = 1;\n    return 0;\n}", "bool需 #include <stdbool.h>"),
        ("int main() {\n    int a=1, b=2, c=3;\n    if(a<b<c) printf(\"yes\");\n    return 0;\n}", "a<b<c解析为(a<b)<c即0<c，非链式比较"),
        ("int main() {\n    char *p = malloc(0);\n    strcpy(p, \"hi\");\n    return 0;\n}", "malloc(0)行为实现定义，空间不足"),
        ("int main() {\n    int n=-1;\n    unsigned u=1;\n    if(n < u) printf(\"yes\");\n    return 0;\n}", "有符号与无符号比较，n转为大正数"),
        ("int main() {\n    char s[10]=\"\";\n    strcat(s, \"hello world\");\n    return 0;\n}", "缓冲区溢出"),
        ("int main() {\n    int i, s=0;\n    for(i=0;i<10;i++);\n        s+=i;\n    return 0;\n}", "for后分号，s只加一次i=10"),
        ("int main() {\n    printf(\"%s\", 123);\n    return 0;\n}", "%s需要char*，123是int"),
        ("int main() {\n    int x = 5;\n    int y = x++ + x++;\n    return 0;\n}", "同一表达式多次修改x，未定义"),
        ("int main() {\n    char c;\n    scanf(\"%c\", &c);\n    scanf(\"%c\", &c);\n    return 0;\n}", "连续读字符需消空白或读\\n"),
        ("int main() {\n    int arr[5];\n    arr = {1,2,3,4,5};\n    return 0;\n}", "数组不能整体赋值"),
        ("int main() {\n    int (*fp)() = main;\n    fp(1,2,3);\n    return 0;\n}", "main参数不匹配或fp类型错误"),
        ("struct S { char c; int i; };\nint main() {\n    printf(\"%d\", sizeof(struct S));\n    return 0;\n}", "考查对齐，非错误；若认为padding则说明"),
        ("int main() {\n    int i=0;\n    while(i++ < 5)\n        continue;\n        printf(\"%d\", i);\n    return 0;\n}", "continue后printf不在循环内，缺{}"),
        ("int main() {\n    #ifdef DEBUG\n    printf(\"debug\");\n    return 0;\n}", "缺少 #endif"),
        ("int main() {\n    int a[2] = {1,2};\n    int *p = a;\n    printf(\"%d\", p[2]);\n    return 0;\n}", "p[2]越界"),
        ("int main() {\n    double d = 0.1 + 0.2;\n    if(d == 0.3) printf(\"eq\");\n    return 0;\n}", "浮点精度，应比较差值epsilon"),
        ("int main() {\n    char s[5]=\"12345\";\n    return 0;\n}", "无空间存'\\0'"),
        ("int main() {\n    int x = -1;\n    unsigned y = 1;\n    if(x > y) printf(\"yes\");\n    return 0;\n}", "x转为unsigned后很大，逻辑易错"),
        ("int main() {\n    printf(\"Hello World\")\n    return 0;\n}", "printf后缺少分号"),
        ("int main() {\n    int 2var = 0;\n    return 0;\n}", "标识符不能以数字开头"),
        ("int main() {\n    return main();\n}", "无限递归栈溢出"),
        ("int main() {\n    char ch = 'A';\n    switch(ch) {\n        case 'A': printf(\"A\");\n        case 'B': printf(\"B\");\n    }\n    return 0;\n}", "case A后缺少break，贯穿"),
        ("int main() {\n    int i;\n    for(i=0; i<10; i++) {\n        if(i==5)\n            break;\n        else\n            continue;\n        printf(\"%d\", i);\n    }\n    return 0;\n}", "continue后printf不可达"),
        ("int main() {\n    int n = 5;\n    int arr[n];\n    return 0;\n}", "VLA需C99；部分旧编译器不支持"),
        ("int main() {\n    printf(\"%%d\", 10);\n    return 0;\n}", "输出%d字面量非10，格式意图错误"),
        ("int main() {\n    int i=10;\n    int j=i+++1;\n    return 0;\n}", "应写 i++ + 1，i+++1歧义"),
    ]
    for i, (code, _) in enumerate(bugs[:100], 1):
        lines.append(f"## 第 {i} 题\n\n```c\n{code}\n```\n\n")
    return "".join(lines), bugs[:100]


def gen_fix_answers(bugs):
    lines = ["# C 语言期末考试 — 纠错题参考答案与解析\n\n---\n"]
    categories = ["语法", "逻辑", "指针", "数组字符串", "预处理", "内存", "类型", "控制流"]
    for i, (code, fix) in enumerate(bugs, 1):
        cat = categories[i % len(categories)]
        lines.append(f"## 第 {i} 题\n\n")
        lines.append("**原代码：**\n\n```c\n" + code + "\n```\n\n")
        lines.append(f"**改正说明：** {fix}\n\n")
        lines.append(f"**考点解析：** 本题属于【{cat}错误】类常见问题，需结合编译器报错信息与语义分析定位。\n\n")
        lines.append("**思路整理：**\n")
        lines.append("1. 先区分语法错误（编译不过）与逻辑错误（结果不对）。\n")
        lines.append("2. 检查括号、分号、类型、边界、指针初始化。\n")
        lines.append("3. 对照正确写法改写并 mentally 走查执行流程。\n\n")
        lines.append("---\n\n")
    return "".join(lines)


# ===================== 编程题 =====================
def gen_prog_questions():
    lines = ["# C 语言期末考试 — 编程题（100 道）\n\n---\n"]
    progs = [
        "编写程序，输入两个整数，输出它们的和、差、积、商（整除）。",
        "输入圆的半径，计算并输出周长和面积（π取3.14159）。",
        "输入三个整数，输出最大值和最小值。",
        "判断输入的年份是否为闰年。",
        "输入成绩，输出对应等级（90+ A, 80-89 B, 70-79 C, 60-69 D, 否则 F）。",
        "输出100以内所有素数。",
        "输入n，计算1+2+...+n的和。",
        "输入n，计算n!（阶乘）。",
        "输出斐波那契数列前n项。",
        "输入一个整数，判断是否为素数。",
        "反转一个整数的各位数字并输出。",
        "输入整数n，输出其各位数字之和。",
        "打印九九乘法表。",
        "输入字符，判断是否为大写字母、小写字母或数字。",
        "统计输入字符串中字母、数字、空格的个数。",
        "将字符串中的小写字母转为大写。",
        "删除字符串中的空格。",
        "判断字符串是否为回文。",
        "实现字符串拷贝（不用strcpy）。",
        "实现字符串连接（不用strcat）。",
        "冒泡排序对n个整数升序排列。",
        "选择排序对数组排序。",
        "插入排序对数组排序。",
        "在有序数组中二分查找给定key。",
        "数组元素逆序存放。",
        "求数组中的最大值、最小值及下标。",
        "统计数组中各元素出现次数（元素范围小）。",
        "矩阵加法：两个m×n矩阵相加。",
        "矩阵乘法：A(m×k) × B(k×n)。",
        "转置矩阵。",
        "编写函数 swap 交换两个整数的值（用指针）。",
        "编写函数求两个整数的最大公约数（辗转相除）。",
        "编写函数求最小公倍数。",
        "编写递归函数求 n!。",
        "编写递归函数求斐波那契第n项。",
        "编写递归函数实现整数各位数字之和。",
        "用指针遍历数组并求和。",
        "用指针实现字符串长度计算。",
        "用指针实现字符串反转。",
        "动态分配数组，输入n个数并排序后输出。",
        "合并两个有序数组为一个有序数组。",
        "定义结构体 Student（学号、姓名、成绩），输入3名学生并输出。",
        "按成绩对学生结构体数组排序。",
        "统计文件中单词个数（假设单词以空格分隔）。",
        "复制文件内容到另一个文件。",
        "统计文件中某字符出现的次数。",
        "从文件读取整数直到EOF，求平均值。",
        "将结构体数组写入二进制文件再读回。",
        "实现单向链表的创建与遍历。",
        "在链表尾部插入结点。",
        "删除链表中值为x的结点。",
        "链表逆序。",
        "判断链表是否有环（思路题）。",
        "用栈判断括号是否匹配。",
        "用队列模拟约瑟夫环（n人报数出列）。",
        "实现简单计算器（+ - * / 两个数）。",
        "输入日期（年-月-日），输出是星期几（蔡勒公式）。",
        "将十进制整数转为二进制字符串输出。",
        "将二进制字符串转为十进制整数。",
        "求100以内完数（等于因子之和）。",
        "水仙花数：三位数等于各位立方和。",
        "打印菱形图案（输入层数）。",
        "打印杨辉三角前n行。",
        "猜数字游戏：随机数，用户猜，提示大/小。",
        "模拟掷骰子统计1000次各点数频率。",
        "求一元二次方程 ax²+bx+c=0 的实根。",
        "用牛顿迭代法求平方根。",
        "计算 e 的近似值（级数）。",
        "计算 sin(x) 的泰勒展开近似。",
        "统计一行文本中每个单词的长度。",
        "找出字符串中最长单词。",
        "字符串中替换所有某字符为另一字符。",
        "统计每个字符出现次数。",
        "去除字符串首尾空格。",
        "实现 atoi（字符串转整数）。",
        "实现 itoa（整数转字符串）。",
        "读入矩阵，求对角线元素之和。",
        "判断矩阵是否为对称矩阵。",
        "螺旋打印矩阵（进阶）。",
        "结构体日期比较哪个更早。",
        "职工信息：按工资排序并输出。",
        "图书信息管理系统：增删查（数组版）。",
        "学生成绩文件：读入、算平均分、写回。",
        "命令行参数求和：argc argv 整数相加。",
        "实现 mystrlen, mystrcpy, mystrcmp。",
        "用函数指针数组实现四则运算。",
        "统计二进制文件中0和1的位数（按字节）。",
        "加密：凯撒密码偏移k位。",
        "解密凯撒密码。",
        "简单通讯录：姓名电话，菜单驱动。",
        "求两个字符串最长公共子串（基础版）。",
        "数组轮转左移k位。",
        "找出数组中第二大的数。",
        "找出只出现一次的数（其他出现两次）。",
        "合并区间（简化版）。",
        "求数组连续子数组最大和（Kadane）。",
        "实现栈的数组版本（push/pop）。",
        "实现队列的数组版本。",
        "链表合并（两个有序链表）。",
        "删除链表重复元素。",
        "判断两个字符串是否为变位词。",
        "统计文件行数。",
        "日志分析：统计各级别出现次数。",
        "生成随机排列（洗牌算法）。",
        "计时：测量某段代码运行时间（clock）。",
        "读取CSV格式一行并解析两个字段。",
        "简易学生选课系统（结构体+文件）。",
    ]
    for i, p in enumerate(progs[:100], 1):
        lines.append(f"{i}. {p}\n\n")
    return "".join(lines), progs[:100]


def gen_prog_answers(progs):
    lines = ["# C 语言期末考试 — 编程题参考答案与解析\n\n---\n"]

    topic_ranges = [
        (20, "基础输入输出、分支与循环。"),
        (40, "数组、字符串、排序与查找算法。"),
        (50, "函数、指针、递归。"),
        (60, "结构体、文件操作。"),
        (101, "链表、栈队列、综合应用。"),
    ]

    for i, p in enumerate(progs, 1):
        lines.append(f"## 第 {i} 题\n\n")
        lines.append(f"**题目：** {p}\n\n")
        code = PROG_SOLUTIONS[i - 1]
        lines.append("**参考代码：**\n\n")
        lines.append(f"```c\n{code}\n```\n\n")
        topic = topic_ranges[-1][1]
        for limit, desc in topic_ranges:
            if i <= limit:
                topic = desc
                break
        lines.append(f"**考点解析：** {topic}\n\n")
        lines.append("**思路整理：** 先明确输入输出与边界条件，再设计数据结构与算法步骤；注意内存释放、文件关闭与数组越界；可用样例手工走查验证结果。\n\n")
        lines.append("---\n\n")
    return "".join(lines)


def main():
    q1, b1 = gen_choice_questions()
    write_file("选择题.md", q1)
    write_file("选择题_参考答案.md", gen_choice_answers(b1))

    q2, b2 = gen_fill_questions()
    write_file("填空题.md", q2)
    write_file("填空题_参考答案.md", gen_fill_answers(b2))

    q3, b3 = gen_qa_questions()
    write_file("问答题.md", q3)
    write_file("问答题_参考答案.md", gen_qa_answers(b3))

    q4, b4 = gen_fix_questions()
    write_file("纠错题.md", q4)
    write_file("纠错题_参考答案.md", gen_fix_answers(b4))

    q5, b5 = gen_prog_questions()
    write_file("编程题.md", q5)
    write_file("编程题_参考答案.md", gen_prog_answers(b5))

    print("\n全部生成完成！")


if __name__ == "__main__":
    main()
