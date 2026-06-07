#include <iostream>
#include <string>
#include <vector>

int main() {
    auto i = 42;
    auto d = 3.14;
    auto s = std::string("hello");

    std::cout << "i=" << i << ", d=" << d << ", s=" << s << std::endl;

    std::vector<int> vec = {1, 2, 3};
    for (auto v : vec) {
        std::cout << v << " ";
    }
    std::cout << std::endl;

    return 0;
}
