#include <stdio.h>

int main() {
    int i = 1;
    int sum = 0;
    
    while (i <= 100) {
        sum += i;  // sum = sum + i
        i++;
    }
    
    printf("1鍒?00鐨勫拰锛?d\n", sum);
    
    return 0;
}
