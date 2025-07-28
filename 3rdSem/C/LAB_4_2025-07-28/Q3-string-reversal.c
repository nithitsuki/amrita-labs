#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    // printf("whitespace ascci is %d \n",*" ");
    char next_char;
    char *string = malloc(sizeof(char) * 100);
    // char string[];
    int len;
    for (len = 0; (int)next_char != *" "; len++)
    {
        next_char = getchar();
        string[len] = next_char;
    }

    for (; len >= 0; len--)
    {
        putchar(string[len]);
    }
    printf("\n");
    

    return 0;
}
