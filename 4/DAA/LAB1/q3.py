import time

def stringToInt(s):
    if len(s) == 1:
        return int(s)
    else:
        return int(s[0]) * (10 ** (len(s) - 1)) + stringToInt(s[1:])

s = input("Enter string of digits: ")

start = time.time()
result = stringToInt(s)
end = time.time()

print(f"Integer: {result}")
print(f"Time taken: {end - start} seconds")
