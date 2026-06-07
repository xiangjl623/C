#pragma once
#include "student.h"
#include <vector>
#include <string>

class StudentManager {
    std::vector<Student> students;

public:
    void addStudent(const Student& s);
    bool removeStudent(const std::string& id);
    Student* findById(const std::string& id);
    void displayAll() const;
    bool saveToFile(const std::string& filename) const;
    bool loadFromFile(const std::string& filename);
};
