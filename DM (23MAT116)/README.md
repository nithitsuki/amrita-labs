# Revision for tommorows DM Lab Evaluation
---

## LAB1:

### Basical Logical Operators
1. **Equality (`==`)**  
Returns true if `P` and `Q` are equal  
```matlab
P == Q  
ans: logical true  
```

2. **Inequality (`~=`)**  
Returns true if `P` and `Q` are not equal  
```matlab
P ~= Q  
ans: logical true  
```

3. **Greater Than (`>`)**  
Returns true if `P` is greater than `Q`  
```matlab
P > Q  
ans: logical true  
```

4. **Less Than (`<`)**  
Returns true if `P` is less than `Q`  
```matlab
P < Q  
ans: logical false  
```

5. **Greater Than or Equal To (`>=`)**  
Returns true if `P` is greater than or equal to `Q`  
```matlab
P >= Q  
ans: logical false  
```

6. **Less Than or Equal To (`<=`)**  
Returns true if `P` is less than or equal to `Q`  
```matlab
P <= Q  
ans: logical true  
```

7. **Logical AND (`&`)**  
Returns true if both `P` and `Q` are true  
```matlab
P = true; Q = false; P & Q  
ans: logical false  
```

8. **Logical OR (`|`)**  
Returns true if either `P` or `Q` is true  
```matlab
P = true; Q = false; P | Q  
ans: logical true  
```

9. **Logical NOT (`~`)**  
Returns the negation of `P`  
```matlab
~P  
ans: logical false  
```

10. **Exclusive OR (`xor`)**  
 Returns true if exactly one of `P` or `Q` is true  
 ```matlab
 xor(P, Q)  
 ans: logical true  
 ```
---

### DM specific Logical Operators
1. **Implication (`->`)**  
P->Q can be written as ~P + Q
```matlab
~P | Q
```

2. **biconditional (`<->`)**  
Negaton of XOR, i.e, both must be same for true
```matlab
~xor(P,Q)
```
---

### Creating Matrice of Binary numbers
+ Ascending form 0 to (2^n)-1
```matlab
A = dec2bin(0:(2^n)-1)-'0';
% dec2bin() returns binary string
% subtracting ascii char '0' from each char
% so that '0' becomes 0 and '1' - '0' becomes 1
```
+ Descending form (2^n)-1 to 0
```matlab
dec2bin((2^n)-1:-1:0)-'0';
```
---

### Creating Truth Tables Using For Loops
```matlab
A = dec2bin(0:(2^2)-1)-'0'; % create matrix of binary numbers
% start from 1 as Matrix indices start from 1
for i = 1:(2^2)
    A(i,3)=xor(A(i,1),A(i,2));
    % Make 3rd col as xor of 1st and 2nd
    % applies to all rows from 1 to 2^n
end
A
```
---
### Checking for Tautology,contradiction, and contingency
```matlab
% ones(no_rows,no_cols)
% zeros(no_rows,no_cols)

if A (1:2^n,5)==ones(2^n, 1)
        fprintf('Tautology')
else
if A (1:2^n,5)==zeros(2^n, 1)
        fprintf('contradiction')
else
    fprintf('contingency')
end
```
---

## LAB 2:
looking at lab1, I remembered lab2
I dont need revision for it as of now
