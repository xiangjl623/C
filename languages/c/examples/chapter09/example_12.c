#include <stdio.h>

int global_var = 100;  // 鍏ㄥ眬鍙橀噺

void test() {
    int local_var = 200;  // 灞€閮ㄥ彉閲?    printf("鍏ㄥ眬鍙橀噺锛?d\n", global_var);
    printf("灞€閮ㄥ彉閲忥細%d\n", local_var);
}

int main() {
    printf("鍏ㄥ眬鍙橀噺锛?d\n", global_var);
    // printf("灞€閮ㄥ彉閲忥細%d\n", local_var);  // 閿欒锛佸眬閮ㄥ彉閲忎笉鍙闂?    
    test();
    
    return 0;
}
