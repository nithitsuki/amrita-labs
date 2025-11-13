#include <stdio.h>

int main(int argc, char const *argv[])
{
    int count = 5;
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < count; j++)
        {
            if(j<=i) printf("%d ",j+1);
        }
        printf("\n");
    }
    return 0;
}
