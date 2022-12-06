#---- Initializing a tuple -----
'''
my_tuple = (1,2,3)
my_tuple_2 = tuple(('Amit','Kumar','Srivastava'))
print(my_tuple)
print(my_tuple_2)

my_tuple_3 = 'Example', #add comma in the end if you want a tuple with single element. 
                        # Else its acts as STRING.
print(type(my_tuple_3))
'''
#---- Accessing a tuple -----
my_tuple = (1,2,3)
my_tuple_2 = ('Amit','Kumar','Srivastava')
my_tuple_3 = (1,2,3,'Amit')

print(my_tuple[0]) # Accessing 0th element of the list.
print(my_tuple_2[:]) # Accessing all the elements at a go.
print(my_tuple_3[3][2]) # Accessing particular element of the string Amit (i).