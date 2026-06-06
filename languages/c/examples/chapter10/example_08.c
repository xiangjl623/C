#include <stdio.h>

int main() {
    char *names[] = {"寮犱笁", "鏉庡洓", "鐜嬩簲", "璧靛叚"};
    
    for (int i = 0; i < 4; i++) {
        printf("names[%d] = %s\n", i, names[i]);
    }
    
    return 0;
}
