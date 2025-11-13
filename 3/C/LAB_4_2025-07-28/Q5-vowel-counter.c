#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char* string = malloc(sizeof(char)*100);
    if(string == NULL) {return 1;}
    fgets(string,100,stdin);
    printf("\nThe given sentence is: \n %s",string);
    char next_char; int len = 0;
    int vowels = 0;
    while ((int)next_char != '\n')
    {
        next_char = string[len];
        switch ((int)next_char)
        {
        case 'a':
            vowels++;
            break;
        case 'e':
            vowels++;
            break;
        case 'i':
            vowels++;
            break;
        case 'o':
            vowels++;
            break;
        case 'u':
            vowels++;
            break;
        default:
            break;
        }
        len++;
    }
    printf("\nThe given sentence has %d vowels \n",vowels);
    return 0;
}

