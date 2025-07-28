#include <stdio.h>

int main(int argc, char const *argv[])
{
    float inpt;
    printf("Enter Integer: ");
    scanf("%f",&inpt);
    printf("Octal Format: %o \n Hex Representation: %x n",(unsigned int)inpt,(unsigned int)inpt);
    return 0;
}
