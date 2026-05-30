#include <stdio.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // 鏂瑰紡1锛氶€愪釜鎴愬憳鍒濆鍖?    struct Person p1;
    strcpy(p1.name, "寮犱笁");
    p1.age = 25;
    p1.height = 1.75f;
    
    // 鏂瑰紡2锛氫娇鐢ㄥ垵濮嬪寲鍒楄〃
    struct Person p2 = {"鏉庡洓", 30, 1.80f};
    
    // 鏂瑰紡3锛氭寚瀹氭垚鍛樺垵濮嬪寲锛圕99鏍囧噯锛?    struct Person p3 = {
        .name = "鐜嬩簲",
        .height = 1.72f,
        .age = 28
    };
    
    return 0;
}
