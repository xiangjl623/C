#include <stdio.h>

// 鏈夊弬鏁版棤杩斿洖鍊?void printMessage(char *msg) {
    printf("娑堟伅锛?s\n", msg);
}

void printNumbers(int start, int end) {
    for (int i = start; i <= end; i++) {
        printf("%d ", i);
    }
    printf("\n");
}

int main() {
    printMessage("杩欐槸涓€涓祴璇曟秷鎭?);
    printNumbers(1, 10);
    
    return 0;
}
