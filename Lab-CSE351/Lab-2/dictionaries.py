
students = {}

for _ in range (3) :
    name = input (" Enter student name : ")
    marks = int( input (" Enter marks : ") )
    students [ name ] = marks
    print (" Student Dictionary :", students )


search_name = input (" Enter the name of the student to find marks : ")
print(f" Marks of { search_name }:", students . get ( search_name , "Not found "))


update_name = input (" Enter the name of the student to update marks : ")
new_marks = int( input (" Enter new marks : ") )
students [ update_name ] = new_marks


del_name = input (" Enter the name of the student to delete : ")
students . pop ( del_name , None )

print (" Updated Dictionary :", students )