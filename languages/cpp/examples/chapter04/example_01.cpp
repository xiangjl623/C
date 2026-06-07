#include <iostream>

int main() {
    bool isReady = true;
    bool isEmpty = false;

    std::cout << std::boolalpha;
    std::cout << "isReady: " << isReady << std::endl;
    std::cout << "isEmpty: " << isEmpty << std::endl;

    int score = 85;
    bool passed = (score >= 60);
    std::cout << "passed: " << passed << std::endl;

    return 0;
}
