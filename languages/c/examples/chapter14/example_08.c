// 鍦ㄥ悗缂€琛ㄨ揪寮忔眰鍊间腑娣诲姞
else if (postfix[i] == 's' && strncmp(postfix+i, "sin", 3) == 0) {
    double x = numPop(&numStack);
    numPush(&numStack, sin(x));
    i += 3;
}
else if (postfix[i] == 'c' && strncmp(postfix+i, "cos", 3) == 0) {
    double x = numPop(&numStack);
    numPush(&numStack, cos(x));
    i += 3;
}
