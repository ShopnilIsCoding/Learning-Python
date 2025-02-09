def isPalindrome(s):
    return s==s[::-1]

s1=input("Enter the string: ")
# s2=''.join(reversed(s1))

if isPalindrome(s1):
    print(f"{s1} is a palindrome.")
else:
    print(f"{s1} is not a palindrome.")

