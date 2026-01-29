import time
import sys
import matplotlib.pyplot as plt

#!/usr/bin/env python3
def findSumIter(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def findSumRecursive(n):
    if n == 1:
        return 1
    else:
        return n + findSumRecursive(n - 1)
    
n = 120

# Increase recursion limit to handle larger n for recursive function
sys.setrecursionlimit(2000)

n_values = [10, 100, 500, 1000]
iter_times = []
rec_times = []

for n in n_values:
    # Time iterative function
    start = time.time()
    findSumIter(n)
    end = time.time()
    iter_times.append(end - start)
    
    # Time recursive function
    start = time.time()
    findSumRecursive(n)
    end = time.time()
    rec_times.append(end - start)

# Plot the results
plt.plot(n_values, iter_times, label='Iterative')
plt.plot(n_values, rec_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.show()