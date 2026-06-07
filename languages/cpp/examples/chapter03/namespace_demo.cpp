#include <iostream>

namespace Math {
    int add(int a, int b) { return a + b; }
}

namespace Utils {
    int add(int a, int b) { return a + b + 1; }
}

int main() {
    std::cout << "Math::add(1, 2) = " << Math::add(1, 2) << std::endl;
    std::cout << "Utils::add(1, 2) = " << Utils::add(1, 2) << std::endl;
    return 0;
}
