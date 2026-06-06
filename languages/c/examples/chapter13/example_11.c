#include <stdio.h>

int main() {
    FILE *fp = fopen("example.txt", "r");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    // 璇诲彇绗竴琛?    char buffer[50];
    fgets(buffer, sizeof(buffer), fp);
    printf("绗竴琛岋細%s", buffer);
    
    // 鍥炲埌鏂囦欢寮€澶?    rewind(fp);
    
    // 鍐嶆璇诲彇绗竴琛?    fgets(buffer, sizeof(buffer), fp);
    printf("鍐嶆璇诲彇绗竴琛岋細%s", buffer);
    
    fclose(fp);
    
    return 0;
}
