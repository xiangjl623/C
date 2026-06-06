#include <stdio.h>

int main() {
    FILE *fp = fopen("example.txt", "w+");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    // 鍐欏叆鍐呭
    fprintf(fp, "Hello, World!");
    
    // 灏嗘枃浠舵寚閽堢Щ鍔ㄥ埌鏂囦欢寮€澶?    fseek(fp, 0, SEEK_SET);
    
    // 璇诲彇鍐呭
    char buffer[20];
    fgets(buffer, sizeof(buffer), fp);
    printf("璇诲彇鍐呭锛?s\n", buffer);
    
    // 灏嗘枃浠舵寚閽堢Щ鍔ㄥ埌绗?涓瓧绗?    fseek(fp, 6, SEEK_SET);
    fgets(buffer, sizeof(buffer), fp);
    printf("浠庣7涓瓧绗﹀紑濮嬶細%s\n", buffer);
    
    // 灏嗘枃浠舵寚閽堝悜鍓嶇Щ鍔?涓瓧绗?    fseek(fp, -5, SEEK_CUR);
    fgets(buffer, sizeof(buffer), fp);
    printf("鍚戝墠绉诲姩5涓瓧绗︼細%s\n", buffer);
    
    fclose(fp);
    
    return 0;
}
