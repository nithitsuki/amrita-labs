#include <stdio.h>
#include <stdlib.h>

int* doubleIt(int* arr)
{
    int n = sizeof(arr)/sizeof(arr[0]);
    int* b = malloc(n*sizeof(int));
    for (int i = 0; i <= n; i++)
    {
        b[i] = 2*arr[i];
    }
    return b;
    
}
int main(int argc, char const *argv[])
{
    int a[] = {1,2,3};
    int* b = doubleIt(a);
    for (int i = 0; i < 3; i++)
    {
        printf("%d ",b[i]);
    }
    printf("\n");
    return 0;
}
