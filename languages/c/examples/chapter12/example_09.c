#include <stdio.h>

// 瀹氫箟鍏辩敤浣?union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    union Data data;
    
    printf("鍏辩敤浣撳ぇ灏忥細%zu bytes\n", sizeof(data));
    
    // 浣跨敤鏁村瀷
    data.i = 100;
    printf("data.i = %d\n", data.i);
    
    // 浣跨敤娴偣鍨嬶紙浼氳鐩栦箣鍓嶇殑鍊硷級
    data.f = 3.14f;
    printf("data.f = %.2f\n", data.f);
    printf("data.i = %d\n", data.i);  // 鍊煎凡鏀瑰彉
    
    // 浣跨敤瀛楃涓?    strcpy(data.str, "Hello");
    printf("data.str = %s\n", data.str);
    printf("data.i = %d\n", data.i);  // 鍊煎凡鏀瑰彉
    
    return 0;
}
