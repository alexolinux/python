"""Sort and square calculation of list elements"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for n in start_list:
    sq = n ** 2
    square_list.append(sq)

square_list.sort()

print(square_list)
