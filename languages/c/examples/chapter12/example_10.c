#include <stdio.h>

// 浣跨敤typedef绠€鍖栫粨鏋勪綋瀹氫箟
typedef struct {
    char name[50];
    int age;
    float height;
} Person;  // Person鐜板湪鏄竴涓被鍨嬪悕

int main() {
    // 鐩存帴浣跨敤Person浣滀负绫诲瀷
    Person p = {"寮犱笁", 25, 1.75f};
    printf("濮撳悕锛?s锛屽勾榫勶細%d锛岃韩楂橈細%.2f\n", p.name, p.age, p.height);
    
    return 0;
}
