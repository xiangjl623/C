#include <iostream>

int main() {
    double radius;
    const double PI = 3.14159;

    std::cout << "请输入圆的半径：";
    std::cin >> radius;

    double area = PI * radius * radius;
    std::cout << "圆的面积为：" << area << std::endl;

    return 0;
}
