def reverse_and_check_palindrome(N):
   
    reversed_N = str(N)[::-1].lstrip('0')
    
   
    is_palindrome = "YES" if str(N) == str(N)[::-1] else "NO"
    
   
    print(reversed_N)
    print(is_palindrome)

# Input
N = input().strip()

# Output
reverse_and_check_palindrome(N)
