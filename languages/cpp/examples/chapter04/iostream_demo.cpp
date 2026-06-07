#include <iostream>
#include <iomanip>

int main() {
    int age = 25;
    double height = 1.75;

    std::cout << "年龄：" << age << std::endl;
    std::cout << "身高：" << height << " 米" << std::endl;

    int a, b;
    std::cout << "请输入两个整数：";
    std::cin >> a >> b;
    std::cout << "和为：" << a + b << std::endl;

    double pi = 3.14159265;
    std::cout << std::fixed << std::setprecision(2) << "PI ≈ " << pi << std::endl;

    return 0;
}
