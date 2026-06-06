#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, 鍦板潃 = %p\n", i, arr[i], &arr[i]);
    }
    
    return 0;
}
