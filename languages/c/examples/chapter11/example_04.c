#include <stdio.h>
#include <stdlib.h>

// 灏忔暟鎹€佷复鏃朵娇鐢?鈫?浣跨敤鏍?int calculateSum(int a, int b) {
    int result = a + b;  // 鏍堜笂鍒嗛厤
    return result;
}

// 澶ф暟鎹€侀渶瑕佹寔涔呬娇鐢?鈫?浣跨敤鍫?int* createArray(int size) {
    int *arr = (int *)malloc(size * sizeof(int));  // 鍫嗕笂鍒嗛厤
    return arr;
}

int main() {
    int small = calculateSum(3, 5);  // 鏍堝彉閲?    
    int *large = createArray(10000);  // 鍫嗘暟缁?    // 浣跨敤...
    free(large);  // 蹇呴』鎵嬪姩閲婃斁
    
    return 0;
}
