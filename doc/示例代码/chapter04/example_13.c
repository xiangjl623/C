#include <stdio.h>

#define PI 3.14159
#define MAX_SIZE 100
#define AUTHOR "寮犱笁"

int main() {
    float radius = 5.0f;
    float area = PI * radius * radius;
    
    printf("鍦嗙殑闈㈢Н: %.2f\n", area);
    printf("鏈€澶у昂瀵? %d\n", MAX_SIZE);
    printf("浣滆€? %s\n", AUTHOR);
    
    return 0;
}
