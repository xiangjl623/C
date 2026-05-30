#include <stdio.h>
#include <stdlib.h>

// 閾捐〃鑺傜偣缁撴瀯
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// 鍒涘缓鏂拌妭鐐?Node* createNode(int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// 鎵撳嵃閾捐〃
void printList(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    // 鍒涘缓閾捐〃
    Node *head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);
    
    printf("閾捐〃鍐呭锛?);
    printList(head);
    
    return 0;
}
