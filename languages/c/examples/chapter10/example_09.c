#include <stdio.h>

int main() {
    int num = 100;
    int *p = &num;      // 涓€绾ф寚閽?    int **pp = &p;      // 浜岀骇鎸囬拡
    
    printf("num = %d\n", num);
    printf("*p = %d\n", *p);
    printf("**pp = %d\n", **pp);
    
    **pp = 200;  // 閫氳繃浜岀骇鎸囬拡淇敼鍘熷鍙橀噺
    printf("淇敼鍚?num = %d\n", num);
    
    return 0;
}
