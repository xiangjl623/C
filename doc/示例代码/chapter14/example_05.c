double evaluatePostfix(char *postfix) {
    NumStack numStack = {-1};
    int i = 0;
    
    while (postfix[i] != '\0') {
        // 璺宠繃绌烘牸
        if (postfix[i] == ' ') {
            i++;
            continue;
        }
        
        // 鏁板瓧
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
        // 杩愮畻绗?        else if (isOperator(postfix[i])) {
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
