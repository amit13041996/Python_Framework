'''
# Python accepts both single('') and double("") quotes for String. 
first_name = "Amit" 
last_name = 'Srivastava'

full_name = first_name + " " + last_name
print (full_name)

message = "I don't know"  # Using single quotes('') for O/p.
print (message)

Program = "\"Pyhton\""  # Using Escape sequence double quotes("") for O/p.
print (Program)

# --------------------------------------------------------------------------------
sent = 'Python Coding'

print(len(sent))
print(sent.index('C'))
print(sent.replace('P','J'))
print(sent.split())

# ---------------We can combine strings and numbers by using the format() method! ------------------------------------------------------------
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

print(myorder.encode())
