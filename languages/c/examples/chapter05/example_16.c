#include <stdio.h>

int main() {
    int a = 10, b = 3, c = 2;
    
    // 娌℃湁鎷彿锛屾寜浼樺厛绾ц绠?    int result1 = a - b * c;  // 绛変环浜?a - (b * c) = 10 - 6 = 4
    printf("a - b * c = %d\n", result1);
    
    // 浣跨敤鎷彿鏀瑰彉浼樺厛绾?    int result2 = (a - b) * c;  // 绛変环浜?(10 - 3) * 2 = 14
    printf("(a - b) * c = %d\n", result2);
    
    // 澶嶅悎琛ㄨ揪寮?    int x = 5, y = 3;
    int result3 = x > y && x + y > 5;  // 绛変环浜?(x > y) && ((x + y) > 5)
    printf("result3 = %d\n", result3);  // 1
    
    return 0;
}
