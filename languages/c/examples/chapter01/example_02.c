#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 42;
    printf("鍙橀噺鐨勫€硷細%d\n", *ptr);
    printf("鍙橀噺鐨勫湴鍧€锛?p\n", ptr);
    free(ptr);
    return 0;
}
