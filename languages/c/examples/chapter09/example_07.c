#include <stdio.h>

void increment(int *x) {
    (*x)++;
    printf("鍑芥暟鍐咃細*x = %d\n", *x);
}

int main() {
    int num = 5;
    printf("璋冪敤鍓嶏細num = %d\n", num);
    
    increment(&num);  // 浼犻€掑湴鍧€
    
    printf("璋冪敤鍚庯細num = %d\n", num);  // num鍙樻垚6
    
    return 0;
}
