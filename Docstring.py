# Docstring is only considered when it is written just after the function defined and in the triple inverted commas
def square(n):
    """This is the function for the square and it is a docstring as well"""
    print(n*n)


square(4)
print(square.__doc__)