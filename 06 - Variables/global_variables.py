"""
Variables that are created outside of a function
(as in all of the examples in the previous pages)
are known as 'global variables'.

'Global variables' can be used by everyone,
both inside of functions and outside.
"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("-------------")

"""
Local variables are those INSIDE the function, and are independent
despite their name.

If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, 
global and with the original value.
"""

x = "incredible"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


"""
For this EXACT reason, we should OPTIMIZE code by making
'Local a Global' variable used iteratively many times inside a LOOP.

This is BAD PRACTICE since Python tries to find the variable inside the LOOP, 
and then look for it outside on ROOT, every single time.

SOLUTION: Re-asign this global variable to Local variable.
"""

print("*************")

global_var = 10

def iterative_func():
    ans  = 0
    local_var = global_var
    # for i in range(1000):
    for i in range(10):
        # ans += global_var * i
        ans += local_var * i
    return print(ans)

iterative_func()