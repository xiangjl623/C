#include <stdio.h>

// 瀹氫箟鏃ユ湡缁撴瀯浣?struct Date {
    int year;
    int month;
    int day;
};

// 瀹氫箟瀛︾敓缁撴瀯浣擄紝鍖呭惈鏃ユ湡缁撴瀯浣?struct Student {
    char name[50];
    struct Date birthday;
    float score;
};

int main() {
    struct Student s = {
        "寮犱笁",
        {2000, 5, 15},
        95.5f
    };
    
    printf("濮撳悕锛?s\n", s.name);
    printf("鐢熸棩锛?d骞?d鏈?d鏃n", s.birthday.year, s.birthday.month, s.birthday.day);
    printf("鎴愮哗锛?.1f\n", s.score);
    
    return 0;
}
