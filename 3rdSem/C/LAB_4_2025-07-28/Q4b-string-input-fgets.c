#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char* string = malloc(sizeof(char)*100);
    if(string == NULL) {return 1;}
    fgets(string,50,stdin);
    printf("The given sentence is: \n %s \n",string);
    return 0;
}
