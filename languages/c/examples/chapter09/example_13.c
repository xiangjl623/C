#include <stdio.h>

void counter() {
    static int count = 0;  // 闈欐€佸彉閲忥紝鍙垵濮嬪寲涓€娆?    count++;
    printf("count = %d\n", count);
}

int main() {
    counter();  // count = 1
    counter();  // count = 2
    counter();  // count = 3
    
    return 0;
}
