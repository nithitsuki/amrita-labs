#include <stdio.h>
#include <math.h>

int main()
{
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    double sum = 0, mean, stddev = 0;

    for (int* i = arr; i < arr+n; i++) {
        sum += *(i);
    }
    mean = sum / n;

    for (int i = 0; i < n; i++) {
        stddev += pow(arr[i] - mean, 2);
    }
    stddev = sqrt(stddev / (double) n);

    printf("Mean = %.2f\n", mean);
    printf("Standard Deviation = %.2f\n", stddev);

    return 0;
}