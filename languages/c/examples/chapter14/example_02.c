#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define MAX_LEN 100

typedef struct {
    double data[MAX_LEN];
    int top;
} NumStack;

typedef struct {
    char data[MAX_LEN];
    int top;
} OpStack;

// 鏁板瓧鏍堟搷浣?void numPush(NumStack *s, double val) {
    if (s->top < MAX_LEN - 1) {
        s->data[++(s->top)] = val;
    }
}

double numPop(NumStack *s) {
    if (s->top >= 0) {
        return s->data[(s->top)--];
    }
    return 0;
}

// 杩愮畻绗︽爤鎿嶄綔
void opPush(OpStack *s, char op) {
    if (s->top < MAX_LEN - 1) {
        s->data[++(s->top)] = op;
    }
}

char opPop(OpStack *s) {
    if (s->top >= 0) {
        return s->data[(s->top)--];
    }
    return '\0';
}

char opPeek(OpStack *s) {
    if (s->top >= 0) {
        return s->data[s->top];
    }
    return '\0';
}
