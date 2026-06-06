# -*- coding: utf-8 -*-
"""100 道编程题参考代码"""

PROG_SOLUTIONS = [
# 1
'''#include <stdio.h>
int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("和:%d 差:%d 积:%d 商:%d\\n", a + b, a - b, a * b, b != 0 ? a / b : 0);
    return 0;
}''',
# 2
'''#include <stdio.h>
#define PI 3.14159
int main(void) {
    double r, c, s;
    scanf("%lf", &r);
    c = 2 * PI * r;
    s = PI * r * r;
    printf("周长:%.5f 面积:%.5f\\n", c, s);
    return 0;
}''',
# 3
'''#include <stdio.h>
int main(void) {
    int a, b, c, max, min;
    scanf("%d %d %d", &a, &b, &c);
    max = min = a;
    if (b > max) max = b; if (c > max) max = c;
    if (b < min) min = b; if (c < min) min = c;
    printf("max=%d min=%d\\n", max, min);
    return 0;
}''',
# 4
'''#include <stdio.h>
int isLeap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
}
int main(void) {
    int y;
    scanf("%d", &y);
    printf("%s\\n", isLeap(y) ? "闰年" : "平年");
    return 0;
}''',
# 5
'''#include <stdio.h>
int main(void) {
    int score;
    char grade;
    scanf("%d", &score);
    if (score >= 90) grade = 'A';
    else if (score >= 80) grade = 'B';
    else if (score >= 70) grade = 'C';
    else if (score >= 60) grade = 'D';
    else grade = 'F';
    printf("%c\\n", grade);
    return 0;
}''',
# 6
'''#include <stdio.h>
int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}
int main(void) {
    for (int i = 2; i < 100; i++)
        if (isPrime(i)) printf("%d ", i);
    printf("\\n");
    return 0;
}''',
# 7
'''#include <stdio.h>
int main(void) {
    int n, sum = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) sum += i;
    printf("%d\\n", sum);
    return 0;
}''',
# 8
'''#include <stdio.h>
int main(void) {
    int n;
    long long f = 1;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) f *= i;
    printf("%lld\\n", f);
    return 0;
}''',
# 9
'''#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        if (i <= 1) printf("%d ", i);
        else {
            int c = a + b;
            printf("%d ", c);
            a = b; b = c;
        }
    }
    printf("\\n");
    return 0;
}''',
# 10
'''#include <stdio.h>
int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}
int main(void) {
    int n;
    scanf("%d", &n);
    printf("%s\\n", isPrime(n) ? "是素数" : "不是素数");
    return 0;
}''',
# 11
'''#include <stdio.h>
int main(void) {
    int n, rev = 0;
    scanf("%d", &n);
    int x = n;
    while (x) { rev = rev * 10 + x % 10; x /= 10; }
    printf("%d\\n", rev);
    return 0;
}''',
# 12
'''#include <stdio.h>
int main(void) {
    int n, sum = 0;
    scanf("%d", &n);
    if (n < 0) n = -n;
    while (n) { sum += n % 10; n /= 10; }
    printf("%d\\n", sum);
    return 0;
}''',
# 13
'''#include <stdio.h>
int main(void) {
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++)
            printf("%d*%d=%-4d", j, i, i * j);
        printf("\\n");
    }
    return 0;
}''',
# 14
'''#include <stdio.h>
#include <ctype.h>
int main(void) {
    char ch;
    scanf(" %c", &ch);
    if (isupper(ch)) printf("大写字母\\n");
    else if (islower(ch)) printf("小写字母\\n");
    else if (isdigit(ch)) printf("数字\\n");
    else printf("其他\\n");
    return 0;
}''',
# 15
'''#include <stdio.h>
#include <ctype.h>
int main(void) {
    char s[256];
    int a = 0, d = 0, sp = 0;
    fgets(s, sizeof(s), stdin);
    for (int i = 0; s[i]; i++) {
        if (isalpha(s[i])) a++;
        else if (isdigit(s[i])) d++;
        else if (s[i] == ' ') sp++;
    }
    printf("字母:%d 数字:%d 空格:%d\\n", a, d, sp);
    return 0;
}''',
# 16
'''#include <stdio.h>
#include <ctype.h>
int main(void) {
    char s[256];
    fgets(s, sizeof(s), stdin);
    for (int i = 0; s[i]; i++)
        if (islower(s[i])) s[i] = toupper(s[i]);
    printf("%s", s);
    return 0;
}''',
# 17
'''#include <stdio.h>
int main(void) {
    char s[256], t[256];
    int j = 0;
    fgets(s, sizeof(s), stdin);
    for (int i = 0; s[i]; i++)
        if (s[i] != ' ' && s[i] != '\\n') t[j++] = s[i];
    t[j] = '\\0';
    printf("%s\\n", t);
    return 0;
}''',
# 18
'''#include <stdio.h>
#include <string.h>
int main(void) {
    char s[256];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\\n")] = '\\0';
    int i = 0, j = strlen(s) - 1;
    int ok = 1;
    while (i < j) {
        if (s[i] != s[j]) { ok = 0; break; }
        i++; j--;
    }
    printf("%s\\n", ok ? "是回文" : "不是回文");
    return 0;
}''',
# 19
'''#include <stdio.h>
void mycpy(char *dst, const char *src) {
    while ((*dst++ = *src++));
}
int main(void) {
    char a[100], b[100] = "hello";
    mycpy(a, b);
    printf("%s\\n", a);
    return 0;
}''',
# 20
'''#include <stdio.h>
void mycat(char *dst, const char *src) {
    while (*dst) dst++;
    while ((*dst++ = *src++));
}
int main(void) {
    char s[100] = "Hi ";
    mycat(s, "World");
    printf("%s\\n", s);
    return 0;
}''',
# 21
'''#include <stdio.h>
void bubble(int a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
}
int main(void) {
    int a[] = {5, 2, 8, 1, 9}, n = 5;
    bubble(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}''',
# 22
'''#include <stdio.h>
void selection(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[min]) min = j;
        int t = a[i]; a[i] = a[min]; a[min] = t;
    }
}
int main(void) {
    int a[] = {5, 2, 8, 1}, n = 4;
    selection(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}''',
# 23
'''#include <stdio.h>
void insertion(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
        a[j + 1] = key;
    }
}
int main(void) {
    int a[] = {5, 2, 8, 1}, n = 4;
    insertion(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}''',
# 24
'''#include <stdio.h>
int binarySearch(int a[], int n, int key) {
    int l = 0, h = n - 1;
    while (l <= h) {
        int m = (l + h) / 2;
        if (a[m] == key) return m;
        if (a[m] < key) l = m + 1;
        else h = m - 1;
    }
    return -1;
}
int main(void) {
    int a[] = {1, 3, 5, 7, 9};
    printf("下标:%d\\n", binarySearch(a, 5, 5));
    return 0;
}''',
# 25
'''#include <stdio.h>
void reverse(int a[], int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}
int main(void) {
    int a[] = {1, 2, 3, 4, 5}, n = 5;
    reverse(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}''',
# 26
'''#include <stdio.h>
int main(void) {
    int a[] = {3, 9, 1, 7, 5}, n = 5;
    int maxi = 0, mini = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[maxi]) maxi = i;
        if (a[i] < a[mini]) mini = i;
    }
    printf("max=%d@%d min=%d@%d\\n", a[maxi], maxi, a[mini], mini);
    return 0;
}''',
# 27
'''#include <stdio.h>
int main(void) {
    int a[] = {1, 2, 2, 3, 1, 2, 3}, n = 7;
    int cnt[10] = {0};
    for (int i = 0; i < n; i++) cnt[a[i]]++;
    for (int i = 0; i < 10; i++)
        if (cnt[i]) printf("%d出现%d次\\n", i, cnt[i]);
    return 0;
}''',
# 28
'''#include <stdio.h>
#define M 2
#define N 3
int main(void) {
    int a[M][N] = {{1,2,3},{4,5,6}}, b[M][N] = {{1,1,1},{1,1,1}}, c[M][N];
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            c[i][j] = a[i][j] + b[i][j];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) printf("%d ", c[i][j]);
        printf("\\n");
    }
    return 0;
}''',
# 29
'''#include <stdio.h>
#define M 2
#define K 3
#define N 2
int main(void) {
    int a[M][K] = {{1,2,3},{4,5,6}}, b[K][N] = {{1,2},{3,4},{5,6}}, c[M][N] = {0};
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            for (int t = 0; t < K; t++)
                c[i][j] += a[i][t] * b[t][j];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) printf("%d ", c[i][j]);
        printf("\\n");
    }
    return 0;
}''',
# 30
'''#include <stdio.h>
#define R 2
#define C 3
int main(void) {
    int a[R][C] = {{1,2,3},{4,5,6}}, t[C][R];
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            t[j][i] = a[i][j];
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < R; j++) printf("%d ", t[i][j]);
        printf("\\n");
    }
    return 0;
}''',
# 31
'''#include <stdio.h>
void swap(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}
int main(void) {
    int x = 3, y = 7;
    swap(&x, &y);
    printf("%d %d\\n", x, y);
    return 0;
}''',
# 32
'''#include <stdio.h>
int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}
int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\\n", gcd(a, b));
    return 0;
}''',
# 33
'''#include <stdio.h>
int gcd(int a, int b) {
    while (b) { int t = b; b = a % b; a = t; }
    return a;
}
int lcm(int a, int b) { return a / gcd(a, b) * b; }
int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\\n", lcm(a, b));
    return 0;
}''',
# 34
'''#include <stdio.h>
long long fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
int main(void) {
    int n;
    scanf("%d", &n);
    printf("%lld\\n", fact(n));
    return 0;
}''',
# 35
'''#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\\n", fib(n));
    return 0;
}''',
# 36
'''#include <stdio.h>
int digitSum(int n) {
    if (n == 0) return 0;
    return n % 10 + digitSum(n / 10);
}
int main(void) {
    int n;
    scanf("%d", &n);
    if (n < 0) n = -n;
    printf("%d\\n", digitSum(n));
    return 0;
}''',
# 37
'''#include <stdio.h>
int main(void) {
    int a[] = {1, 2, 3, 4, 5}, n = 5, sum = 0;
    int *p = a;
    for (int i = 0; i < n; i++) sum += *(p + i);
    printf("%d\\n", sum);
    return 0;
}''',
# 38
'''#include <stdio.h>
int mylen(const char *s) {
    int n = 0;
    while (*s++) n++;
    return n;
}
int main(void) {
    printf("%d\\n", mylen("hello"));
    return 0;
}''',
# 39
'''#include <stdio.h>
#include <string.h>
void strRev(char *s) {
    char *p = s, *q = s + strlen(s) - 1;
    while (p < q) { char t = *p; *p = *q; *q = t; p++; q--; }
}
int main(void) {
    char s[] = "hello";
    strRev(s);
    printf("%s\\n", s);
    return 0;
}''',
# 40
'''#include <stdio.h>
#include <stdlib.h>
void bubble(int *a, int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
}
int main(void) {
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    bubble(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    free(a);
    return 0;
}''',
# 41
'''#include <stdio.h>
int main(void) {
    int a[] = {1, 3, 5}, b[] = {2, 4, 6}, c[6];
    int i = 0, j = 0, k = 0, na = 3, nb = 3;
    while (i < na && j < nb)
        c[k++] = a[i] < b[j] ? a[i++] : b[j++];
    while (i < na) c[k++] = a[i++];
    while (j < nb) c[k++] = b[j++];
    for (int t = 0; t < k; t++) printf("%d ", c[t]);
    return 0;
}''',
# 42
'''#include <stdio.h>
typedef struct {
    int id;
    char name[32];
    float score;
} Student;
int main(void) {
    Student st[3];
    for (int i = 0; i < 3; i++) {
        printf("学号 姓名 成绩: ");
        scanf("%d %s %f", &st[i].id, st[i].name, &st[i].score);
    }
    for (int i = 0; i < 3; i++)
        printf("%d %s %.1f\\n", st[i].id, st[i].name, st[i].score);
    return 0;
}''',
# 43
'''#include <stdio.h>
typedef struct { int id; char name[32]; float score; } Student;
void sortByScore(Student a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = i + 1; j < n; j++)
            if (a[j].score > a[i].score) {
                Student t = a[i]; a[i] = a[j]; a[j] = t;
            }
}
int main(void) {
    Student st[] = {{1,"A",80},{2,"B",90},{3,"C",70}};
    sortByScore(st, 3);
    for (int i = 0; i < 3; i++) printf("%s %.1f\\n", st[i].name, st[i].score);
    return 0;
}''',
# 44
'''#include <stdio.h>
#include <ctype.h>
int main(void) {
    FILE *fp = fopen("input.txt", "r");
    if (!fp) return 1;
    int inWord = 0, cnt = 0;
    int ch;
    while ((ch = fgetc(fp)) != EOF) {
        if (isspace(ch)) inWord = 0;
        else if (!inWord) { inWord = 1; cnt++; }
    }
    fclose(fp);
    printf("单词数:%d\\n", cnt);
    return 0;
}''',
# 45
'''#include <stdio.h>
int main(void) {
    FILE *in = fopen("src.txt", "r"), *out = fopen("dst.txt", "w");
    if (!in || !out) return 1;
    int ch;
    while ((ch = fgetc(in)) != EOF) fputc(ch, out);
    fclose(in); fclose(out);
    return 0;
}''',
# 46
'''#include <stdio.h>
int main(void) {
    FILE *fp = fopen("input.txt", "r");
    char target = 'a';
    int cnt = 0, ch;
    if (!fp) return 1;
    while ((ch = fgetc(fp)) != EOF)
        if (ch == target) cnt++;
    fclose(fp);
    printf("'%c'出现%d次\\n", target, cnt);
    return 0;
}''',
# 47
'''#include <stdio.h>
int main(void) {
    FILE *fp = fopen("nums.txt", "r");
    if (!fp) return 1;
    int x, n = 0;
    double sum = 0;
    while (fscanf(fp, "%d", &x) == 1) { sum += x; n++; }
    fclose(fp);
    printf("平均:%.2f\\n", n ? sum / n : 0);
    return 0;
}''',
# 48
'''#include <stdio.h>
typedef struct { int id; char name[20]; } Item;
int main(void) {
    Item a[] = {{1,"Tom"},{2,"Amy"}};
    FILE *fp = fopen("data.bin", "wb");
    fwrite(a, sizeof(Item), 2, fp);
    fclose(fp);
    Item b[2];
    fp = fopen("data.bin", "rb");
    fread(b, sizeof(Item), 2, fp);
    fclose(fp);
    for (int i = 0; i < 2; i++) printf("%d %s\\n", b[i].id, b[i].name);
    return 0;
}''',
# 49
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *create(int a[], int n) {
    Node *head = NULL, *tail = NULL;
    for (int i = 0; i < n; i++) {
        Node *p = (Node *)malloc(sizeof(Node));
        p->data = a[i]; p->next = NULL;
        if (!head) head = tail = p;
        else { tail->next = p; tail = p; }
    }
    return head;
}
void printList(Node *head) {
    for (Node *p = head; p; p = p->next) printf("%d ", p->data);
    printf("\\n");
}
int main(void) {
    int a[] = {1, 2, 3};
    Node *head = create(a, 3);
    printList(head);
    return 0;
}''',
# 50
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
void append(Node **head, int x) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = x; p->next = NULL;
    if (!*head) { *head = p; return; }
    Node *q = *head;
    while (q->next) q = q->next;
    q->next = p;
}
int main(void) {
    Node *head = NULL;
    append(&head, 1); append(&head, 2); append(&head, 3);
    for (Node *p = head; p; p = p->next) printf("%d ", p->data);
    return 0;
}''',
# 51
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *append(Node *head, int x) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = x; p->next = NULL;
    if (!head) return p;
    Node *q = head;
    while (q->next) q = q->next;
    q->next = p;
    return head;
}
void deleteVal(Node **head, int x) {
    Node *p = *head, *prev = NULL;
    while (p) {
        if (p->data == x) {
            Node *del = p;
            if (prev) prev->next = p->next;
            else *head = p->next;
            p = p->next;
            free(del);
        } else { prev = p; p = p->next; }
    }
}
int main(void) {
    Node *head = NULL;
    int a[] = {1, 2, 2, 3};
    for (int i = 0; i < 4; i++) head = append(head, a[i]);
    deleteVal(&head, 2);
    for (Node *p = head; p; p = p->next) printf("%d ", p->data);
    printf("\\n");
    return 0;
}''',
# 52
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *reverse(Node *head) {
    Node *prev = NULL, *cur = head;
    while (cur) {
        Node *nxt = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}
int main(void) {
    Node *head = NULL, *tail = NULL;
    int a[] = {1, 2, 3, 4};
    for (int i = 0; i < 4; i++) {
        Node *p = (Node *)malloc(sizeof(Node));
        p->data = a[i]; p->next = NULL;
        if (!head) head = tail = p;
        else { tail->next = p; tail = p; }
    }
    head = reverse(head);
    for (Node *p = head; p; p = p->next) printf("%d ", p->data);
    printf("\\n");
    return 0;
}''',
# 53
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
int hasCycle(Node *head) {
    Node *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return 1;
    }
    return 0;
}
int main(void) {
    printf("%d\\n", hasCycle(NULL));
    return 0;
}''',
# 54
'''#include <stdio.h>
#include <string.h>
#define MAX 100
char stack[MAX];
int top = -1;
int match(char *s) {
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') stack[++top] = s[i];
        else {
            if (top < 0) return 0;
            char c = stack[top--];
            if (s[i] == ')' && c != '(') return 0;
            if (s[i] == ']' && c != '[') return 0;
            if (s[i] == '}' && c != '{') return 0;
        }
    }
    return top == -1;
}
int main(void) {
    printf("%s\\n", match("({[]})") ? "匹配" : "不匹配");
    return 0;
}''',
# 55
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int id; struct Node *next; } Node;
int josephus(int n, int k) {
    Node *head = NULL, *tail = NULL;
    for (int i = 1; i <= n; i++) {
        Node *p = (Node *)malloc(sizeof(Node));
        p->id = i; p->next = NULL;
        if (!head) head = tail = p;
        else { tail->next = p; tail = p; }
    }
    tail->next = head;
    Node *p = head, *prev = tail;
    int remain = n;
    while (remain > 1) {
        for (int i = 1; i < k; i++) { prev = p; p = p->next; }
        prev->next = p->next;
        free(p);
        p = prev->next;
        remain--;
    }
    int ans = p->id;
    free(p);
    return ans;
}
int main(void) {
    printf("最后剩下:%d\\n", josephus(5, 3));
    return 0;
}''',
# 56
'''#include <stdio.h>
int main(void) {
    double a, b;
    char op;
    scanf("%lf %c %lf", &a, &op, &b);
    switch (op) {
        case '+': printf("%.2f\\n", a + b); break;
        case '-': printf("%.2f\\n", a - b); break;
        case '*': printf("%.2f\\n", a * b); break;
        case '/': printf("%.2f\\n", b ? a / b : 0); break;
        default: printf("无效运算符\\n");
    }
    return 0;
}''',
# 57
'''#include <stdio.h>
int dayOfWeek(int y, int m, int d) {
    if (m < 3) { m += 12; y--; }
    int w = (d + 2*m + 3*(m+1)/5 + y + y/4 - y/100 + y/400 + 1) % 7;
    return w; /* 0=周日 */
}
int main(void) {
    int y, m, d;
    scanf("%d-%d-%d", &y, &m, &d);
    const char *names[] = {"日","一","二","三","四","五","六"};
    printf("星期%s\\n", names[dayOfWeek(y, m, d)]);
    return 0;
}''',
# 58
'''#include <stdio.h>
void decToBin(int n, char *buf) {
    if (n == 0) { buf[0] = '0'; buf[1] = '\\0'; return; }
    char tmp[33]; int i = 0;
    while (n) { tmp[i++] = (n % 2) + '0'; n /= 2; }
    int j = 0;
    while (i > 0) buf[j++] = tmp[--i];
    buf[j] = '\\0';
}
int main(void) {
    char s[33];
    decToBin(13, s);
    printf("%s\\n", s);
    return 0;
}''',
# 59
'''#include <stdio.h>
int binToDec(const char *s) {
    int val = 0;
    for (int i = 0; s[i]; i++)
        if (s[i] == '0' || s[i] == '1')
            val = val * 2 + (s[i] - '0');
    return val;
}
int main(void) {
    printf("%d\\n", binToDec("1101"));
    return 0;
}''',
# 60
'''#include <stdio.h>
int main(void) {
    for (int n = 2; n <= 100; n++) {
        int sum = 1;
        for (int i = 2; i * i <= n; i++)
            if (n % i == 0) { sum += i; if (i != n / i) sum += n / i; }
        if (sum == n) printf("%d ", n);
    }
    printf("\\n");
    return 0;
}''',
# 61
'''#include <stdio.h>
int main(void) {
    for (int n = 100; n <= 999; n++) {
        int a = n / 100, b = n / 10 % 10, c = n % 10;
        if (a*a*a + b*b*b + c*c*c == n) printf("%d ", n);
    }
    printf("\\n");
    return 0;
}''',
# 62
'''#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < n - i; j++) printf(" ");
        for (int j = 0; j < 2 * i - 1; j++) printf("*");
        printf("\\n");
    }
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 0; j < n - i; j++) printf(" ");
        for (int j = 0; j < 2 * i - 1; j++) printf("*");
        printf("\\n");
    }
    return 0;
}''',
# 63
'''#include <stdio.h>
int main(void) {
    int n, a[20][20] = {0};
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        a[i][0] = a[i][i] = 1;
        for (int j = 1; j < i; j++)
            a[i][j] = a[i-1][j-1] + a[i-1][j];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) printf("%d ", a[i][j]);
        printf("\\n");
    }
    return 0;
}''',
# 64
'''#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand((unsigned)time(NULL));
    int target = rand() % 100 + 1, guess;
    while (1) {
        printf("猜数字(1-100): ");
        scanf("%d", &guess);
        if (guess == target) { printf("正确!\\n"); break; }
        printf("%s\\n", guess > target ? "太大" : "太小");
    }
    return 0;
}''',
# 65
'''#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    int cnt[7] = {0};
    srand((unsigned)time(NULL));
    for (int i = 0; i < 1000; i++) cnt[rand() % 6 + 1]++;
    for (int i = 1; i <= 6; i++) printf("%d点:%d次\\n", i, cnt[i]);
    return 0;
}''',
# 66
'''#include <stdio.h>
#include <math.h>
int main(void) {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    double d = b*b - 4*a*c;
    if (d < 0) printf("无实根\\n");
    else if (d == 0) printf("x=%.4f\\n", -b/(2*a));
    else printf("x1=%.4f x2=%.4f\\n", (-b+sqrt(d))/(2*a), (-b-sqrt(d))/(2*a));
    return 0;
}''',
# 67
'''#include <stdio.h>
double mySqrt(double x) {
    if (x <= 0) return 0;
    double r = x;
    for (int i = 0; i < 20; i++) r = 0.5 * (r + x / r);
    return r;
}
int main(void) {
    printf("%.6f\\n", mySqrt(2.0));
    return 0;
}''',
# 68
'''#include <stdio.h>
int main(void) {
    double e = 1.0, term = 1.0;
    for (int i = 1; i <= 20; i++) {
        term /= i;
        e += term;
    }
    printf("%.10f\\n", e);
    return 0;
}''',
# 69
'''#include <stdio.h>
#include <math.h>
double mySin(double x) {
    double term = x, sum = x;
    for (int n = 1; n <= 10; n++) {
        term *= -x * x / ((2*n) * (2*n + 1));
        sum += term;
    }
    return sum;
}
int main(void) {
    printf("%.6f\\n", mySin(1.0));
    return 0;
}''',
# 70
'''#include <stdio.h>
#include <ctype.h>
int main(void) {
    char line[256];
    fgets(line, sizeof(line), stdin);
    int i = 0, len = 0, first = 1;
    while (line[i]) {
        if (isalpha(line[i])) len++;
        else if (isspace(line[i]) && len > 0) {
            if (!first) printf(" ");
            printf("%d", len);
            first = 0; len = 0;
        }
        i++;
    }
    if (len > 0) { if (!first) printf(" "); printf("%d", len); }
    printf("\\n");
    return 0;
}''',
# 71
'''#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void) {
    char line[256], word[64], longest[64] = "";
    fgets(line, sizeof(line), stdin);
    int i = 0, j = 0, maxLen = 0;
    while (1) {
        if (isalpha(line[i])) word[j++] = line[i];
        else if (j > 0) {
            word[j] = '\\0';
            if (j > maxLen) { maxLen = j; strcpy(longest, word); }
            j = 0;
        }
        if (line[i] == '\\0') break;
        i++;
    }
    printf("%s\\n", longest);
    return 0;
}''',
# 72
'''#include <stdio.h>
void replaceAll(char *s, char oldc, char newc) {
    for (int i = 0; s[i]; i++)
        if (s[i] == oldc) s[i] = newc;
}
int main(void) {
    char s[] = "hello world";
    replaceAll(s, 'l', 'L');
    printf("%s\\n", s);
    return 0;
}''',
# 73
'''#include <stdio.h>
int main(void) {
    char s[256];
    int cnt[256] = {0};
    fgets(s, sizeof(s), stdin);
    for (int i = 0; s[i]; i++) cnt[(unsigned char)s[i]]++;
    for (int i = 0; i < 256; i++)
        if (cnt[i]) printf("'%c':%d\\n", i, cnt[i]);
    return 0;
}''',
# 74
'''#include <stdio.h>
#include <ctype.h>
#include <string.h>
void trim(char *s) {
    int start = 0, end = strlen(s) - 1;
    while (isspace(s[start])) start++;
    while (end >= start && isspace(s[end])) end--;
    int j = 0;
    for (int i = start; i <= end; i++) s[j++] = s[i];
    s[j] = '\\0';
}
int main(void) {
    char s[] = "  hello  ";
    trim(s);
    printf("[%s]\\n", s);
    return 0;
}''',
# 75
'''#include <stdio.h>
int myAtoi(const char *s) {
    int sign = 1, val = 0;
    while (*s == ' ') s++;
    if (*s == '-' || *s == '+') sign = (*s++ == '-') ? -1 : 1;
    while (*s >= '0' && *s <= '9')
        val = val * 10 + (*s++ - '0');
    return sign * val;
}
int main(void) {
    printf("%d\\n", myAtoi("-12345"));
    return 0;
}''',
# 76
'''#include <stdio.h>
void myItoa(int n, char *s) {
    int i = 0, sign = 1;
    if (n < 0) { sign = -1; n = -n; }
    do { s[i++] = n % 10 + '0'; n /= 10; } while (n);
    if (sign < 0) s[i++] = '-';
    s[i] = '\\0';
    for (int l = 0, r = i - 1; l < r; l++, r--) {
        char t = s[l]; s[l] = s[r]; s[r] = t;
    }
}
int main(void) {
    char buf[32];
    myItoa(-456, buf);
    printf("%s\\n", buf);
    return 0;
}''',
# 77
'''#include <stdio.h>
#define N 3
int main(void) {
    int a[N][N] = {{1,2,3},{4,5,6},{7,8,9}}, sum = 0;
    for (int i = 0; i < N; i++) sum += a[i][i];
    printf("%d\\n", sum);
    return 0;
}''',
# 78
'''#include <stdio.h>
#define N 3
int main(void) {
    int a[N][N] = {{1,2,3},{2,1,4},{3,4,1}};
    int ok = 1;
    for (int i = 0; i < N && ok; i++)
        for (int j = 0; j < N; j++)
            if (a[i][j] != a[j][i]) ok = 0;
    printf("%s\\n", ok ? "对称" : "不对称");
    return 0;
}''',
# 79
'''#include <stdio.h>
#define N 3
int main(void) {
    int a[N][N] = {{1,2,3},{4,5,6},{7,8,9}};
    int top=0, bottom=N-1, left=0, right=N-1;
    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; j++) printf("%d ", a[top][j]);
        top++;
        for (int i = top; i <= bottom; i++) printf("%d ", a[i][right]);
        right--;
        if (top <= bottom)
            for (int j = right; j >= left; j--) printf("%d ", a[bottom][j]);
        bottom--;
        if (left <= right)
            for (int i = bottom; i >= top; i--) printf("%d ", a[i][left]);
        left++;
    }
    return 0;
}''',
# 80
'''#include <stdio.h>
typedef struct { int y, m, d; } Date;
int cmpDate(Date a, Date b) {
    if (a.y != b.y) return a.y - b.y;
    if (a.m != b.m) return a.m - b.m;
    return a.d - b.d;
}
int main(void) {
    Date d1 = {2024, 3, 1}, d2 = {2024, 5, 1};
    int c = cmpDate(d1, d2);
    printf("%s更早\\n", c < 0 ? "d1" : (c > 0 ? "d2" : "相同"));
    return 0;
}''',
# 81
'''#include <stdio.h>
typedef struct { char name[32]; double salary; } Emp;
int main(void) {
    Emp e[] = {{"Tom",5000},{"Amy",6000},{"Bob",4500}};
    int n = 3;
    for (int i = 0; i < n - 1; i++)
        for (int j = i + 1; j < n; j++)
            if (e[j].salary > e[i].salary) {
                Emp t = e[i]; e[i] = e[j]; e[j] = t;
            }
    for (int i = 0; i < n; i++) printf("%s %.0f\\n", e[i].name, e[i].salary);
    return 0;
}''',
# 82
'''#include <stdio.h>
#include <string.h>
#define MAX 50
typedef struct { int id; char title[64]; } Book;
Book books[MAX];
int count = 0;
void addBook(void) {
    if (count >= MAX) return;
    printf("编号 书名: ");
    scanf("%d %s", &books[count].id, books[count].title);
    count++;
}
void listBooks(void) {
    for (int i = 0; i < count; i++)
        printf("%d %s\\n", books[i].id, books[i].title);
}
void findBook(int id) {
    for (int i = 0; i < count; i++)
        if (books[i].id == id) { printf("找到:%s\\n", books[i].title); return; }
    printf("未找到\\n");
}
int main(void) {
    int op, id;
    while (scanf("%d", &op) == 1 && op != 0) {
        if (op == 1) addBook();
        else if (op == 2) listBooks();
        else if (op == 3) { scanf("%d", &id); findBook(id); }
    }
    return 0;
}''',
# 83
'''#include <stdio.h>
int main(void) {
    FILE *fp = fopen("scores.txt", "r");
    if (!fp) return 1;
    int id, score, n = 0, sum = 0;
    while (fscanf(fp, "%d %d", &id, &score) == 2) { sum += score; n++; }
    fclose(fp);
    double avg = n ? (double)sum / n : 0;
    fp = fopen("result.txt", "w");
    fprintf(fp, "人数:%d 平均:%.2f\\n", n, avg);
    fclose(fp);
    return 0;
}''',
# 84
'''#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int sum = 0;
    for (int i = 1; i < argc; i++) sum += atoi(argv[i]);
    printf("和:%d\\n", sum);
    return 0;
}''',
# 85
'''#include <stdio.h>
int mystrlen(const char *s) {
    int n = 0; while (*s++) n++; return n;
}
void mystrcpy(char *d, const char *s) {
    while ((*d++ = *s++));
}
int mystrcmp(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }
    return (unsigned char)*a - (unsigned char)*b;
}
int main(void) {
    char a[32];
    mystrcpy(a, "hello");
    printf("len=%d cmp=%d\\n", mystrlen(a), mystrcmp(a, "hello"));
    return 0;
}''',
# 86
'''#include <stdio.h>
double add(double a, double b) { return a + b; }
double sub(double a, double b) { return a - b; }
double mul(double a, double b) { return a * b; }
double divv(double a, double b) { return b ? a / b : 0; }
int main(void) {
    double a = 10, b = 3;
    double (*ops[4])(double, double) = {add, sub, mul, divv};
    char sym[] = "+-*/";
    for (int i = 0; i < 4; i++)
        printf("%.2f %c %.2f = %.2f\\n", a, sym[i], b, ops[i](a, b));
    return 0;
}''',
# 87
'''#include <stdio.h>
int main(void) {
    FILE *fp = fopen("data.bin", "rb");
    if (!fp) return 1;
    int c0 = 0, c1 = 0, ch;
    while ((ch = fgetc(fp)) != EOF)
        for (int i = 0; i < 8; i++)
            if ((ch >> i) & 1) c1++; else c0++;
    fclose(fp);
    printf("0:%d 1:%d\\n", c0, c1);
    return 0;
}''',
# 88
'''#include <stdio.h>
void caesarEnc(char *s, int k) {
    for (int i = 0; s[i]; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = 'a' + (s[i] - 'a' + k) % 26;
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = 'A' + (s[i] - 'A' + k) % 26;
}
int main(void) {
    char s[] = "Hello";
    caesarEnc(s, 3);
    printf("%s\\n", s);
    return 0;
}''',
# 89
'''#include <stdio.h>
void caesarDec(char *s, int k) {
    for (int i = 0; s[i]; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = 'a' + (s[i] - 'a' - k + 26) % 26;
        else if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = 'A' + (s[i] - 'A' - k + 26) % 26;
}
int main(void) {
    char s[] = "Khoor";
    caesarDec(s, 3);
    printf("%s\\n", s);
    return 0;
}''',
# 90
'''#include <stdio.h>
#include <string.h>
#define MAX 20
typedef struct { char name[32]; char phone[16]; } Contact;
Contact book[MAX];
int n = 0;
void add(void) {
    printf("姓名 电话: ");
    scanf("%s %s", book[n].name, book[n].phone);
    n++;
}
void show(void) {
    for (int i = 0; i < n; i++) printf("%s %s\\n", book[i].name, book[i].phone);
}
int main(void) {
    int op;
    while (scanf("%d", &op) == 1 && op) {
        if (op == 1) add();
        else if (op == 2) show();
    }
    return 0;
}''',
# 91
'''#include <stdio.h>
#include <string.h>
void longestCommon(const char *a, const char *b, char *out) {
    int la = strlen(a), lb = strlen(b), maxLen = 0, end = 0;
    for (int i = 0; i < la; i++)
        for (int j = 0; j < lb; j++) {
            int k = 0;
            while (i + k < la && j + k < lb && a[i + k] == b[j + k]) k++;
            if (k > maxLen) { maxLen = k; end = i; }
        }
    strncpy(out, a + end, maxLen);
    out[maxLen] = '\\0';
}
int main(void) {
    char res[64];
    longestCommon("abcdef", "zcdemn", res);
    printf("%s\\n", res);
    return 0;
}''',
# 92
'''#include <stdio.h>
void rotateLeft(int a[], int n, int k) {
    k %= n;
    int tmp[k];
    for (int i = 0; i < k; i++) tmp[i] = a[i];
    for (int i = 0; i < n - k; i++) a[i] = a[i + k];
    for (int i = 0; i < k; i++) a[n - k + i] = tmp[i];
}
int main(void) {
    int a[] = {1, 2, 3, 4, 5}, n = 5;
    rotateLeft(a, n, 2);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}''',
# 93
'''#include <stdio.h>
int secondMax(int a[], int n) {
    int max1 = a[0], max2 = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max1) { max2 = max1; max1 = a[i]; }
        else if (a[i] > max2 && a[i] != max1) max2 = a[i];
    }
    return max2;
}
int main(void) {
    int a[] = {3, 9, 1, 7, 5};
    printf("%d\\n", secondMax(a, 5));
    return 0;
}''',
# 94
'''#include <stdio.h>
int singleNumber(int a[], int n) {
    int x = 0;
    for (int i = 0; i < n; i++) x ^= a[i];
    return x;
}
int main(void) {
    int a[] = {4, 1, 2, 1, 4};
    printf("%d\\n", singleNumber(a, 5));
    return 0;
}''',
# 95
'''#include <stdio.h>
#include <stdlib.h>
typedef struct { int start, end; } Interval;
int cmp(const void *a, const void *b) {
    return ((Interval *)a)->start - ((Interval *)b)->start;
}
int main(void) {
    Interval arr[] = {{1,3},{2,6},{8,10},{15,18}};
    int n = 4;
    qsort(arr, n, sizeof(Interval), cmp);
    int out = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || arr[i].start > arr[out].end)
            arr[++out] = arr[i];
        else if (arr[i].end > arr[out].end)
            arr[out].end = arr[i].end;
    }
    for (int i = 0; i <= out; i++)
        printf("[%d,%d] ", arr[i].start, arr[i].end);
    return 0;
}''',
# 96
'''#include <stdio.h>
int maxSubSum(int a[], int n) {
    int cur = a[0], best = a[0];
    for (int i = 1; i < n; i++) {
        cur = a[i] > cur + a[i] ? a[i] : cur + a[i];
        if (cur > best) best = cur;
    }
    return best;
}
int main(void) {
    int a[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    printf("%d\\n", maxSubSum(a, 9));
    return 0;
}''',
# 97
'''#include <stdio.h>
#define MAX 100
int stack[MAX], top = -1;
void push(int x) { if (top < MAX - 1) stack[++top] = x; }
int pop(void) { return top >= 0 ? stack[top--] : -1; }
int main(void) {
    push(1); push(2); push(3);
    printf("%d ", pop());
    printf("%d\\n", pop());
    return 0;
}''',
# 98
'''#include <stdio.h>
#define MAX 100
int q[MAX], front = 0, rear = 0, cnt = 0;
void enqueue(int x) {
    if (cnt < MAX) { q[rear] = x; rear = (rear + 1) % MAX; cnt++; }
}
int dequeue(void) {
    if (cnt == 0) return -1;
    int x = q[front]; front = (front + 1) % MAX; cnt--; return x;
}
int main(void) {
    enqueue(1); enqueue(2);
    printf("%d ", dequeue());
    printf("%d\\n", dequeue());
    return 0;
}''',
# 99
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *newNode(int x) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = x; p->next = NULL;
    return p;
}
Node *merge(Node *a, Node *b) {
    Node dummy; Node *tail = &dummy; dummy.next = NULL;
    while (a && b) {
        if (a->data <= b->data) { tail->next = a; a = a->next; }
        else { tail->next = b; b = b->next; }
        tail = tail->next;
    }
    tail->next = a ? a : b;
    return dummy.next;
}
int main(void) {
    Node *a = newNode(1); a->next = newNode(3); a->next->next = newNode(5);
    Node *b = newNode(2); b->next = newNode(4); b->next->next = newNode(6);
    Node *c = merge(a, b);
    for (Node *p = c; p; p = p->next) printf("%d ", p->data);
    printf("\\n");
    return 0;
}''',
# 100
'''#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *removeDup(Node *head) {
    Node *cur = head;
    while (cur) {
        Node *prev = cur, *p = cur->next;
        while (p) {
            if (p->data == cur->data) {
                prev->next = p->next;
                free(p);
                p = prev->next;
            } else { prev = p; p = p->next; }
        }
        cur = cur->next;
    }
    return head;
}
int main(void) {
    Node *head = (Node *)malloc(sizeof(Node));
    head->data = 1;
    head->next = (Node *)malloc(sizeof(Node));
    head->next->data = 2;
    head->next->next = (Node *)malloc(sizeof(Node));
    head->next->next->data = 2;
    head->next->next->next = NULL;
    head = removeDup(head);
    for (Node *p = head; p; p = p->next) printf("%d ", p->data);
    printf("\\n");
    return 0;
}''',
]

assert len(PROG_SOLUTIONS) == 100, f"应有100道，实际{len(PROG_SOLUTIONS)}"
