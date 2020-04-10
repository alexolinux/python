''''
Boolean operators aren’t just evaluated from left to right.
Just like with arithmetic operators, there’s an order
of operations for boolean operators:

 1. "not" is evaluated first;
 2. "and" is evaluated next;
 3. "or" is evaluated last.
'''

bool_one = False or not True and True
print(bool_one)

bool_two = False and not True or True
print(bool_two)

bool_three = True and not (False or False)
print(bool_three)

bool_four = not not True or False and not True
print(bool_four)

bool_five = False or not (True and True)
print(bool_five)