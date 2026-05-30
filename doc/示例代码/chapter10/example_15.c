#include <stdio.h>
#include <stdlib.h>

void func() {
    int *p = (int *)malloc(sizeof(int));
    *p = 10;
    // 蹇樿閲婃斁鍐呭瓨锛?}

int main() {
    func();
    // p鎸囧悜鐨勫唴瀛樻案杩滄棤娉曢噴鏀撅紝閫犳垚鍐呭瓨娉勬紡
    
    return 0;
}
