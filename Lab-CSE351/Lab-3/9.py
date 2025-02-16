def is_palindrome(n):
    return "Palindrome" if str(n) == str(n)[::-1] else "Not a Palindrome"