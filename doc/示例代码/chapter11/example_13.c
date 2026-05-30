void func() {
    int *data = (int *)malloc(100 * sizeof(int));
    if (data == NULL) return;
    
    // 浣跨敤data...
    
    free(data);  // 纭繚閲婃斁
}
