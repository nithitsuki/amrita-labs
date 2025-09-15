#include <stdio.h>
#include <stdlib.h>
typedef enum bool
{
    FALSE,
    TRUE
} bool;
void BubbleSort(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - 1 - i); j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }  
    }
}
int main(int argc, char const *argv[])
{
    printf("Enter size of array, N:");
    int n;
    scanf("%d", &n);
    int *arr = (int *)malloc(sizeof(int) * n);
    printf("Enter %d integers, one in each line:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    BubbleSort(arr,n);
    printf("Sorted numbers are:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}
