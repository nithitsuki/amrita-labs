#include <stdio.h>

int main(int argc, char *argv[])
{
  for(int i = 3; i > 0; i--)
  {
    for(int j = (i*2)-1; j > 0; j--)
    {
      printf("* ");
    }
    printf("\n");
  }
  return 0;
}
