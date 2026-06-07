#include <iostream>
#include <string>

int main() {
    std::string s1 = "Hello";
    std::string s2 = "World";
    std::string s3 = s1 + ", " + s2 + "!";

    std::cout << s3 << std::endl;
    std::cout << "长度：" << s3.length() << std::endl;

    return 0;
}
