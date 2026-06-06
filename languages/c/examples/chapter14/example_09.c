// 娣诲姞鍙橀噺瀛樺偍
double variables[26] = {0};  // a-z

// 鍦ㄤ富绋嬪簭涓鐞嗗彉閲忚祴鍊?if (strchr(expression, '=') != NULL) {
    char var = expression[0];
    if (var >= 'a' && var <= 'z') {
        // 鎻愬彇绛夊彿鍙宠竟鐨勮〃杈惧紡
        char *expr = strchr(expression, '=') + 1;
        // 璁＄畻骞惰祴鍊?        infixToPostfix(expr, postfix);
        variables[var - 'a'] = evaluatePostfix(postfix);
        printf("%c = %.6f\n\n", var, variables[var - 'a']);
        continue;
    }
}
