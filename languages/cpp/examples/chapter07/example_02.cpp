#include <iostream>
#include <string>

int main() {
    std::string s = "Hello";
    for (char c : s)
        std::cout << c;
    std::cout << std::endl;
    return 0;
}
