#include <iostream>
#include <string>

class Student {
public:
    std::string name;
    int age;

    void introduce() const {
        std::cout << "我是 " << name << "，今年 " << age << " 岁" << std::endl;
    }
};

int main() {
    Student s;
    s.name = "张三";
    s.age = 20;
    s.introduce();
    return 0;
}
