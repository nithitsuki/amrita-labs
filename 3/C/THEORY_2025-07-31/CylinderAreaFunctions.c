#include <stdio.h>
#define PI 3.14

void VolumeOfCylinder_NoArgsNoReturn()
{
  int radius = 5; int height = 5;
  float Area = PI*radius*radius;
  float volume = Area*height;
  printf("radius = %d\n", radius);
  printf("Area = %0.2f\n", Area);
  printf("volume = %0.2f\n", volume);
}

void VolumeOfCylinder_NoReturn(int radius, int height)
{
  float Area = PI*radius*radius;
  float volume = Area*height;
  printf("radius = %d\n", radius);
  printf("Area = %0.2f\n", Area);
  printf("volume = %0.2f\n", volume);
}

float VolumeOfCylinder_NoArgs()
{
  int radius = 5; int height = 5;
  float Area = PI*radius*radius;
  float volume = Area*height;
  printf("radius = %d\n", radius);
  printf("Area = %0.2f\n", Area);
  return  volume;
}

float VolumeOfCylinder(int radius, int height)
{
  float Area = PI*radius*radius;
  float volume = Area*height;
  printf("radius = %d\n", radius);
  printf("Area = %0.2f\n", Area);
  return  volume;
}

int main(int argc, char *argv[])
{
  printf("---------No Args No Return--------\n");
  VolumeOfCylinder_NoArgsNoReturn();
  printf("---------No Args------------------\n");
  VolumeOfCylinder_NoReturn(5,5);
  return 0;
}
