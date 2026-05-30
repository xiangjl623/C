#include <stdio.h>

int main() {
    char str[] = "Hello";
    char *p = str;
    
    // 閬嶅巻瀛楃涓?    while (*p != '\0') {
        printf("%c ", *p);
        p++;
    }
    printf("\n");
    
    return 0;
}
