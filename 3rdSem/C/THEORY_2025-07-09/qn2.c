#include <stdio.h>
#include <stdlib.h>

int total(int* a, int size)
{
  int total = 0;
  for (int i = 0; i < size; i++) {
    total += *(a+i);
  }
  return total;
}

int main(int argc, char *argv[])
{
  printf("How many array elements? ");
  int len;
  scanf("%d",&len);
  int* arr = malloc(sizeof(int)*len);
  for (int i = 0;i < len;i++) {
    printf("Enter value of element no.%d: ",i);
    scanf("%d",arr+i);
  }
  printf("total value of elements is %d\n",total(arr,len));
  return EXIT_SUCCESS;
}
