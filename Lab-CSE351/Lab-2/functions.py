def greet ( name ) :
    print ( f"Hello , { name }!")
name = input (" Enter your name : ")
greet ( name )

def factorial ( n ) :
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial ( n - 1)

num = int ( input (" Enter a number to find its factorial : ") )
print ( f" Factorial of {num} is { factorial (num)}")


def is_prime ( n ) :
    if n <= 1:
        return False
    for i in range (2 , int( n ** 0.5) + 1) :
        if n % i == 0:
            return False
        return True

prime_check = int( input (" Enter a number to check if it is prime : ") )
if is_prime ( prime_check ) :
    print ( f"{ prime_check } is a prime number .")
else :
    print ( f"{ prime_check } is not a prime number .")