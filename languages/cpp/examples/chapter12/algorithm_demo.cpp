#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> vec = {5, 2, 8, 1, 9};

    std::sort(vec.begin(), vec.end());
    for (int v : vec) std::cout << v << " ";
    std::cout << std::endl;

    auto it = std::find(vec.begin(), vec.end(), 8);
    if (it != vec.end())
        std::cout << "找到 8" << std::endl;

    return 0;
}
