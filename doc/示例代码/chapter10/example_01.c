#include <stdio.h>

int main() {
    int num = 42;
    int *ptr = &num;  // ptr鏄寚鍚憂um鐨勬寚閽?    
    printf("鍙橀噺num鐨勫€硷細%d\n", num);
    printf("鍙橀噺num鐨勫湴鍧€锛?p\n", &num);
    printf("鎸囬拡ptr鐨勫€硷細%p\n", ptr);
    printf("鎸囬拡ptr鎸囧悜鐨勫€硷細%d\n", *ptr);
    
    return 0;
}
