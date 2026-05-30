#include <stdio.h>

int global_var = 100;  // 鍏ㄥ眬鍙橀噺锛屾暣涓▼搴忛兘鍙互璁块棶

int main() {
    int local_var = 200;  // 灞€閮ㄥ彉閲忥紝浠呭湪main鍑芥暟鍐呮湁鏁?    
    printf("鍏ㄥ眬鍙橀噺: %d\n", global_var);
    printf("灞€閮ㄥ彉閲? %d\n", local_var);
    
    {
        int block_var = 300;  // 鍧楃骇鍙橀噺锛屼粎鍦ㄨ姳鎷彿鍐呮湁鏁?        printf("鍧楃骇鍙橀噺: %d\n", block_var);
    }
    // printf("鍧楃骇鍙橀噺: %d\n", block_var); // 閿欒锛乥lock_var鍦ㄦ涓嶅彲璁块棶
    
    return 0;
}
