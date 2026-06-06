#include <stdio.h>

int main() {
    int score;
    
    printf("璇疯緭鍏ヤ綘鐨勬垚缁╋細");
    scanf("%d", &score);
    
    if (score >= 60) {
        printf("鎭枩浣狅紝鍙婃牸浜嗭紒\n");
    } else {
        printf("寰堥仐鎲撅紝涓嶅強鏍笺€俓n");
    }
    
    printf("绋嬪簭缁撴潫\n");
    
    return 0;
}
