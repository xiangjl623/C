#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    free(p);
    // free(p);  // 閿欒锛侀噸澶嶉噴鏀句細瀵艰嚧鏈畾涔夎涓?    
    return 0;
}
