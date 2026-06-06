#include <stdio.h>

struct Point {
    int x;
    int y;
};

// 鍊间紶閫?void printPoint(struct Point p) {
    printf("Point: (%d, %d)\n", p.x, p.y);
}

// 鎸囬拡浼犻€?void movePoint(struct Point *p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}

int main() {
    struct Point pt = {3, 4};
    
    printPoint(pt);
    movePoint(&pt, 2, -1);
    printPoint(pt);
    
    return 0;
}
