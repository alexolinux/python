import random
"""
1.  Computer pick a random Number
2.  Player makes a guess
3.  Compare guess to the number
4.  Print out "Too High...", "Too Low...", "You got it""
"""

secret = random.randrange(1, 101)
#print(secret)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Make a guess: "))
    tries += 1

    if guess < secret:
        print("Too Low...")
    elif guess > secret:
        print("Too High...")
    else:
        print("You Got It!")
        if tries <= 3:
            print("Excellent: Just %d tries" % tries)
        elif tries > 3 and tries <= 9:
            print("You needed %d tries, try a better performance.." % tries)
        else:
            print("So bad, so slow..: It took %d times to find something...." % tries)