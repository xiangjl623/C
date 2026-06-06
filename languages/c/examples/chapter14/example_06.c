int main() {
    char expression[MAX_LEN];
    char postfix[MAX_LEN * 2];
    double result = 0;
    int choice;
    
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
        
        // 绉婚櫎鎹㈣绗?        expression[strcspn(expression, "\n")] = '\0';
        
        // 閫€鍑哄懡浠?        if (strcmp(expression, "quit") == 0) {
            printf("鎰熻阿浣跨敤璁＄畻鍣紝鍐嶈锛乗n");
            break;
        }
        
        // 绌鸿緭鍏?        if (strlen(expression) == 0) {
            continue;
        }
        
        // 澶勭悊 ANS
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
        
        // 杞崲涓哄悗缂€琛ㄨ揪寮?        infixToPostfix(processed, postfix);
        
        // 璁＄畻缁撴灉
        result = evaluatePostfix(postfix);
        
        if (isnan(result)) {
            continue;
        }
        
        printf("= %.6f\n\n", result);
    }
    
    return 0;
}
