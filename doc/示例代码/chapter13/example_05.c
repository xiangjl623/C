#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[100];
    
    // 鍐欏叆瀛楃涓?    fp = fopen("strings.txt", "w");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    fputs("Hello, World!\n", fp);
    fputs("杩欐槸绗簩琛屻€俓n", fp);
    fclose(fp);
    
    // 璇诲彇瀛楃涓?    fp = fopen("strings.txt", "r");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }
    fclose(fp);
    
    return 0;
}
