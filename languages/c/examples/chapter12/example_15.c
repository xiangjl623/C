#include <stdio.h>

// 鑷畾涔夋灇涓惧€?enum Status {
    ERROR = -1,
    SUCCESS = 0,
    WARNING = 1,
    INFO = 2
};

// 甯︿綅杩愮畻鐨勬灇涓?enum Permission {
    READ = 1 << 0,   // 0001
    WRITE = 1 << 1,  // 0010
    EXECUTE = 1 << 2 // 0100
};

int main() {
    printf("ERROR = %d\n", ERROR);
    printf("SUCCESS = %d\n", SUCCESS);
    
    // 浣跨敤浣嶈繍绠楃粍鍚堟潈闄?    int permissions = READ | WRITE;
    printf("鏉冮檺缁勫悎锛?d\n", permissions);
    
    if (permissions & READ) {
        printf("鏈夎鏉冮檺\n");
    }
    
    return 0;
}
