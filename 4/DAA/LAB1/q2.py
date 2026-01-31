import time
import random
import matplotlib.pyplot as plt

def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [random.randint(1, 1000) for _ in range(10000)]
sorted_arr = sorted(arr)

linear_times = []
binary_times = []

for i in range(5):
    key = int(input(f"Enter search key {i+1}: "))
    
    start = time.time()
    linearSearch(arr, key)
    end = time.time()
    linear_times.append(end - start)
    
    start = time.time()
    binarySearch(sorted_arr, key)
    end = time.time()
    binary_times.append(end - start)

searches = [f"Search {i+1}" for i in range(5)]
plt.plot(searches, linear_times, label='Linear Search')
plt.plot(searches, binary_times, label='Binary Search')
plt.xlabel('Search Number')
plt.ylabel('Time (seconds)')
plt.title('Time taken for Linear and Binary Search')
plt.legend()
plt.show()
