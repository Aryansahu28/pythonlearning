'''Integer intern is used in programming languages to use the memory better we use integer intern
when the same integer are used many times so we reuse it in the same memory location with 
different variable '''

a = 10
b = 10

print(a is b) #This will print true becaue the memory location of both variable is same


'''String intern has same concept as integer intern but the memory location for the same string 
is different so we have to use the function call sys.intern(). This will provide the same memory
location to the different variable of same content '''

c = "Hello, World!"
d = "Hello, World!"

print(c is d) #This will print False

import sys

c_interned = sys.intern("Hello, World!")
d_interned = sys.intern("Hello, World!")

print(c_interned is d_interned) #This will print True