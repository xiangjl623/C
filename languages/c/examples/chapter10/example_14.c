#include <stdio.h>

int main() {
    int *p;  // 鏈垵濮嬪寲鐨勬寚閽堬紝鎸囧悜闅忔満鍦板潃
    // *p = 10;  // 閿欒锛侀噹鎸囬拡鍙兘瀵艰嚧鏈煡琛屼负
    
    // 姝ｇ‘鍋氭硶锛氬垵濮嬪寲鎸囬拡
    int num = 0;
    p = &num;
    *p = 10;
    
    return 0;
}
