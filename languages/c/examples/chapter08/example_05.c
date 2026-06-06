#include <stdio.h>

int main() {
    int arr[] = {5, 2, 8, 1, 9, 3};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    // 1. 姹傛渶澶у€?    int max = arr[0];
    for (int i = 1; i < len; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("鏈€澶у€硷細%d\n", max);
    
    // 2. 姹傛渶灏忓€?    int min = arr[0];
    for (int i = 1; i < len; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    printf("鏈€灏忓€硷細%d\n", min);
    
    // 3. 姹傚拰
    int sum = 0;
    for (int i = 0; i < len; i++) {
        sum += arr[i];
    }
    printf("鎬诲拰锛?d\n", sum);
    
    // 4. 姹傚钩鍧囧€?    float avg = (float)sum / len;
    printf("骞冲潎鍊硷細%.2f\n", avg);
    
    return 0;
}
