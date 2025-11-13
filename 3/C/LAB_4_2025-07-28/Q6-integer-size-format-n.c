#include <stdio.h>

int main(int argc, char const *argv[])
{
    int inpt;
    printf("Enter Integer: ");
    scanf("%d",&inpt);
    int size;
    printf("%d%n",inpt,&size);
    printf("\nSize of input is: %d\n",size);
    return 0;
}
