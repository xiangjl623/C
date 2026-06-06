#include <stdio.h>

int global_var;           // 鍦?bss娈碉紙鏈垵濮嬪寲锛?int global_init = 100;    // 鍦?data娈碉紙宸插垵濮嬪寲锛?
int main() {
    int local_var;        // 鍦ㄦ爤涓?    static int static_var; // 鍦?bss娈?    static int static_init = 200; // 鍦?data娈?    int *heap_var = (int *)malloc(sizeof(int)); // 鍦ㄥ爢涓?    
    printf("鍏ㄥ眬鍙橀噺锛堟湭鍒濆鍖栵級: %p\n", &global_var);
    printf("鍏ㄥ眬鍙橀噺锛堝凡鍒濆鍖栵級: %p\n", &global_init);
    printf("闈欐€佸彉閲忥紙鏈垵濮嬪寲锛? %p\n", &static_var);
    printf("闈欐€佸彉閲忥紙宸插垵濮嬪寲锛? %p\n", &static_init);
    printf("灞€閮ㄥ彉閲? %p\n", &local_var);
    printf("鍫嗗彉閲? %p\n", heap_var);
    
    free(heap_var);
    return 0;
}
