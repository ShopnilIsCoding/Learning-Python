for i in range(5):
    print(i)
def full_name(first_name,last_name,**kwargs):
    return f'{first_name} {kwargs['middle_name']} {last_name}'

name = full_name('John', 'Doe',middle_name='Milton')
print(name)

numbers= [2,55,100,89,75,7]

print(numbers[2:5])
print(numbers[1:6:2])
print(numbers[6:1:-2])
print(numbers[-2])
print(numbers[::-1])#reverse
odd_nums =[num for num in numbers if num%2 == 1 and num%5==0]
print(odd_nums)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age=45)