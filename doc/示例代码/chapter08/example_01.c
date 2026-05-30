#include <stdio.h>

int main() {
    // 瀹氫箟涓€涓寘鍚?涓暣鏁扮殑鏁扮粍
    int scores[5];
    
    // 鍒濆鍖栨暟缁勫厓绱?    scores[0] = 85;
    scores[1] = 90;
    scores[2] = 78;
    scores[3] = 92;
    scores[4] = 88;
    
    // 璁块棶鏁扮粍鍏冪礌
    printf("绗竴涓鐢熺殑鎴愮哗锛?d\n", scores[0]);
    printf("绗笁涓鐢熺殑鎴愮哗锛?d\n", scores[2]);
    
    return 0;
}
