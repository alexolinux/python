# Double, triple, square root

n = float(input('Enter with a number:\t'))

print('The double of {} is {}'.format(n, (n * 2)))
print('The triple of {} is {}'.format(n, (n * 3)))
print('The square root of {} is {:.2f}'.format(n, (n ** 0.5)))

# *The smart alternative for calculating pow:
# pow(n, (0.5))