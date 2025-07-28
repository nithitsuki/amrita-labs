#include <stdio.h>

int main(int argc, char *argv[])
{
  int inpt, sum_digits;
  printf("Enter a number: ");
  scanf("%d",&inpt);
  while (inpt > 0) {
    sum_digits += inpt % 10;
    inpt = inpt / 10;
  }
  printf("Sum of digits is: %d\n",sum_digits);
  return 0;
}
