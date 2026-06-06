#include <stdio.h>

void increment(int x) {
    x++;
    printf("鍑芥暟鍐咃細x = %d\n", x);
}

int main() {
    int num = 5;
    printf("璋冪敤鍓嶏細num = %d\n", num);
    
    increment(num);
    
    printf("璋冪敤鍚庯細num = %d\n", num);  // num浠嶇劧鏄?
    
    return 0;
}
