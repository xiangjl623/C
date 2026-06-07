#include <iostream>

int main() {
    int a = 10, b = 20;
    auto max = (a > b) ? a : b;
    std::cout << "最大值：" << max << std::endl;
    return 0;
}
