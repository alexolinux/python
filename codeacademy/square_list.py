# Disordered list
start_list = [5, 3, 1, 2, 4]

# New empty list for subsequent use in 'for loop'
square_list = []

# Your code here!
for number in start_list:
  # Vai adicionando a potência dos números da lista
  # start_list p/ square_list, ordenando-a no final
  # portanto, fora da identação (o sort...).
  square_list.append(number ** 2)
square_list.sort()

print square_list
