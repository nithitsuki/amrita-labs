#include <stdio.h>
#include <stdlib.h>

int LinearSearch(int *arr, int n, int k)
{
    int kPtr = -1;
    for (int i = 0; i < (n); i++)
    {
        if (arr[i] == k)
        {
            kPtr = i;
        }
    }
    return kPtr;
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
    printf("Enter target element K: ");
    int k;
    scanf("%d",&k);
    printf("Found target number %d at %d:\n", k, LinearSearch(arr, n, k)+1);

    return 0;
}
