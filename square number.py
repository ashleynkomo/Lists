def generate_squares(a):
    for x in a:
        yield x**2 

# this is equivalent to above
b = (x**2 for x in a)
