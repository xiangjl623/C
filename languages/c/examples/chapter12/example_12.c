#include <stdio.h>

// 浣跨敤浣嶅煙瀹氫箟缁撴瀯浣?struct Flags {
    unsigned int is_active : 1;   // 1浣?    unsigned int is_admin : 1;    // 1浣?    unsigned int has_access : 1;  // 1浣?    unsigned int reserved : 29;   // 29浣嶏紙鎬诲叡32浣嶏級
};

int main() {
    struct Flags f;
    printf("Flags澶у皬锛?zu bytes\n", sizeof(f));
    
    f.is_active = 1;
    f.is_admin = 0;
    f.has_access = 1;
    
    printf("is_active = %u\n", f.is_active);
    printf("is_admin = %u\n", f.is_admin);
    printf("has_access = %u\n", f.has_access);
    
    return 0;
}
