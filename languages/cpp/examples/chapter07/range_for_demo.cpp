#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    for (auto& v : vec)
        v *= 2;
    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    return 0;
}
