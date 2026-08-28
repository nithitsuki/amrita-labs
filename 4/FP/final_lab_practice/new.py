"""
Lab Evaluation 3 (Set A)
Max Marks: 15
"""
from multipledispatch import dispatch

# Question 1 (5 Marks)
# -------------------------------------------------------------------------
# A data analytics system processes inputs from different sources. 
# Based on input types, it applies different functional transformations: 
# If inputs are integers -> return their sum. 
# If inputs are strings -> concatenate them in uppercase. 
# If inputs are lists -> merge them and apply a function to remove duplicates. 
# Write a python program for above scenario using multiple dispatch.
@dispatch(int,int)
def add(a: int, b: int):
    return a + b

@dispatch(str,str)
def add(a: str, b: str):
    return str(a + b + " <string adder used>").upper()

@dispatch(list,list)
def add(a, b):
    return list(set(a + b))

print(add(1,2))
print(add("idli, dosa, ","vada"))
print(add([1,2,3],[2,3,4]))


# Question 2 (5 Marks)
# -------------------------------------------------------------------------
# Write a Python program that creates a lazy evaluation chain to 
# generate an infinite stream of numbers and detects the third 
# prime number greater than 100.
def inf_stream():
   current_value = 101
   while(True):
       yield current_value
       #when next hits
       current_value += 1

normal_stream = inf_stream()

def isPrime(n: int):
    return all(n % i != 0 for i in range(2,int(n**0.5)+1))

prime_stream = filter(isPrime,normal_stream)

first_prime = next(prime_stream)
second_prime = next(prime_stream)
third_prime = next(prime_stream)

print(third_prime)

# Question 3 (5 Marks)
# -------------------------------------------------------------------------
# Write a Python program to merge two lists and sort the result in 
# ascending order.
l1 = [1,2,3]
l2 = [7,8,9]
final_list = sorted(l2+l1)
print(final_list)
