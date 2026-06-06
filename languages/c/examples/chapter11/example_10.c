#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    
    free(p);
    // printf("%d\n", *p);  // 閿欒锛佷娇鐢ㄥ凡閲婃斁鐨勫唴瀛?    
    return 0;
}
