#include <stdio.h>

int main() {
    float fahrenheit;
    
    printf("璇疯緭鍏ュ崕姘忔俯搴︼細");
    scanf("%f", &fahrenheit);
    
    float celsius = (fahrenheit - 32) * 5 / 9;
    
    printf("%.1f鍗庢皬搴?= %.1f鎽勬皬搴n", fahrenheit, celsius);
    
    return 0;
}
