#include <iostream>
#include <string>

void greet(const std::string& name, const std::string& prefix = "Hello") {
    std::cout << prefix << ", " << name << "!" << std::endl;
}

int main() {
    greet("Alice");
    greet("Bob", "Hi");
    return 0;
}
