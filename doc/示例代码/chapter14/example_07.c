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

void numPush(NumStack *s, double val) {
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

int getPriority(char op) {
    switch(op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
        case '%':
            return 2;
        case '(':
            return 0;
        default:
            return -1;
    }
}

int isOperator(char ch) {
    return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%';
}

void infixToPostfix(char *infix, char *postfix) {
    OpStack opStack = {-1};
    int i = 0, j = 0;
    
    while (infix[i] != '\0') {
        if (infix[i] == ' ') {
            i++;
            continue;
        }
        
        if (isdigit(infix[i]) || infix[i] == '.') {
            while (isdigit(infix[i]) || infix[i] == '.') {
                postfix[j++] = infix[i++];
            }
            postfix[j++] = ' ';
        }
        else if (infix[i] == '(') {
            opPush(&opStack, infix[i]);
            i++;
        }
        else if (infix[i] == ')') {
            while (opStack.top >= 0 && opPeek(&opStack) != '(') {
                postfix[j++] = opPop(&opStack);
                postfix[j++] = ' ';
            }
            opPop(&opStack);
            i++;
        }
        else if (isOperator(infix[i])) {
            while (opStack.top >= 0 && getPriority(opPeek(&opStack)) >= getPriority(infix[i])) {
                postfix[j++] = opPop(&opStack);
                postfix[j++] = ' ';
            }
            opPush(&opStack, infix[i]);
            i++;
        }
        else {
            i++;
        }
    }
    
    while (opStack.top >= 0) {
        postfix[j++] = opPop(&opStack);
        postfix[j++] = ' ';
    }
    
    postfix[j] = '\0';
}

double evaluatePostfix(char *postfix) {
    NumStack numStack = {-1};
    int i = 0;
    
    while (postfix[i] != '\0') {
        if (postfix[i] == ' ') {
            i++;
            continue;
        }
        
        if (isdigit(postfix[i]) || postfix[i] == '.') {
            double num = 0.0;
            int decimal = 0;
            double factor = 0.1;
            
            while (isdigit(postfix[i]) || postfix[i] == '.') {
                if (postfix[i] == '.') {
                    decimal = 1;
                    i++;
                    continue;
                }
                if (decimal) {
                    num += (postfix[i] - '0') * factor;
                    factor *= 0.1;
                } else {
                    num = num * 10 + (postfix[i] - '0');
                }
                i++;
            }
            numPush(&numStack, num);
        }
        else if (isOperator(postfix[i])) {
            double b = numPop(&numStack);
            double a = numPop(&numStack);
            double result;
            
            switch(postfix[i]) {
                case '+': result = a + b; break;
                case '-': result = a - b; break;
                case '*': result = a * b; break;
                case '/': 
                    if (b == 0) {
                        printf("閿欒锛氶櫎鏁颁笉鑳戒负闆讹紒\n");
                        return NAN;
                    }
                    result = a / b; 
                    break;
                case '%': 
                    if (b == 0) {
                        printf("閿欒锛氭ā鏁颁笉鑳戒负闆讹紒\n");
                        return NAN;
                    }
                    result = (int)a % (int)b; 
                    break;
                default: result = 0;
            }
            numPush(&numStack, result);
            i++;
        }
        else {
            i++;
        }
    }
    
    return numPop(&numStack);
}

int main() {
    char expression[MAX_LEN];
    char postfix[MAX_LEN * 2];
    double result = 0;
    
    printf("===========================================\n");
    printf("            绠€鏄撹绠楀櫒 v1.0\n");
    printf("===========================================\n");
    printf("鏀寔鐨勮繍绠楃锛? - * / %\n");
    printf("鏀寔鎷彿锛?)\n");
    printf("杈撳叆 ANS 浣跨敤涓婁竴娆＄粨鏋淺n");
    printf("杈撳叆 quit 閫€鍑虹▼搴廫n");
    printf("===========================================\n\n");
    
    while (1) {
        printf("> ");
        fgets(expression, MAX_LEN, stdin);
        
        expression[strcspn(expression, "\n")] = '\0';
        
        if (strcmp(expression, "quit") == 0) {
            printf("鎰熻阿浣跨敤璁＄畻鍣紝鍐嶈锛乗n");
            break;
        }
        
        if (strlen(expression) == 0) {
            continue;
        }
        
        char processed[MAX_LEN];
        char *p = expression;
        char *q = processed;
        while (*p != '\0') {
            if (strncmp(p, "ANS", 3) == 0) {
                sprintf(q, "%.6f", result);
                q += strlen(q);
                p += 3;
            } else {
                *q++ = *p++;
            }
        }
        *q = '\0';
        
        infixToPostfix(processed, postfix);
        
        result = evaluatePostfix(postfix);
        
        if (isnan(result)) {
            continue;
        }
        
        printf("= %.6f\n\n", result);
    }
    
    return 0;
}
