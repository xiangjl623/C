#include <stdio.h>

int main() {
    int day;
    
    printf("璇疯緭鍏ユ槦鏈熷嚑(1-7)锛?);
    scanf("%d", &day);
    
    switch (day) {
        case 1:
            printf("鏄熸湡涓€\n");
            break;
        case 2:
            printf("鏄熸湡浜孿n");
            break;
        case 3:
            printf("鏄熸湡涓塡n");
            break;
        case 4:
            printf("鏄熸湡鍥沑n");
            break;
        case 5:
            printf("鏄熸湡浜擻n");
            break;
        case 6:
            printf("鏄熸湡鍏璡n");
            break;
        case 7:
            printf("鏄熸湡鏃n");
            break;
        default:
            printf("杈撳叆閿欒锛乗n");
    }
    
    return 0;
}
