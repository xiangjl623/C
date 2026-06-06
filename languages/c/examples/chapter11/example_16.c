#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 1024

typedef struct MemoryBlock {
    struct MemoryBlock *next;
    char data[BLOCK_SIZE - sizeof(struct MemoryBlock *)];
} MemoryBlock;

typedef struct {
    MemoryBlock *head;
} MemoryPool;

MemoryPool* createMemoryPool() {
    MemoryPool *pool = (MemoryPool *)malloc(sizeof(MemoryPool));
    pool->head = NULL;
    return pool;
}

void* poolAlloc(MemoryPool *pool, size_t size) {
    if (size > BLOCK_SIZE - sizeof(MemoryBlock *)) {
        return NULL;  // 瓒呰繃鍧楀ぇ灏?    }
    
    MemoryBlock *block = (MemoryBlock *)malloc(BLOCK_SIZE);
    block->next = pool->head;
    pool->head = block;
    
    return block->data;
}

void destroyMemoryPool(MemoryPool *pool) {
    MemoryBlock *current = pool->head;
    while (current != NULL) {
        MemoryBlock *next = current->next;
        free(current);
        current = next;
    }
    free(pool);
}

int main() {
    MemoryPool *pool = createMemoryPool();
    
    char *str = (char *)poolAlloc(pool, 100);
    strcpy(str, "Hello, Memory Pool!");
    printf("%s\n", str);
    
    destroyMemoryPool(pool);
    
    return 0;
}
