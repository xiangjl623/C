#include <iostream>

int main() {
    int score = 85;
    bool passed = (score >= 60);

    if (passed)
        std::cout << "及格" << std::endl;
    else
        std::cout << "不及格" << std::endl;

    return 0;
}
