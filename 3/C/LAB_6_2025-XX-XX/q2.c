#include <stdio.h>

int main() {
    int arr[10];

    printf("Enter 10 integers, one in each line:\n");
    for(int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Even numbers are:\n");

    for(int i = 0; i < 10; i++) {
        if(arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
    return 0;
}
