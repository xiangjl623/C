#include <stdio.h>

int main() {
    int year;
    
    printf("璇疯緭鍏ュ勾浠斤細");
    scanf("%d", &year);
    
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("%d骞存槸闂板勾\n", year);
    } else {
        printf("%d骞翠笉鏄棸骞碶n", year);
    }
    
    return 0;
}
