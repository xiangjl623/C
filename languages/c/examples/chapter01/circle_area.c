#include <stdio.h>

#define PI 3.14159

int main() {
    float radius, area;
    
    printf("请输入圆的半径：");
    scanf("%f", &radius);
    
    area = PI * radius * radius;
    printf("圆的面积为：%.2f\n", area);
    
    return 0;
}