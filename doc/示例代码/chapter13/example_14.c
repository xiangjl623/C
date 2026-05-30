#include <stdio.h>

int main() {
    FILE *source, *dest;
    char ch;
    
    source = fopen("source.txt", "r");
    if (source == NULL) {
        perror("鏃犳硶鎵撳紑婧愭枃浠?);
        return 1;
    }
    
    dest = fopen("dest.txt", "w");
    if (dest == NULL) {
        perror("鏃犳硶鎵撳紑鐩爣鏂囦欢");
        fclose(source);
        return 1;
    }
    
    // 閫愬瓧绗﹀鍒?    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, dest);
    }
    
    printf("鏂囦欢澶嶅埗鎴愬姛锛乗n");
    
    fclose(source);
    fclose(dest);
    
    return 0;
}
