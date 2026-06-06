#include <stdio.h>

#define PI 3.14159

int main() {
    float radius, area;
    
    printf("璇疯緭鍏ュ渾鐨勫崐寰勶細");
    scanf("%f", &radius);
    
    area = PI * radius * radius;
    printf("鍦嗙殑闈㈢Н涓猴細%.2f\n", area);
    
    return 0;
}
