#include <stdio.h>

int countLines(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("鏃犳硶鎵撳紑鏂囦欢");
        return -1;
    }
    
    int count = 0;
    char ch;
    
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            count++;
        }
    }
    
    // 濡傛灉鏂囦欢涓嶄互鎹㈣缁撳熬锛屾渶鍚庝竴琛屼篃绠?    if (count > 0 || !feof(fp)) {
        count++;
    }
    
    fclose(fp);
    return count;
}

int main() {
    int lines = countLines("example.txt");
    if (lines >= 0) {
        printf("鏂囦欢鍏辨湁%d琛孿n", lines);
    }
    
    return 0;
}
