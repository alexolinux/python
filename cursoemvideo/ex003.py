# Primitives Types in Python
# https://youtu.be/hdDHg1p3YVc
# Python has four primitive variable types:
# Integers.
# Float.
# Strings.
# Boolean.

# * Aggregating from Curso em Video playlist exercises 003 + 004 and solving here.
user = input('Enter with user: \n')
n1 = int(input('Enter with a first number: \n'))
n2 = int(input('Enter with a second number: \n'))

result = n1 + n2

#print('The sum between', n1, 'and', n2, 'is', result)
print('Replying to {0}, the sum between {1} and {2} is {3}\n'.format(user, n1, n2, result))

print('Primitive type of n1: ', type(n1))
print('Primitive type of n2: ', type(n2))
print('Primitive type of result: ', type(result))

print('\nExtra Informations:\n')
print('Primitive type of user: ', type(user))
print('user content is only spaces? ', user.isspace())
print('user content is numeric? ', user.isnumeric())
print('user content is alpha? ', user.isalpha())
print('user content is alphanumeric? ', user.isalnum())
print('user content is in lowcase? ', user.islower())
print('user content is in uppercase? ', user.isupper())
print('user content is capitalized? ', user.istitle())