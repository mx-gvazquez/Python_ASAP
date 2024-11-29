"""
Remove any duplicates from a List:
First we have a List that contains duplicates:
Create a 'dictionary', using the List items as 'keys'.

TRICK:
This will automatically remove any duplicates because
dictionaries cannot have duplicate keys.

Then, convert the dictionary back into a list:

Now we have a List without any duplicates,
and it has the same order as the original List.

Print the List to demonstrate the result
"""


mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


print("-------------")

# Como funcion parametrizada

def my_function(vector):
  return list(dict.fromkeys(vector))

mylist = my_function(["Pedro", "Hugo", "Pedro", "Luis", "Luis"])

print(mylist)


print("-----------")

# Otra manera es convertirlo a 'set', mismo resultado.

a = [1, 2, 1, 1, 3, 4, 3, 3, 5]

res = list(set(a))
print(res)