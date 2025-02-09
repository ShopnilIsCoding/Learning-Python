# Sets Example
set_a = {1 , 2 , 3 , 4}
set_b = {3 , 4 , 5 , 6}
print (" Union :", set_a | set_b )
print (" Intersection :", set_a & set_b )
print (" Difference (A - B):", set_a - set_b )
print ("Is A a subset of B?", set_a . issubset ( set_b ) )
# Add and remove elements
set_a . add (10)
set_b . remove (6)
print (" Updated Set A:", set_a )
print (" Updated Set B:", set_b )