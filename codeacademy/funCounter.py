"""
This function returns the number of occurs of an item
"""

def count(sequence, item):
    occur = 0

    for i in sequence:
        if i == item:
            occur += i
    return occur

print(count([1,2,1,3,4,1], 1))