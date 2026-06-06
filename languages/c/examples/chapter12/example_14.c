#include <stdio.h>

// 瀹氫箟鏋氫妇绫诲瀷
enum Weekday {
    Monday,    // 0
    Tuesday,   // 1
    Wednesday, // 2
    Thursday,  // 3
    Friday,    // 4
    Saturday,  // 5
    Sunday     // 6
};

int main() {
    enum Weekday today = Wednesday;
    
    printf("浠婂ぉ鏄槦鏈?d\n", today);
    
    // switch璇彞涓娇鐢ㄦ灇涓?    switch (today) {
        case Monday:
        case Tuesday:
        case Wednesday:
        case Thursday:
        case Friday:
            printf("宸ヤ綔鏃n");
            break;
        case Saturday:
        case Sunday:
            printf("鍛ㄦ湯\n");
            break;
    }
    
    return 0;
}
