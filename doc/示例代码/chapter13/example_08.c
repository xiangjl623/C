#include <stdio.h>

struct Student {
    char name[50];
    int age;
    float score;
};

int main() {
    struct Student students[3];
    
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    // 璇诲彇浜岃繘鍒舵暟鎹?    fread(students, sizeof(struct Student), 3, fp);
    fclose(fp);
    
    // 杈撳嚭鏁版嵁
    for (int i = 0; i < 3; i++) {
        printf("瀛︾敓%d锛歕n", i + 1);
        printf("  濮撳悕锛?s\n", students[i].name);
        printf("  骞撮緞锛?d\n", students[i].age);
        printf("  鎴愮哗锛?.1f\n", students[i].score);
    }
    
    return 0;
}
