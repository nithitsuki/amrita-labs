#include <stdio.h>
#include <stdlib.h>

int main(){
    //print data types sizes
    printf("Size of char   is %d Bytes\n",  sizeof(char));
    printf("Size of short  is %d Bytes\n",  sizeof(short));
    printf("Size of int    is %d Bytes\n",  sizeof(int));
    printf("Size of long   is %d Bytes\n",  sizeof(long));
    printf("Size of float  is %d Bytes\n",  sizeof(float));
    printf("Size of double is %d Bytes\n",  sizeof(double));

    //qn2
    printf("Enter a number and a float seperated by a singe space: ");
    int* a = malloc(sizeof(int));
    float* b = malloc(sizeof(float)); 
    scanf("%d %f",a,b);
    printf("Their sum is %.2f\n",(*a) + (*b));

    //qn3
    //qn4
    //qn5
  
    return 0;
}
