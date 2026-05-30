#include <stdio.h>

int main() {
    FILE *fp;
    
    // 鎵撳紑鏂囦欢
    fp = fopen("test.txt", "w");
    
    // 妫€鏌ユ槸鍚︽垚鍔熸墦寮€
    if (fp == NULL) {
        printf("鏂囦欢鎵撳紑澶辫触锛乗n");
        perror("鍘熷洜");
        return 1;
    }
    
    printf("鏂囦欢鎵撳紑鎴愬姛锛乗n");
    
    // 鍏抽棴鏂囦欢
    fclose(fp);
    
    return 0;
}
