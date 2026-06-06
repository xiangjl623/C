#include <stdio.h>

int main() {
    const float PI = 3.14159;
    const int MAX_SIZE = 100;
    
    float radius = 5.0f;
    float area = PI * radius * radius;
    
    printf("鍦嗙殑闈㈢Н: %.2f\n", area);
    
    // PI = 3.14;  // 閿欒锛乧onst鍙橀噺涓嶈兘琚慨鏀?    
    return 0;
}
