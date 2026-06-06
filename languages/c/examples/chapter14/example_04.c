void infixToPostfix(char *infix, char *postfix) {
    OpStack opStack = {-1};
    int i = 0, j = 0;
    
    while (infix[i] != '\0') {
        // 璺宠繃绌烘牸
        if (infix[i] == ' ') {
            i++;
            continue;
        }
        
        // 鏁板瓧
        if (isdigit(infix[i]) || infix[i] == '.') {
            while (isdigit(infix[i]) || infix[i] == '.') {
                postfix[j++] = infix[i++];
            }
            postfix[j++] = ' ';
        }
        // 宸︽嫭鍙?        else if (infix[i] == '(') {
            opPush(&opStack, infix[i]);
            i++;
        }
        // 鍙虫嫭鍙?        else if (infix[i] == ')') {
            while (opStack.top >= 0 && opPeek(&opStack) != '(') {
                postfix[j++] = opPop(&opStack);
                postfix[j++] = ' ';
            }
            opPop(&opStack);  // 寮瑰嚭宸︽嫭鍙?            i++;
        }
        // 杩愮畻绗?        else if (isOperator(infix[i])) {
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
    
    // 寮瑰嚭鍓╀綑杩愮畻绗?    while (opStack.top >= 0) {
        postfix[j++] = opPop(&opStack);
        postfix[j++] = ' ';
    }
    
    postfix[j] = '\0';
}
