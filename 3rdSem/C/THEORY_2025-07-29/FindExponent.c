#include <stdio.h>
#include <math.h>

double factorial(int i)
{
    if(i<=1){return 1;}
    return i*factorial(i-1);
}
int main(int argc, char const *argv[])
{
    printf("Enter x: ");
    int x; scanf("%d",&x);
    printf("Enter n: ");
    int n; scanf("%d",&n);
    double exp;
    for(int i = 0; i < n; i++)
    {
        exp += (pow(x,(double)i)/factorial(i));
    }
    printf("The value of exponent is %lf\n",exp);
    return 0;
}
