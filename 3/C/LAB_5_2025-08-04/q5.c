#include <stdio.h>

float CelsiusToFarenheit(float C)
{
  float F = (9*C/5)+32;
  return F;
}


float FarenheitToCelsius(float F)
{
  float C = (F-32)*5/9;
  return C;
}

int main(int argc, char *argv[])
{
  printf("56.23F in Celcius is %.2f \n", FarenheitToCelsius(56.23));
  printf("56.23C in Farenheight is %.2f \n", CelsiusToFarenheit(56.23));
  return 0;
}
