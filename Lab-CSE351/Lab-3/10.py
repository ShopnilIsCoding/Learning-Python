def isArmstrong(n):
    digits = [int(digit) for digit in str(n)]
    total = 0
    power = len(digits)
    for d in digits:
        total += d ** power
    if total == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"