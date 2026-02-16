# Generate 1000 integer random numbers between 1 and 10000. Compare the sorting algorithms learnt in the class using the same set of numbers generated. Plot the time taken for them to complete the process.
import time
import random
import matplotlib.pyplot as plt

rand_nos = [random.randint(1, 10000) for i in range(1000)]

def MyBubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def MySelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

sorting_functions  = [MyBubbleSort, MySelectionSort]

time_taken = []
for sort_func in sorting_functions:
    arr_copy = rand_nos.copy()
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    time_taken.append(end_time - start_time)

plt.bar([func.__name__ for func in sorting_functions], time_taken)
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Comparison')
plt.show()