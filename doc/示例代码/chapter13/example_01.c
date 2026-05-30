#include <stdio.h>

int main() {
    // 澹版槑鏂囦欢鎸囬拡
    FILE *fp;
    
    // 鎵撳紑鏂囦欢
    fp = fopen("example.txt", "w");
    
    if (fp == NULL) {
        printf("鏂囦欢鎵撳紑澶辫触\n");
        return 1;
    }
    
    // 鍐欏叆鍐呭
    fprintf(fp, "Hello, File!\n");
    
    // 鍏抽棴鏂囦欢
    fclose(fp);
    
    return 0;
}
