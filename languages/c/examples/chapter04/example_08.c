#include <stdio.h>

void counter() {
    auto int auto_count = 0;     // 姣忔璋冪敤閮介噸鏂板垵濮嬪寲涓?
    static int static_count = 0; // 鍙垵濮嬪寲涓€娆★紝鍊间細淇濈暀
    
    auto_count++;
    static_count++;
    
    printf("auto_count: %d, static_count: %d\n", auto_count, static_count);
}

int main() {
    counter();  // auto_count: 1, static_count: 1
    counter();  // auto_count: 1, static_count: 2
    counter();  // auto_count: 1, static_count: 3
    
    return 0;
}
