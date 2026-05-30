#include <stdio.h>

int binarySearch(int arr[], int len, int target) {
    int left = 0;
    int right = len - 1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        
        if (arr[mid] == target) {
            return mid;  // 鎵惧埌鐩爣锛岃繑鍥炵储寮?        } else if (arr[mid] < target) {
            left = mid + 1;  // 鍦ㄥ彸鍗婇儴鍒嗘煡鎵?        } else {
            right = mid - 1;  // 鍦ㄥ乏鍗婇儴鍒嗘煡鎵?        }
    }
    
    return -1;  // 鏈壘鍒?}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    int target = 7;
    int index = binarySearch(arr, len, target);
    
    if (index != -1) {
        printf("鎵惧埌%d锛岀储寮曚负%d\n", target, index);
    } else {
        printf("鏈壘鍒?d\n", target);
    }
    
    return 0;
}
