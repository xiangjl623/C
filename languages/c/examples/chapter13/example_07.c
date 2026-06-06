#include <stdio.h>

struct Student {
    char name[50];
    int age;
    float score;
};

int main() {
    struct Student students[3] = {
        {"寮犱笁", 25, 95.5f},
        {"鏉庡洓", 23, 88.0f},
        {"鐜嬩簲", 24, 92.3f}
    };
    
    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    // 鍐欏叆浜岃繘鍒舵暟鎹?    fwrite(students, sizeof(struct Student), 3, fp);
    fclose(fp);
    
    printf("浜岃繘鍒舵枃浠跺啓鍏ユ垚鍔燂紒\n");
    
    return 0;
}
