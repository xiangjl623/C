#include <iostream>

class Rectangle {
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double area() const { return width * height; }
};

int main() {
    Rectangle rect(3.0, 4.0);
    std::cout << "面积：" << rect.area() << std::endl;
    return 0;
}
