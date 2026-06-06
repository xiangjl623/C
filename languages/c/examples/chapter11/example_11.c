#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];
    // strcpy(buffer, "Hello, World!");  // 閿欒锛佺紦鍐插尯婧㈠嚭
    
    // 瀹夊叏鍋氭硶
    strncpy(buffer, "Hello, World!", sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
    
    return 0;
}
