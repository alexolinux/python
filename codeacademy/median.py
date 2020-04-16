"""
Compute the median of a collection of values from list
"""

#Empty list
data = []
value = input("Enter a value (blank line to quit: )")

# Reading values until a blank line is entered.
while value != "":
    value = float(value)
    data.append(value)

    value = input("Enter another value (blank line to quit: )")

# Sort values
data.sort()

# Compute de median and display it.
if len(data) == 0:
    print("No values were entered.\nBye!")
elif len(data) % 2 == 1:
    # The median is the middle element (if number of elements is odd)
    median = data[len(data) // 2]
    print("\nODD elements\nThe median of those values is ", median)
else:
    # The median is the average of the two middle elements (even elements)
    median = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    print("\nEVEN elements\nThe median of those values is ", median)
