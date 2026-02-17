
#include <stdio.h>
#include <unistd.h>

void main()
{
    int pid;
    pid = fork();
    if (pid == 0)
    {
        printf("\nChild is processing\n");

        execlp("/home/nithilan/Software/amrita-labs/4/os/LAB_feb_16/factorial", "factorial", "5", NULL);
    }
    else
    {
        printf("Parent is processing");
    }
}