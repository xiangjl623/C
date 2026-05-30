#include <stdio.h>
#include <stdlib.h>

void badFunc() {
    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    // 蹇樿閲婃斁锛侀€犳垚鍐呭瓨娉勬紡
}

int main() {
    for (int i = 0; i < 1000000; i++) {
        badFunc();  // 姣忔璋冪敤閮戒細娉勬紡鍐呭瓨
    }
    return 0;
}
