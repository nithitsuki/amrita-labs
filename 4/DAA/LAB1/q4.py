def reverseString(s):
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0]

s = input("Enter string: ")
result = reverseString(s)
print(f"Reversed: {result}")
