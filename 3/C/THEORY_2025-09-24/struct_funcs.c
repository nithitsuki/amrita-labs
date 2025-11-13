#include <stdio.h>

typedef int mint;

typedef struct Student {
    mint roll;
    char* name;
    float gpa;
} Student;

void displayStudent(Student S){
    printf(" Name: %s\n roll no: %d\n gpa: %.2f\n",S.name,S.roll,S.gpa);
    
}
mint main(mint argc, char *argv[]) {
    Student s1 = {23,"pranav",5.0};
    displayStudent(s1);
    return 0;
}
