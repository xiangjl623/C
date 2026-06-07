#include <iostream>

enum class Menu { Add, Delete, Query, Exit };

int main() {
    Menu choice = Menu::Add;

    switch (choice) {
        case Menu::Add:    std::cout << "添加" << std::endl; break;
        case Menu::Delete: std::cout << "删除" << std::endl; break;
        case Menu::Query:  std::cout << "查询" << std::endl; break;
        case Menu::Exit:   std::cout << "退出" << std::endl; break;
    }

    return 0;
}
