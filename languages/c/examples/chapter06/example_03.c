#include <stdio.h>

int main() {
    int score;
    
    printf("璇疯緭鍏ヤ綘鐨勬垚缁╋細");
    scanf("%d", &score);
    
    if (score >= 90) {
        printf("浼樼锛乗n");
    } else if (score >= 80) {
        printf("鑹ソ锛乗n");
    } else if (score >= 70) {
        printf("涓瓑锛乗n");
    } else if (score >= 60) {
        printf("鍙婃牸锛乗n");
    } else {
        printf("涓嶅強鏍硷紒\n");
    }
    
    return 0;
}
