#include <stdio.h>

struct Student {
    int id;
    char name[50];
    float score;
};

int main() {
    // 瀹氫箟缁撴瀯浣撴暟缁?    struct Student students[3] = {
        {101, "寮犱笁", 95.5f},
        {102, "鏉庡洓", 88.0f},
        {103, "鐜嬩簲", 92.3f}
    };
    
    // 閬嶅巻缁撴瀯浣撴暟缁?    for (int i = 0; i < 3; i++) {
        printf("瀛︾敓%d锛歕n", i + 1);
        printf("  ID锛?d\n", students[i].id);
        printf("  濮撳悕锛?s\n", students[i].name);
        printf("  鎴愮哗锛?.1f\n", students[i].score);
    }
    
    return 0;
}
