#include <stdio.h>

int main() {
    int grade;
    
    printf("璇疯緭鍏ユ垚缁╃瓑绾?A-E)锛?);
    scanf("%c", &grade);
    
    switch (grade) {
        case 'A':
        case 'B':
        case 'C':
            printf("鎴愮哗鍚堟牸\n");
            break;
        case 'D':
        case 'E':
            printf("鎴愮哗涓嶅悎鏍糪n");
            break;
        default:
            printf("杈撳叆閿欒\n");
    }
    
    return 0;
}
