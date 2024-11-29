# Naming Conventions

"""
++OK++

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


snake_case_naming_variables = RECOMENDED

++WRONG++

2myvar = "John"
my-var = "John"
my var = "John"
"""


"""
Python has no command for declaring a 'data type' variable.
A variable is created the moment you first assign a value to it.
"""
x = 5
y = "John"
print(x)
print(y)


"""
Variables do not need to be declared with any particular type, 
and can even change type after they have been set.
"""

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print("------")

# Variable names are case-sensitive.  'A' will not overwrite 'a'
a = 4
A = "Sally"
print(a)
print(A)


# Many Values to Multiple Variables
print("+++++++++++")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
print("************")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("------")
# Unpack a Collection
"""
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. 
This is called 'unpacking'.
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)