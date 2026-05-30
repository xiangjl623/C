#include <stdio.h>

int main() {
    float weight, height, bmi;
    
    printf("璇疯緭鍏ヤ綋閲嶏紙kg锛夛細");
    scanf("%f", &weight);
    
    printf("璇疯緭鍏ヨ韩楂橈紙m锛夛細");
    scanf("%f", &height);
    
    bmi = weight / (height * height);
    
    printf("浣犵殑BMI鎸囨暟涓猴細%.1f\n", bmi);
    
    // 鍒ゆ柇BMI绛夌骇
    printf("BMI绛夌骇锛?);
    if (bmi < 18.5) {
        printf("鍋忕槮\n");
    } else if (bmi < 24) {
        printf("姝ｅ父\n");
    } else if (bmi < 28) {
        printf("瓒呴噸\n");
    } else {
        printf("鑲ヨ儢\n");
    }
    
    return 0;
}
