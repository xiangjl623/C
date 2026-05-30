#include <stdio.h>

void my_strcpy(char *dest, const char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';  // 娣诲姞瀛楃涓茬粨鏉熺
}

int main() {
    char src[] = "Hello, World!";
    char dest[20];
    
    my_strcpy(dest, src);
    printf("澶嶅埗缁撴灉锛?s\n", dest);
    
    return 0;
}
