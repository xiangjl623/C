#include <stdio.h>

// 鍑芥暟鍘熷瀷
int add(int a, int b);
void printHello();

int main() {
    int result = add(3, 5);
    printf("缁撴灉锛?d\n", result);
    
    printHello();
    
    return 0;
}

// 鍑芥暟瀹氫箟
int add(int a, int b) {
    return a + b;
}

void printHello() {
    printf("Hello!\n");
}
