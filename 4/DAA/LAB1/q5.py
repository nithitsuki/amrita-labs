def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

s = input("Enter string: ")
result = isPalindrome(s)
if result:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
