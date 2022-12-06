"""
my_list = [] # Initializing empty list
print(my_list)

my_list2 = list() # Initializing empty list
print(my_list2)
"""
'''
# Adding elements to the list.
my_list = [1,2,3,'amit','kumar']
my_list2 = list([4,5,6,'Sunny','Aloha'])
print(my_list)
print(my_list2)

# Accessing elements from the list.
my_list = [1,2,3,'Amit','Kumar']
'''
'''
print(my_list[:]) # Accessing all the elements at a go.
print(my_list[3]) # Accessing 3rd element of the list.

# Accessing the elements from 1 to 4, i.e., index 0 to 3 & leaving index 4 of the list.
print(my_list[0:4]) 

print(my_list[::-1]) # Accessing all the elements in Reverse order.

print(my_list[0:5:2]) # Accessing from index 0 to 4 and jumping 2 elements intead of 1.

print(my_list[3][2]) # Accessing particular element of the string Amit (i).
'''
'''
# ----- Adding the list of elements ------
my_list.append([25,50]) # append add the elements as single element.
print(my_list)
print(len(my_list))
my_list2.extend([75,100]) # extending listby adding all the elements one by one.
print(my_list2)
print(len(my_list2))
'''
'''
my_list.insert(1,'insert_example') #insert passed paramenter in place of index and extend list.
print(my_list)
print(my_list + ['Concatenation']) # Concatenation
print (my_list * 2) # Multiply
print (my_list)
'''
# ----- Delete the list of elements ------
my_list = [1,2,3,'Aloha','Aloha Tech']
print (my_list)

del my_list[2] # deleting using delete keyword.
print (my_list)

my_list.remove('Aloha') # remove the passed elem. if present else error.
print (my_list)
 
a = my_list.pop(2) # Deleted element can be retrived.
print('Popped element:',a)
print('List remaining:',my_list) 