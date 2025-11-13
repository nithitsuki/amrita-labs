#include <stdio.h>
#include <stdlib.h>
#define PI 3.14159

void calc_CircleAreaPerimeter(int radius)
{
  printf("Area is %0.2f\n",PI*radius*radius);
  printf("Perimeter is %0.f\n",2*PI*radius);
}

int main(int argc, char *argv[])
{
  int* a = malloc(sizeof(int));
  printf("Enter the radius of the circle");
  scanf("%d",a);
  calc_CircleAreaPerimeter(*a);
  free(a);
  return EXIT_SUCCESS;
}
