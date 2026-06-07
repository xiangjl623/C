#include <iostream>

void print(int* p) {
    if (p == nullptr)
        std::cout << "空指针" << std::endl;
    else
        std::cout << "值：" << *p << std::endl;
}

int main() {
    int x = 10;
    print(&x);
    print(nullptr);
    return 0;
}
