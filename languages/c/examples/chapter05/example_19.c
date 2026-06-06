#include <stdio.h>

#define READ  1 << 0  // 0b0001
#define WRITE 1 << 1  // 0b0010
#define EXEC  1 << 2  // 0b0100

int main() {
    int permission = READ | WRITE;  // 0b0011
    
    // 娣诲姞鎵ц鏉冮檺
    permission |= EXEC;  // 0b0111
    printf("娣诲姞鎵ц鏉冮檺鍚? 0b%04b\n", permission);
    
    // 绉婚櫎鍐欐潈闄?    permission &= ~WRITE;  // 0b0101
    printf("绉婚櫎鍐欐潈闄愬悗: 0b%04b\n", permission);
    
    // 妫€鏌ユ槸鍚︽湁璇绘潈闄?    if (permission & READ) {
        printf("鏈夎鏉冮檺\n");
    }
    
    // 妫€鏌ユ槸鍚︽湁鍐欐潈闄?    if (permission & WRITE) {
        printf("鏈夊啓鏉冮檺\n");
    } else {
        printf("娌℃湁鍐欐潈闄怽n");
    }
    
    return 0;
}
