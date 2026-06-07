#include <iostream>

int main() {
    std::cout << "g++ 编译示例" << std::endl;
    std::cout << "编译命令：g++ -std=c++17 -Wall example_02.cpp -o out" << std::endl;

    int x = 10, y = 20;
    std::cout << x << " + " << y << " = " << x + y << std::endl;

    return 0;
}
