#include "student_manager.h"
#include <fstream>
#include <algorithm>

void StudentManager::addStudent(const Student& s) {
    students.push_back(s);
}

bool StudentManager::removeStudent(const std::string& id) {
    auto it = std::remove_if(students.begin(), students.end(),
        [&](const Student& s) { return s.id == id; });
    if (it == students.end()) return false;
    students.erase(it, students.end());
    return true;
}

Student* StudentManager::findById(const std::string& id) {
    for (auto& s : students)
        if (s.id == id) return &s;
    return nullptr;
}

void StudentManager::displayAll() const {
    if (students.empty()) {
        std::cout << "（暂无学生）" << std::endl;
        return;
    }
    for (const auto& s : students)
        s.display();
}

bool StudentManager::saveToFile(const std::string& filename) const {
    std::ofstream ofs(filename);
    if (!ofs) return false;
    for (const auto& s : students)
        ofs << s.id << " " << s.name << " " << s.age << "\n";
    return true;
}

bool StudentManager::loadFromFile(const std::string& filename) {
    std::ifstream ifs(filename);
    if (!ifs) return false;
    students.clear();
    Student s;
    while (ifs >> s.id >> s.name >> s.age)
        students.push_back(s);
    return true;
}
