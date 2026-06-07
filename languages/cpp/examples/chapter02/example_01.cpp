#include <iostream>

int main() {
    int a, b;
    std::cout << "请输入第一个整数：";
    std::cin >> a;
    std::cout << "请输入第二个整数：";
    std::cin >> b;

    std::cout << "两数之和为：" << a + b << std::endl;
    return 0;
}
