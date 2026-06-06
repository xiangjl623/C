#include <stdio.h>

int main() {
    char letter = 'A';       // 瀛樺偍瀛楃'A'
    char digit = '5';        // 瀛樺偍瀛楃'5'
    char newline = '\n';     // 杞箟瀛楃锛屾崲琛岀
    
    printf("瀛楁瘝: %c (ASCII: %d)\n", letter, letter);
    printf("鏁板瓧瀛楃: %c (ASCII: %d)\n", digit, digit);
    
    // 瀛楃杩愮畻
    char lowercase = letter + 32;  // 'A' + 32 = 'a'
    printf("灏忓啓瀛楁瘝: %c\n", lowercase);
    
    return 0;
}
