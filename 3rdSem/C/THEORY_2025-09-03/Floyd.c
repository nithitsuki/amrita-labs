#include <stdio.h>

int main(int argc, char const *argv[])
{
    int count = 5;
    int global = ;
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < count; j++)
        {
            if(j<=i) printf("%d ",global++);
        }
        printf("\n");
    }
    return 0;
}
