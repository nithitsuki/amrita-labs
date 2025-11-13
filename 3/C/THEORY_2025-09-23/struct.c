#include <stdio.h>

typedef struct
{
    int Phy;
    int Che;
    int Bio;
    int Math;
    int Geo;
} Marks;

typedef struct
{
    char name[50];
    int roll;
    Marks marks;

} student;

int main()
{
    student S1;
    printf("Enter Name: ");
    scanf("%s", S1.name);
    printf("Enter roll: ");
    scanf("%d", &(S1.roll));
    printf("Enter Phy: ");
    scanf("%d", &(S1.marks.Phy));
    printf("Enter Che: ");
    scanf("%d", &(S1.marks.Che));
    printf("Enter Bio: ");
    scanf("%d", &(S1.marks.Bio));
    printf("Enter Math: ");
    scanf("%d", &(S1.marks.Math));
    printf("Enter Geo: ");
    scanf("%d", &(S1.marks.Geo));

    printf("\nStudent Details:\n");
    printf("Name: %s\n", S1.name);
    printf("Roll: %d\n", S1.roll);
    printf("Physics: %d\n", S1.marks.Phy);
    printf("Chemistry: %d\n", S1.marks.Che);
    printf("Biology: %d\n", S1.marks.Bio);
    printf("Math: %d\n", S1.marks.Math);
    printf("Geography: %d\n", S1.marks.Geo);

    return 0;
}