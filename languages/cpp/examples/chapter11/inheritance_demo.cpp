#include <iostream>
#include <string>

class Person {
protected:
    std::string name;

public:
    Person(const std::string& n) : name(n) {}
    void showName() const { std::cout << name << std::endl; }
};

class Student : public Person {
    std::string studentId;

public:
    Student(const std::string& n, const std::string& id)
        : Person(n), studentId(id) {}

    void showInfo() const {
        showName();
        std::cout << "学号：" << studentId << std::endl;
    }
};

int main() {
    Student s("李四", "2024001");
    s.showInfo();
    return 0;
}
