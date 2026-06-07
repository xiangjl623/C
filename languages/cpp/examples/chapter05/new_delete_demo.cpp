#include <iostream>

int main() {
    int* p = new int(42);
    std::cout << *p << std::endl;
    delete p;

    int* arr = new int[5]{1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
        std::cout << arr[i] << " ";
    std::cout << std::endl;
    delete[] arr;

    return 0;
}
