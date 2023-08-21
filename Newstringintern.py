import sys

a = "hello"
b = "hello"
print(a is b)  # This will print False because string literals are not interned by default

a_interned = sys.intern("hello")
b_interned = sys.intern("hello")
print(a_interned is b_interned)  # This will print True because the strings are interned
