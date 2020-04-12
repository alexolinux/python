"""Receive a number and check if is even"""
def isEven(num):
    if num  % 2 == 0:
        print("%i is even" % num)
    else:
        print("Ops... It's not even, boy.")

entrada = int(input("Digit a number: "))

isEven(entrada)