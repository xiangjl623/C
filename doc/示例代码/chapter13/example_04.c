#include <stdio.h>

int main() {
    FILE *fp;
    char ch;
    
    // 鍐欏叆鏂囦欢
    fp = fopen("chars.txt", "w");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    for (ch = 'A'; ch <= 'Z'; ch++) {
        fputc(ch, fp);
    }
    fclose(fp);
    
    // 璇诲彇鏂囦欢
    fp = fopen("chars.txt", "r");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    while ((ch = fgetc(fp)) != EOF) {
        printf("%c ", ch);
    }
    printf("\n");
    fclose(fp);
    
    return 0;
}
