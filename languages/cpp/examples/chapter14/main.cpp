#include "student_manager.h"
#include <iostream>

int main() {
    StudentManager mgr;
    mgr.loadFromFile("students.txt");

    int choice;
    do {
        std::cout << "\n=== 学生管理系统 ===\n";
        std::cout << "1.添加 2.删除 3.查询 4.显示全部 5.保存 0.退出\n";
        std::cout << "选择：";
        std::cin >> choice;

        if (choice == 1) {
            Student s;
            std::cout << "姓名 学号 年龄：";
            std::cin >> s.name >> s.id >> s.age;
            mgr.addStudent(s);
            std::cout << "已添加\n";
        } else if (choice == 2) {
            std::string id;
            std::cout << "学号：";
            std::cin >> id;
            std::cout << (mgr.removeStudent(id) ? "已删除\n" : "未找到\n");
        } else if (choice == 3) {
            std::string id;
            std::cout << "学号：";
            std::cin >> id;
            if (auto* p = mgr.findById(id))
                p->display();
            else
                std::cout << "未找到\n";
        } else if (choice == 4) {
            mgr.displayAll();
        } else if (choice == 5) {
            if (mgr.saveToFile("students.txt"))
                std::cout << "已保存到 students.txt\n";
            else
                std::cout << "保存失败\n";
        }
    } while (choice != 0);

    return 0;
}
