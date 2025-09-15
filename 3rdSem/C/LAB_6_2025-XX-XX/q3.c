#include <stdio.h>

int main(int argc, char const *argv[])
{
    int arr2[5];
    int arr1[5];
    printf("Enter 5 integers, one in each line:\n");
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &arr1[i]);
    }
    printf("Enter 5 integers, one in each line:\n");
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &arr2[i]);
    }
    int arr3[3];
    for (int i = 0; i < 5; i++)
    {
        arr3[i] = arr1[i] + arr2[i];
    }
    printf("Sum of arrays numbers are:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", arr3[i]);
    }

    return 0;
}
