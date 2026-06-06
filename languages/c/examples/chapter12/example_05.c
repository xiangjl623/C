#include <stdio.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person p = {"寮犱笁", 25};
    struct Person *ptr = &p;
    
    // 浣跨敤鎸囬拡璁块棶缁撴瀯浣撴垚鍛?    printf("濮撳悕锛?s\n", ptr->name);
    printf("骞撮緞锛?d\n", ptr->age);
    
    // 淇敼缁撴瀯浣撴垚鍛?    strcpy(ptr->name, "鏉庡洓");
    ptr->age = 30;
    
    printf("淇敼鍚庯細\n");
    printf("濮撳悕锛?s\n", p.name);
    printf("骞撮緞锛?d\n", p.age);
    
    return 0;
}
