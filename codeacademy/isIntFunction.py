"""
Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.
"""
def is_int(x):
    if x == int(x):
        return True
    else:
        return False

print(is_int(11.3))