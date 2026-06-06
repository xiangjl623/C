#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 42;
    printf("变量的值：%d\n", *ptr);
    printf("变量的地址：%p\n", ptr);
    free(ptr);
    return 0;
}