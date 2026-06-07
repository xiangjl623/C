#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec;

    for (int i = 1; i <= 5; i++)
        vec.push_back(i * 10);

    std::cout << "大小：" << vec.size() << std::endl;
    for (const auto& v : vec)
        std::cout << v << " ";
    std::cout << std::endl;

    return 0;
}
