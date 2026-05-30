#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello";
    char str2[20] = "World";
    char str3[40];
    
    // 1. strcpy锛氬瓧绗︿覆澶嶅埗
    strcpy(str3, str1);
    printf("strcpy: %s\n", str3);  // Hello
    
    // 2. strcat锛氬瓧绗︿覆鎷兼帴
    strcat(str1, " ");
    strcat(str1, str2);
    printf("strcat: %s\n", str1);  // Hello World
    
    // 3. strcmp锛氬瓧绗︿覆姣旇緝
    int result = strcmp("Apple", "Banana");
    printf("strcmp: %d\n", result);  // 璐熸暟锛圓pple < Banana锛?    
    // 4. strchr锛氭煡鎵惧瓧绗?    char *pos = strchr("Hello, World!", 'W');
    printf("strchr: %s\n", pos);  // World!
    
    // 5. strstr锛氭煡鎵惧瓙瀛楃涓?    char *sub = strstr("Hello, World!", "World");
    printf("strstr: %s\n", sub);  // World!
    
    return 0;
}
