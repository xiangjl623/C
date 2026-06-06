#include <stdio.h>

// 涓哄熀鏈被鍨嬪垱寤哄埆鍚?typedef int Integer;
typedef float Real;

// 涓烘寚閽堢被鍨嬪垱寤哄埆鍚?typedef int* IntPtr;
typedef char* String;

// 涓烘暟缁勭被鍨嬪垱寤哄埆鍚?typedef int IntArray[10];

int main() {
    Integer num = 42;
    Real pi = 3.14f;
    String str = "Hello";
    IntArray arr = {1, 2, 3, 4, 5};
    
    printf("num = %d\n", num);
    printf("pi = %.2f\n", pi);
    printf("str = %s\n", str);
    
    return 0;
}
