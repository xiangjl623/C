#include <stdio.h>

int main() {
    float num1, num2;
    char op;
    
    printf("璇疯緭鍏ヨ〃杈惧紡锛堝锛? + 5锛夛細");
    scanf("%f %c %f", &num1, &op, &num2);
    
    switch (op) {
        case '+':
            printf("%.2f + %.2f = %.2f\n", num1, num2, num1 + num2);
            break;
        case '-':
            printf("%.2f - %.2f = %.2f\n", num1, num2, num1 - num2);
            break;
        case '*':
            printf("%.2f * %.2f = %.2f\n", num1, num2, num1 * num2);
            break;
        case '/':
            if (num2 != 0) {
                printf("%.2f / %.2f = %.2f\n", num1, num2, num1 / num2);
            } else {
                printf("閿欒锛氶櫎鏁颁笉鑳戒负0\n");
            }
            break;
        default:
            printf("閿欒锛氭湭鐭ヨ繍绠楃\n");
    }
    
    return 0;
}
