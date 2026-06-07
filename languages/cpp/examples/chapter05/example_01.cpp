#include <iostream>

int main() {
    int a = 10, b = 3;
    std::cout << "a + b = " << a + b << std::endl;
    std::cout << "a / b = " << a / b << std::endl;
    std::cout << "浮点除法 = " << static_cast<double>(a) / b << std::endl;
    return 0;
}
