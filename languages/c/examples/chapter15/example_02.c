#include <stdio.h>

int main() {
    FILE *fp = fopen("file.txt", "r");
    if (fp == NULL) {
        perror("Failed to open file");
        return 1;
    }
    
    // 璇诲彇鎴栧啓鍏ユ搷浣?    
    fclose(fp);
    return 0;
}
