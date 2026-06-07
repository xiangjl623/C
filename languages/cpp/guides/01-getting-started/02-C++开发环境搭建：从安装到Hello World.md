
# C++开发环境搭建：从安装到Hello World

## 在 C 环境之上配置 C++

如果你已按 [C 语言开发环境搭建](../../c/guides/01-getting-started/02-C语言开发环境搭建：从安装到Hello World.md) 配置过 MinGW-w64 或 GCC，那么 **g++ 通常已经可用**——C 与 C++ 共用同一套工具链。本篇重点补充 C++ 特有的配置：g++ 编译选项、VS Code C++ 任务、以及 CMake 简介。

---

## 一、C++ 开发环境核心组件

### 1.1 与 C 环境的对比

| 组件 | C 语言 | C++ 额外/差异 |
|------|--------|---------------|
| 编译器 | gcc | **g++**（或 `gcc -x c++`） |
| 标准库 | C 标准库 | **C++ 标准库**（iostream、vector 等） |
| 构建工具 | Make | **CMake**（跨平台，推荐） |
| 编辑器 | VS Code + C/C++ 插件 | 相同，tasks.json 改用 g++ |
| 调试器 | GDB | 相同 |

### 1.2 验证 g++ 是否已安装

```bash
g++ --version
```

若已安装 MinGW-w64 或 Linux GCC，应看到类似输出：

```
g++ (MinGW.org GCC-8.2.0-5) 8.2.0
```

若未安装，请参考 [C 语言开发环境搭建](../../c/guides/01-getting-started/02-C语言开发环境搭建：从安装到Hello World.md) 安装 MinGW-w64（Windows）或 `sudo apt install g++`（Linux）。

---

## 二、Windows 环境（C++ 专项）

### 2.1 VS Code tasks.json（g++ 编译 C++）

在 C 语言配置基础上，将 `gcc` 改为 `g++`，并添加 C++ 标准：

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "g++ build",
            "type": "shell",
            "command": "g++",
            "args": [
                "-std=c++17",
                "-Wall",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": ["$gcc"]
        }
    ]
}
```

### 2.2 launch.json（调试 C++）

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - 调试活动文件",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${fileDirname}",
            "environment": [],
            "externalConsole": true,
            "preLaunchTask": "g++ build"
        }
    ]
}
```

### 2.3 安装 VS Code C++ 插件

若尚未安装，搜索并安装 **Extension Pack for C++**（Microsoft 出品），包含 IntelliSense、调试、CMake 支持。

---

## 三、macOS / Linux 环境

### 3.1 安装 g++

**macOS：**

```bash
xcode-select --install
clang++ --version   # macOS 默认使用 clang++，兼容 C++
```

**Linux（Debian/Ubuntu）：**

```bash
sudo apt update
sudo apt install g++ gdb make cmake
```

### 3.2 VS Code tasks.json（Unix 路径）

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "g++ build",
            "type": "shell",
            "command": "g++",
            "args": [
                "-std=c++17",
                "-Wall",
                "-g",
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": ["$gcc"]
        }
    ]
}
```

---

## 四、CMake 简介

当项目包含多个 `.cpp` 文件时，手写编译命令会变得繁琐。CMake 是跨平台的构建系统生成器，广泛用于 C++ 项目。

### 4.1 最小 CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.14)
project(HelloCpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(hello hello.cpp)
```

### 4.2 编译步骤

```bash
mkdir build && cd build
cmake ..
cmake --build .
./hello          # Linux/macOS
hello.exe        # Windows
```

> 入门阶段单文件程序用 `g++` 直接编译即可；多文件项目或后续实战章节会用到 CMake。

---

## 五、编写第一个 C++ 程序

### 5.1 创建 hello.cpp

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << "你好，C++！" << std::endl;
    return 0;
}
```

### 5.2 编译运行

**终端：**

```bash
g++ -std=c++17 -Wall hello.cpp -o hello
./hello
```

**VS Code：** 按 `Ctrl+Shift+B` 编译，`F5` 调试运行。

### 5.3 常用 g++ 参数

| 参数 | 作用 |
|------|------|
| `-std=c++17` | 指定 C++ 标准（推荐 C++17） |
| `-Wall` | 开启常见警告 |
| `-g` | 生成调试信息 |
| `-O2` | 优化（发布时使用） |
| `-o name` | 指定输出文件名 |

---

## 六、常见问题

### 6.1 找不到 iostream

**问题：** `fatal error: iostream: No such file or directory`

**解决：** 确认使用 `g++` 而非 `gcc` 编译 `.cpp` 文件。

### 6.2 中文乱码

**解决：** 源文件保存为 UTF-8；Windows 终端执行 `chcp 65001`。

### 6.3 C 与 C++ 混用

- `.c` 文件用 `gcc` 编译
- `.cpp` 文件用 `g++` 编译
- 链接时用 `g++` 可自动链接 C++ 标准库

---

## 七、实战练习

### 练习1：配置 C++ 编译任务

按本篇配置 VS Code 的 tasks.json，确保 `Ctrl+Shift+B` 能成功编译 `.cpp` 文件。

### 练习2：输出个人信息

```cpp
#include <iostream>

int main() {
    std::cout << "========== 个人信息 ==========" << std::endl;
    std::cout << "姓名：张三" << std::endl;
    std::cout << "学号：2024001001" << std::endl;
    std::cout << "专业：计算机科学与技术" << std::endl;
    std::cout << "语言：C++" << std::endl;
    std::cout << "==============================" << std::endl;
    return 0;
}
```

### 练习3：两数之和（C++ 版）

使用 `std::cin` 和 `std::cout` 实现两整数求和，对比 C 版本的 `scanf`/`printf`。

---

## 八、总结与延伸

### 本节重点回顾

1. C++ 与 C 共用工具链，编译器为 g++/clang++
2. VS Code 需将 tasks.json 中的 `gcc` 改为 `g++`，并添加 `-std=c++17`
3. 单文件：`g++ -std=c++17 -Wall file.cpp -o out`
4. 多文件项目推荐使用 CMake

### 下节预告

下一篇我们将学习《程序结构：头文件、命名空间与编译链接》，理解 C++ 程序的模块组织方式。

### 延伸阅读

- [C 语言开发环境搭建](../../c/guides/01-getting-started/02-C语言开发环境搭建：从安装到Hello World.md)
- [engineering/02-linux-and-shell/](../../../engineering/02-linux-and-shell/) — Linux 下的 GCC/g++ 实践

---

📌 **知识点卡片**
- C++ 编译器：g++、clang++；源文件：`.cpp`
- 推荐编译：`g++ -std=c++17 -Wall -g file.cpp -o out`
- CMake 用于多文件项目的跨平台构建
- VS Code：Extension Pack for C++ + tasks.json + launch.json

💡 **小技巧**
- 始终用 g++ 编译 .cpp，避免用 gcc 导致链接错误
- 养成 `-Wall` 习惯，尽早发现潜在问题

⚠️ **注意事项**
- C 头文件（如 `stdio.h`）在 C++ 中建议写为 `cstdio`（C++ 风格）
- 调试前必须先编译成功

---

> 如果你在配置过程中遇到问题，欢迎在评论区留言！下一篇见！
