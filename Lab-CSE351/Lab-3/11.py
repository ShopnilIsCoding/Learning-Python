
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
print(gcd(4,6))