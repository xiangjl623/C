#include <stdio.h>
#include <string.h>

// 瀹氫箟缁撴瀯浣?struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // 澹版槑骞跺垵濮嬪寲缁撴瀯浣撳彉閲?    struct Person p1;
    strcpy(p1.name, "寮犱笁");
    p1.age = 25;
    p1.height = 1.75f;
    
    // 璁块棶缁撴瀯浣撴垚鍛?    printf("濮撳悕锛?s\n", p1.name);
    printf("骞撮緞锛?d\n", p1.age);
    printf("韬珮锛?.2f\n", p1.height);
    
    return 0;
}
