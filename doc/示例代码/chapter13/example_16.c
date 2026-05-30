#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100

typedef struct {
    int id;
    char name[50];
    float score;
} Student;

void saveStudents(Student students[], int count) {
    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) {
        perror("淇濆瓨澶辫触");
        return;
    }
    
    fwrite(students, sizeof(Student), count, fp);
    fclose(fp);
    printf("淇濆瓨鎴愬姛锛乗n");
}

int loadStudents(Student students[]) {
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        return 0;
    }
    
    int count = 0;
    while (fread(&students[count], sizeof(Student), 1, fp) == 1) {
        count++;
    }
    
    fclose(fp);
    return count;
}

int main() {
    Student students[MAX_STUDENTS];
    int count = loadStudents(students);
    
    // 娣诲姞鏂板鐢?    strcpy(students[count].name, "鏂板鐢?);
    students[count].id = count + 1;
    students[count].score = 85.5f;
    count++;
    
    saveStudents(students, count);
    
    return 0;
}
