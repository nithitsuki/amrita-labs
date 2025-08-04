#include <stdio.h>

int maxOfThree(int a, int b, int c)
{
  return a>=b ? (a>=c ? a : b) : (b>=c ? b : c);
}

int main(int argc, char *argv[])
{
  printf("max of 4, 21, 12 is %d \n", maxOfThree(4,21,12));
  return 0;
}
