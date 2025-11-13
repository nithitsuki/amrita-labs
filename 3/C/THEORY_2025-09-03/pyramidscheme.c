#include <stdio.h>
#include <stdlib.h>

void display(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int *MakePyramidScheme(int n)
{
    int *arr = malloc(sizeof(int) * ((2 * n) - 1));
    for (int i = 0; i < n; i++)
    {
        arr[i] = i + 1;
    }
    for (int i = n; i < (2 * n); i++)
    {
        arr[i] = (2 * n) - i - 1;
    }
    return arr;
}
int main(int argc, char const *argv[])
{
    int n = 4;
    for (int i = 1; i <= n; i++)
    {
        int *arr = MakePyramidScheme(i);
        for (int j = n - i; j > 0; j--)
        {
            printf(" ");
        }

        display(arr, (2 * i) - 1);
        free(arr);
    }

    return 0;
}
