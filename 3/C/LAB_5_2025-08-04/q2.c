#include <stdio.h>

void isEvenOdd(int a)
{
  printf("%d is %s\n",a,a%2==0 ? "even" : "odd");
}

int main(int argc, char *argv[])
{
  isEvenOdd(2);
  return 0;
}
