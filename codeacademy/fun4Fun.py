"""A function called by another function."""

def cube(number):
    return number ** 3


def by_three(number):
    if (number % 3 == 0):
        return cube(number)
    else:
        return not True

c = int(input("Please a number: \t"))

print(by_three(c))

