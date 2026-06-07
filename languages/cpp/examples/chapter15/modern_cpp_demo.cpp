#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <algorithm>

int main() {
    // C++11/14/17 特性演示
    auto vec = std::vector<int>{1, 2, 3, 4, 5};
    auto ptr = std::make_unique<int>(42);

    std::cout << "现代 C++ 特性演示：" << std::endl;
    std::cout << "unique_ptr: " << *ptr << std::endl;

    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    std::sort(vec.begin(), vec.end(), std::greater<int>());
    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    return 0;
}
