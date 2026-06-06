#include <stdio.h>

int main() {
    char c = 'A';           // 瀛楃鍨嬶紝瀹為檯瀛樺偍ASCII鐮佸€?    short s = 32767;        // 鐭暣鍨嬶紝鑼冨洿绾?32768鍒?2767
    int i = 2147483647;     // 鏁村瀷锛岃寖鍥寸害-21浜垮埌21浜?    long l = 9223372036854775807L; // 闀挎暣鍨嬶紝L鍚庣紑琛ㄧず闀挎暣鍨?    long long ll = 9223372036854775807LL; // 闀块暱鏁村瀷
    
    printf("char: %c (%d)\n", c, (int)c);      // 杈撳嚭瀛楃鍜孉SCII鐮?    printf("short: %d\n", s);
    printf("int: %d\n", i);
    printf("long: %ld\n", l);
    printf("long long: %lld\n", ll);
    
    return 0;
}
