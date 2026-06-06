#include <stdio.h>

int main() {
    int x = 5;
    
    // 涓嶈鍦ㄥ悓涓€涓〃杈惧紡涓娆′慨鏀瑰悓涓€涓彉閲?    int result = x++ + ++x;  // 琛屼负鏈畾涔夛紒
    
    printf("x = %d, result = %d\n", x, result);
    
    return 0;
}
