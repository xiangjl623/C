#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int len = sizeof(arr) / sizeof(arr[0]);  // 璁＄畻鏁扮粍闀垮害
    
    // 浣跨敤for寰幆閬嶅巻
    printf("鏁扮粍鍏冪礌锛?);
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 浣跨敤while寰幆閬嶅巻
    printf("鏁扮粍鍏冪礌锛?);
    int j = 0;
    while (j < len) {
        printf("%d ", arr[j]);
        j++;
    }
    printf("\n");
    
    return 0;
}
