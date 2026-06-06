#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static size_t totalAllocated = 0;
static size_t totalFreed = 0;

void* debugMalloc(size_t size, const char *file, int line) {
    void *ptr = malloc(size);
    if (ptr != NULL) {
        totalAllocated += size;
        printf("[MALLOC] %s:%d - Allocated %zu bytes at %p\n", 
               file, line, size, ptr);
    }
    return ptr;
}

void debugFree(void *ptr, const char *file, int line) {
    if (ptr != NULL) {
        // 绠€鍖栧鐞嗭細瀹為檯涓渶瑕佽褰曞垎閰嶅ぇ灏?        totalFreed += sizeof(ptr);
        printf("[FREE] %s:%d - Freed memory at %p\n", file, line, ptr);
        free(ptr);
    }
}

#define malloc(size) debugMalloc(size, __FILE__, __LINE__)
#define free(ptr) debugFree(ptr, __FILE__, __LINE__)

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    
    int *arr = (int *)malloc(5 * sizeof(int));
    
    free(p);
    free(arr);
    
    printf("Total allocated: %zu bytes\n", totalAllocated);
    printf("Total freed: %zu bytes\n", totalFreed);
    
    return 0;
}
