#include <stdio.h>

int main() {
    int *p = NULL;
    // *p = 10;  // 閿欒锛佺┖鎸囬拡瑙ｅ紩鐢ㄤ細瀵艰嚧绋嬪簭宕╂簝
    
    // 姝ｇ‘鍋氭硶锛氭鏌ユ寚閽堟槸鍚︿负绌?    if (p != NULL) {
        *p = 10;
    }
    
    return 0;
}
