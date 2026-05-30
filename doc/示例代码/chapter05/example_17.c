#include <stdio.h>

int main() {
    int year;
    
    printf("璇疯緭鍏ュ勾浠斤細");
    scanf("%d", &year);
    
    // 闂板勾鍒ゆ柇瑙勫垯锛氳兘琚?鏁撮櫎浣嗕笉鑳借100鏁撮櫎锛屾垨鑳借400鏁撮櫎
    int is_leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    
    if (is_leap) {
        printf("%d骞存槸闂板勾\n", year);
    } else {
        printf("%d骞翠笉鏄棸骞碶n", year);
    }
    
    return 0;
}
