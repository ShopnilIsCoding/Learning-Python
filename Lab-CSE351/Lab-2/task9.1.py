f=int(input("Enter the number you want to get factorial: "))
factorial=1
for i in range(1,f+1):
    factorial*=i

print(f"The factorial of {f} is {factorial}")
