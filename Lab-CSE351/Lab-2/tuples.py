
my_tuple = (10 , 20 , 30 , 40 , 50)
print (" First element :", my_tuple [0])
print (" Last element :", my_tuple [ -1])

my_list = list ( my_tuple )
my_list [1] = 2
my_tuple = tuple ( my_list )
print (" Modified Tuple :", my_tuple )

print (" Count of 30:", my_tuple . count (30) )
print (" Index of 40:", my_tuple . index (40) )