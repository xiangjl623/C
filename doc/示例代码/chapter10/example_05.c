#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    // 浣跨敤鏁扮粍涓嬫爣
    printf("浣跨敤涓嬫爣閬嶅巻锛?);
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 浣跨敤鎸囬拡
    printf("浣跨敤鎸囬拡閬嶅巻锛?);
    int *p = arr;
    for (int i = 0; i < len; i++) {
        printf("%d ", *(p + i));
    }
    printf("\n");
    
    // 浣跨敤鎸囬拡绉诲姩
    printf("浣跨敤鎸囬拡绉诲姩閬嶅巻锛?);
    for (int *p = arr; p < arr + len; p++) {
        printf("%d ", *p);
    }
    printf("\n");
    
    return 0;
}
