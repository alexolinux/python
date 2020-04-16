"""
Product of integer numbers from list
"""

def product(int_list):
    #1, because must have 1 element at least
    total = 1

    for i in int_list:
        total = total * i
    return total

print(product([3, 2, 4]))