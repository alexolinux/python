"""
For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
"""

def digit_sum(n):
    total = 0
    string_n = str(n)
    for char in string_n:
        total += int(char)
    return total


# Alternate Solution:

# def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total

print(digit_sum(1234))