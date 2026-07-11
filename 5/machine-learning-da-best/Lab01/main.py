#!/usr/bin/env python3
import numpy as np
from collections import Counter
import random 

def q1(inpt):
    n = len(inpt)
    ans = list()
    for i in range(n-1):
        for j in range(i,n):
            if(inpt[i] + inpt[j] == 10):
               ans.append((inpt[i],inpt[j])) 
    return ans

def q2(inpt):
    if(len(inpt) < 3):
        raise Exception("list smoler than 3")
    # no rules against inbuilt functions :p
    return (min(inpt),max(inpt))

def q3(A: numpy.ndarray,m):
    if(m == 0):
        return A
    return np.matmul(A,q3(A,m-1))
    
    return 0

def q4(s):
    list(s) # C did strings better
    d = {}
    max_occur = ('',0)
    for letter in s:
        if(not(letter in d.keys())):
            d[letter] = 1
        else:
            d[letter] += 1
        if(d[letter] > max_occur[1]):
           max_occur = (letter,d[letter])
    return max_occur

def q5():
    x = [random.randint(1, 10) for _ in range(25)]
    mean = sum(x) / len(x)
    median = sorted(x)[len(x)//2]
    mode = Counter(x).most_common(1)[0][0]
    return mean, median, mode
   
inpt = [2,7,4,1,3,6]
print(f"Q1: {q1(inpt)}")
print(f"Q2: {q2(inpt)}")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Q3: {q3(A,3)}")
print(f"Q4: {q4("made by nithitsuki")}")
print(f"Q5: {q5()}")
