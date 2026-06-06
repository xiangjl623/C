#include <stdio.h>

// 瀹氫箟涓€涓绠楀钩鏂圭殑鍑芥暟
int square(int num) {
    return num * num;
}

int main() {
    int result = square(5);  // 璋冪敤鍑芥暟
    printf("5鐨勫钩鏂规槸锛?d\n", result);
    
    return 0;
}
