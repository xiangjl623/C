#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct Student {
    int id;
    char name[50];
    float score;
};

void addStudent(struct Student students[], int *count) {
    if (*count >= MAX_STUDENTS) {
        printf("瀛︾敓鏁伴噺宸茶揪涓婇檺\n");
        return;
    }
    
    struct Student s;
    printf("璇疯緭鍏ュ鐢烮D锛?);
    scanf("%d", &s.id);
    printf("璇疯緭鍏ュ鐢熷鍚嶏細");
    scanf("%s", s.name);
    printf("璇疯緭鍏ュ鐢熸垚缁╋細");
    scanf("%f", &s.score);
    
    students[*count] = s;
    (*count)++;
    
    printf("瀛︾敓淇℃伅娣诲姞鎴愬姛\n");
}

void printStudents(struct Student students[], int count) {
    printf("\n瀛︾敓鍒楄〃锛歕n");
    printf("ID\t濮撳悕\t鎴愮哗\n");
    for (int i = 0; i < count; i++) {
        printf("%d\t%s\t%.1f\n", students[i].id, students[i].name, students[i].score);
    }
}

int main() {
    struct Student students[MAX_STUDENTS];
    int count = 0;
    int choice;
    
    do {
        printf("\n瀛︾敓淇℃伅绠＄悊绯荤粺\n");
        printf("1. 娣诲姞瀛︾敓\n");
        printf("2. 鏄剧ず瀛︾敓鍒楄〃\n");
        printf("3. 閫€鍑篭n");
        printf("璇烽€夋嫨锛?);
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                addStudent(students, &count);
                break;
            case 2:
                printStudents(students, count);
                break;
            case 3:
                printf("閫€鍑虹郴缁焅n");
                break;
            default:
                printf("鏃犳晥閫夋嫨\n");
        }
    } while (choice != 3);
    
    return 0;
}
