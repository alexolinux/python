"""
Filtering odd numbers from list
"""

def purify(num_list):
    odds = []

    for item in num_list:
        if item % 2 == 0:
            odds.append(item)
    return odds

print(purify([1, 2, 3, 4, 5, 6]))