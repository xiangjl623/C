#include <stdio.h>

int main() {
    float f = 3.14f;         // 鍗曠簿搴︽诞鐐癸紝f鍚庣紑琛ㄧずfloat
    double d = 3.1415926535; // 鍙岀簿搴︽诞鐐癸紝榛樿鏄痙ouble
    long double ld = 3.141592653589793238L; // 闀垮弻绮惧害
    
    printf("float: %.6f\n", f);
    printf("double: %.10f\n", d);
    printf("long double: %.15Lf\n", ld);
    
    return 0;
}
