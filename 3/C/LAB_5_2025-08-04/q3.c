#include <stdio.h>

float circleArea(float radius)
{
  return 3.14 * radius * radius;
}

int main(int argc, char *argv[])
{
  printf("Area of circle with radius 5 is %.2f \n",circleArea(5.0));
  return 0;
}
