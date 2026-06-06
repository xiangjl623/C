#include <stdio.h>

int main() {
    char name[50];
    char address[100];
    
    // 1. 浣跨敤scanf杈撳叆锛堥亣鍒扮┖鏍煎仠姝級
    printf("璇疯緭鍏ヤ綘鐨勫鍚嶏細");
    scanf("%s", name);
    printf("浣犲ソ锛?s锛乗n", name);
    
    // 2. 浣跨敤gets杈撳叆锛堣鍙栨暣琛岋紝鍖呮嫭绌烘牸锛?    printf("璇疯緭鍏ヤ綘鐨勫湴鍧€锛?);
    // gets(address);  // 娉ㄦ剰锛歡ets宸插簾寮冿紝涓嶅畨鍏?    
    // 3. 浣跨敤fgets杈撳叆锛堟帹鑽愶級
    printf("璇疯緭鍏ヤ綘鐨勫湴鍧€锛?);
    fgets(address, sizeof(address), stdin);
    printf("浣犵殑鍦板潃锛?s", address);
    
    return 0;
}
