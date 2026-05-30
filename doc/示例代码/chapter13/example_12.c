#include <stdio.h>

int fileExists(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp != NULL) {
        fclose(fp);
        return 1;
    }
    return 0;
}

int main() {
    if (fileExists("example.txt")) {
        printf("鏂囦欢瀛樺湪\n");
    } else {
        printf("鏂囦欢涓嶅瓨鍦╘n");
    }
    
    return 0;
}
