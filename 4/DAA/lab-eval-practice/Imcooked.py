import time
import math
import heapq
import random
import matplotlib.pyplot as plt

### 1. Basic Sorts
# Bubble Sort 
# Selection Sort 
# Insertion Sort

### 2. Divide and Conquer Sorts
# Merge Sort 
# Quick Sort 

### 3. Non-Comparison / Linear-Time Sorts
# Counting Sort 
# Radix Sort 
# Bucket Sort 

### 4. Advanced / Hybrid Sorts
# Heap Sort
# Introsort (Introspective Sort)*

# Know the time complexities of all algorithms
# plot time take by each algorithm

arr = list()
times = dict()

for i in range(100):
    arr.append(random.randint(1, 100))
    
print(arr)

def tester(name: str, func, arr: list) -> None:
    times[name] = time.time()
    test = func(arr.copy())
    if test != sorted(arr): 
        print(name + " failed to sort!!")
        print("the array returned was: " + str(test))
    else:
        print(name + " sorted successfully!!")
    times[name] = time.time() - times[name]
    print(name + " took " + str(times[name] * 1000000) + " nano seconds")


def my_bubble_sort(arr: list): 
    n:int = len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j+1] < arr[j]):
                c = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = c
    return arr

def my_select_sort(arr: list) -> list:
    nu = list()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def my_insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def my_merge_sort(arr: list) -> list:
    n = len(arr)
    if(n <2): return arr
    m = n//2
    left = my_merge_sort(arr[:m])
    right = my_merge_sort(arr[m:])
    return my_mergeer(left,right)

def my_mergeer(arr_l: list, arr_r: list) -> list:
    i = 0
    j = 0
    result = list()
    while(i < len(arr_l) and j < len(arr_r)):
        if(arr_l[i] < arr_r[j]):
            result.append(arr_l[i])
            i += 1
        else:
            result.append(arr_r[j])
            j += 1
    result.extend(arr_l[i:])
    result.extend(arr_r[j:])
    return result
            

def my_quick_sort(arr: list) -> list:
    if(len(arr) <=1):
        return arr
    pivot = arr[-1]
    left = list()
    right = list()
    for i in arr[:-1]:
        if(i <= pivot):
            left.append(i)
        else:
            right.append(i)
    p = list()
    p.append(pivot)
    return my_quick_sort(left) + p +  my_quick_sort(right)

sorts = {
    "bubble": my_bubble_sort,
    "select": my_select_sort,
    "insert": my_insertion_sort,
    "merge": my_merge_sort,
    "quick": my_quick_sort
}

for sort_type in sorts.keys():
    tester(sort_type,sorts[sort_type],arr.copy())

tups = [
    (3 ,8 ),
    (5 ,9 ),
    (6 ,10), 
    (8 ,11), 
    (8 ,12),
    (1 ,4 ),
    (3 ,5 ),
    (0 ,6 ),
    (5 ,7 ),
    (2 ,13), 
    (12,14)
]
tups = sorted(tups, key=lambda x: x[1])
lptr = tups[0]
rptr = tups[1]
count = 1
results = list()
results.append(lptr)
lptr_idx = 0
rptr_idx = 1
while(rptr_idx < (len(tups))):
    if(rptr[0] > lptr[1]):
        count += 1
        results.append(rptr)
        lptr = tups[rptr_idx]
        rptr_idx += 1
        try:
            rptr = tups[rptr_idx]
        except:
            break
    else:
        rptr_idx += 1
        rptr = tups[rptr_idx]

print(count)
print(results)


print("== TOP 5 nums ==")
min_heap = arr[:5]
heapq.heapify(min_heap)
for num in arr:
    if(num > arr[0]):
        heapq.heappushpop(min_heap,num)
print("top 5 nums: " + str(sorted(min_heap)))

# rank inversions:
smol_arr = arr[:5]
ans = list()
for i in range(len(smol_arr)-1):
    for j in range(i,len(smol_arr)):
        if(smol_arr[i] > smol_arr[j]):
            ans.append((smol_arr[i], smol_arr[j]))
print("smol_arr " + str(smol_arr))
print("ans " + str(ans))