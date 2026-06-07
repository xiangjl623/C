#include <iostream>

template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << maximum(3, 5) << std::endl;
    std::cout << maximum(3.14, 2.71) << std::endl;
    return 0;
}
