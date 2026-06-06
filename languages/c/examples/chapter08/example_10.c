#include <stdio.h>

int main() {
    // 鏂瑰紡1锛氬瓧绗︽暟缁勫舰寮?    char str1[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    
    // 鏂瑰紡2锛氬瓧绗︿覆瀛楅潰閲忥紙鎺ㄨ崘锛?    char str2[] = "Hello";
    
    // 鏂瑰紡3锛氬瓧绗︽寚閽?    char *str3 = "Hello";
    
    printf("str1: %s\n", str1);
    printf("str2: %s\n", str2);
    printf("str3: %s\n", str3);
    
    return 0;
}
