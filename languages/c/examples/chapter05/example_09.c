#include <stdio.h>

int main() {
    int a = 10;
    
    a += 5;   // 绛変环浜?a = a + 5锛岀粨鏋? 15
    printf("a += 5: %d\n", a);
    
    a -= 3;   // 绛変环浜?a = a - 3锛岀粨鏋? 12
    printf("a -= 3: %d\n", a);
    
    a *= 2;   // 绛変环浜?a = a * 2锛岀粨鏋? 24
    printf("a *= 2: %d\n", a);
    
    a /= 4;   // 绛変环浜?a = a / 4锛岀粨鏋? 6
    printf("a /= 4: %d\n", a);
    
    a %= 4;   // 绛変环浜?a = a % 4锛岀粨鏋? 2
    printf("a %%= 4: %d\n", a);
    
    return 0;
}
