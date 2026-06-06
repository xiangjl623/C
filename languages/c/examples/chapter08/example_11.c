#include <stdio.h>

// 鑷畾涔夊瓧绗︿覆闀垮害鍑芥暟
int my_strlen(const char *str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

int main() {
    char str[] = "Hello, World!";
    
    // 浣跨敤鑷畾涔夊嚱鏁?    printf("瀛楃涓查暱搴︼細%d\n", my_strlen(str));
    
    // 浣跨敤鏍囧噯搴撳嚱鏁?    #include <string.h>
    printf("瀛楃涓查暱搴︼細%zu\n", strlen(str));
    
    return 0;
}
