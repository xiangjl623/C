#include <stdio.h>

int main() {
    FILE *fp = fopen("nonexistent.txt", "r");
    
    if (fp == NULL) {
        perror("鏃犳硶鎵撳紑鏂囦欢");
        printf("閿欒浠ｇ爜锛?d\n", ferror(fp));
        return 1;
    }
    
    // 妫€鏌ユ槸鍚﹀埌杈炬枃浠舵湯灏?    if (feof(fp)) {
        printf("宸插埌杈炬枃浠舵湯灏綷n");
    }
    
    fclose(fp);
    
    return 0;
}
