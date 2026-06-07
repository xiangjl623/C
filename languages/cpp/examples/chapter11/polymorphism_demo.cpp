#include <iostream>
#include <string>

class Animal {
public:
    virtual void speak() { std::cout << "..." << std::endl; }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    void speak() override { std::cout << "汪汪！" << std::endl; }
};

class Cat : public Animal {
public:
    void speak() override { std::cout << "喵喵！" << std::endl; }
};

int main() {
    Animal* animals[] = {new Dog(), new Cat()};
    for (auto* a : animals) {
        a->speak();
        delete a;
    }
    return 0;
}
