#include <stdio.h> 
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int num, i;
    unsigned long long fact = 1;

    num = atoi(argv[1]);

    for (i = 1; i <= num; i++) {
        fact *= i;
    }

    printf("The Factorial of %d is %llu\n", num, fact);
    return 0;
}