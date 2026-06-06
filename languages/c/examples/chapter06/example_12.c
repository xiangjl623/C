#include <stdio.h>

int main() {
    int choice;
    
    while (1) {
        printf("\n===== 瀛︾敓鎴愮哗绠＄悊绯荤粺 =====\n");
        printf("1. 娣诲姞鎴愮哗\n");
        printf("2. 鏌ヨ鎴愮哗\n");
        printf("3. 淇敼鎴愮哗\n");
        printf("4. 鍒犻櫎鎴愮哗\n");
        printf("5. 閫€鍑虹郴缁焅n");
        printf("璇疯緭鍏ラ€夋嫨(1-5)锛?);
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("鎵ц娣诲姞鎴愮哗鍔熻兘\n");
                break;
            case 2:
                printf("鎵ц鏌ヨ鎴愮哗鍔熻兘\n");
                break;
            case 3:
                printf("鎵ц淇敼鎴愮哗鍔熻兘\n");
                break;
            case 4:
                printf("鎵ц鍒犻櫎鎴愮哗鍔熻兘\n");
                break;
            case 5:
                printf("鎰熻阿浣跨敤锛屽啀瑙侊紒\n");
                return 0;
            default:
                printf("杈撳叆閿欒锛岃閲嶆柊杈撳叆\n");
        }
    }
    
    return 0;
}
