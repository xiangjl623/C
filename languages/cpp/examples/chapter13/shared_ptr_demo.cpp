#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> p1 = std::make_shared<int>(42);
    std::shared_ptr<int> p2 = p1;

    std::cout << "值：" << *p1 << std::endl;
    std::cout << "引用计数：" << p1.use_count() << std::endl;

    return 0;
}
