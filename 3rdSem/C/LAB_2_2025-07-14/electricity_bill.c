#include <stdio.h>

#define rate1 1.2
#define rate2 2
#define rate3 3

int main(int argc, char *argv[])
{
  double units;
  double price;
  printf("Enter Units Consumed: ");
  scanf("%lf",&units);
  printf("|----------------------|\n");
  printf("|========BILL==========|\n");
  printf("| Total Units Used: %.2lf |\n",units);
  if(units > 300){
    printf("| units after 300: 3.00*%0.2lf = %.2lfrs |\n",(units-300),(units - 300)*rate3);
    price += (units - 300)*rate3; 
    units = 300;
  }
  if (units > 100){
    printf("| units after 100 until 200: 2.00*%0.2lf = %.2lfrs |\n",(units-100),(units - 100)*rate2);
    price += (units - 100)*rate2; 
    units = 100;
  }
  printf("| units until 100: 1.20*%0.2lf = %.2lfrs |\n",(units),(units)*rate1);
  price += (units)*rate1; 
  printf("| total price: %.2lf |\n",price);
  return(0);
}
