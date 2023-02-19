# Arithmetic operators
#-- Precedence Order:
# 1.  ()
# 2.  **
# 3.  * / //  %
# 4.  + -

n1 = float(input('Enter with a number: \t'))
n2 = float(input('Enter with a number: \t'))

print('Choose your operator: \n')
print('\nEnter "+" for sum\n')
print('Enter "-" for subtraction\n')
print('Enter "*" for multiplication\n')
print('Enter "/" for division\n')
print('Enter "//" for division\n')
print('Enter "%" for module\n')

op = (input('\nInput the operator:\n'))

def calculator(n1, n2, op):
  if op == '+':
    return n1 + n2
  elif op == '-':
    return n1 - n2
  elif op == '*':
    return n1 * n2
  elif op == '/':
    return n1 / n2
  elif op == '//':
    return n1 // n2
  elif op == '%':
    return n1 % n2
  else:
    print('Input string is not valid.')
    return False

print(calculator(n1, n2, op))
