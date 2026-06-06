#include <stdio.h>

int main() {
    FILE *fp = fopen("data.txt", "w");
    
    if (fp == NULL) {
        perror("鏂囦欢鎵撳紑澶辫触");
        return 1;
    }
    
    // 浣跨敤鏂囦欢...
    
    // 鍏抽棴鏂囦欢
    if (fclose(fp) != 0) {
        printf("鏂囦欢鍏抽棴澶辫触锛乗n");
        return 1;
    }
    
    printf("鏂囦欢鍏抽棴鎴愬姛锛乗n");
    
    return 0;
}
