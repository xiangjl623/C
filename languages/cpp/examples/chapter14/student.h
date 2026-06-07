#pragma once
#include <iostream>
#include <string>

class Student {
public:
    std::string name;
    std::string id;
    int age;

    Student() : age(0) {}
    Student(const std::string& n, const std::string& i, int a)
        : name(n), id(i), age(a) {}

    void display() const {
        std::cout << "学号：" << id << " 姓名：" << name
                  << " 年龄：" << age << std::endl;
    }
};
