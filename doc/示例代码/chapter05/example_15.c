#include <stdio.h>

int main() {
    int score = 85;
    
    char grade = (score >= 90) ? 'A' :
                 (score >= 80) ? 'B' :
                 (score >= 70) ? 'C' :
                 (score >= 60) ? 'D' : 'F';
    
    printf("鎴愮哗绛夌骇: %c\n", grade);  // B
    
    return 0;
}
