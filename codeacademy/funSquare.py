# -*- coding: UTF-8 -*-

"""'This function return squared number"""

def square(number):
    sqr = number ** 2
    print("%d squared is %d" % (number, sqr))

squared = int(input("Give-me a number now: "))

square(squared)