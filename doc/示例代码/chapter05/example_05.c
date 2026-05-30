#include <stdio.h>

int main() {
    int x = 5;
    
    // 閿欒锛氫娇鐢ㄤ簡璧嬪€艰繍绠楃=鑰屼笉鏄浉绛夎繍绠楃==
    if (x = 10) {
        printf("x琚祴鍊间负10锛屾潯浠朵负鐪焅n");
    }
    
    // 姝ｇ‘锛氫娇鐢ㄧ浉绛夎繍绠楃==
    if (x == 10) {
        printf("x绛変簬10\n");
    } else {
        printf("x涓嶇瓑浜?0锛寈 = %d\n", x);
    }
    
    return 0;
}
