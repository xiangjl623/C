#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int len = strlen(str);
    int start = 0;
    int end = len - 1;
    
    while (start < end) {
        // 浜ゆ崲瀛楃
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        
        start++;
        end--;
    }
}

int main() {
    char str[] = "Hello, World!";
    
    printf("鍘熷瓧绗︿覆锛?s\n", str);
    
    reverseString(str);
    
    printf("鍙嶈浆鍚庯細%s\n", str);
    
    return 0;
}
