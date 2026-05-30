// 杩愮畻绗︿紭鍏堢骇
int priority(char op) {
    switch(op) {
        case '(': return 0;
        case '+': case '-': return 1;
        case '*': case '/': case '%': return 2;
        default: return -1;
    }
}

// 鏍堢粨鏋?typedef struct {
    double data[100];
    int top;
} Stack;
