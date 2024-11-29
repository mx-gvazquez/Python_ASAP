# The Python 'print()' function is often used to output variables.
x = "Python is awesome"
print(x)

print("--------")

# In the 'print()' function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the '+' operator to CONCATENATE output multiple variables:
print("--------")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# RESPECT data types.
# In the print() function, when you try to combine
# a string and a number with the + operator,
# Python will give you an error:
print("--------")
x = 5
y = "Johny"
# print(x + y)

# Yet, this there's a WAY to do it right.
print(y, x)

