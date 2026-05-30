#include <stdio.h>

int findMax(int arr[], int len) {
    int max = arr[0];
    for (int i = 1; i < len; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 3};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    printf("鏁扮粍鐨勬渶澶у€硷細%d\n", findMax(arr, len));
    
    return 0;
}
