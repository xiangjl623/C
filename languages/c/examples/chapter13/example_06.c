#include <stdio.h>

struct Student {
    char name[50];
    int age;
    float score;
};

int main() {
    struct Student s = {"寮犱笁", 25, 95.5f};
    FILE *fp;
    
    // 鍐欏叆鏍煎紡鍖栨暟鎹?    fp = fopen("student.txt", "w");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    fprintf(fp, "%s %d %.1f\n", s.name, s.age, s.score);
    fclose(fp);
    
    // 璇诲彇鏍煎紡鍖栨暟鎹?    struct Student s2;
    fp = fopen("student.txt", "r");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    fscanf(fp, "%s %d %f", s2.name, &s2.age, &s2.score);
    printf("濮撳悕锛?s锛屽勾榫勶細%d锛屾垚缁╋細%.1f\n", s2.name, s2.age, s2.score);
    fclose(fp);
    
    return 0;
}
