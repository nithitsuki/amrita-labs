#include <stdio.h>
#include <stdlib.h>

void SelectionSort(int *arr, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min =  99999;
        int victim = arr[i];
        int victim_ptr;
        for (int j = i; j < n; j++)
        {
            if (min > arr[j])
            {
                min = arr[j];
                victim_ptr = j;
            }
        }
        arr[i] = min;
        arr[victim_ptr] = victim;
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
    SelectionSort(arr, n);
    printf("Sorted numbers are:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}
