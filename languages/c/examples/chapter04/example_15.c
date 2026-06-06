#include <stdio.h>

#define PI 3.14159

int main() {
    float radius;
    
    printf("璇疯緭鍏ュ渾鐨勫崐寰勶細");
    scanf("%f", &radius);
    
    float circumference = 2 * PI * radius;
    float area = PI * radius * radius;
    
    printf("鍦嗙殑鍛ㄩ暱锛?.2f\n", circumference);
    printf("鍦嗙殑闈㈢Н锛?.2f\n", area);
    
    return 0;
}
