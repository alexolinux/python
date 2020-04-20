from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

#Uncomment below to check the code (exposing therandom number)
#print random_number

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess (the number is between 1-10): "))

  if guess == random_number:
    print("You win!")
    break
  else:
    guesses_left -= 1
    print("You wrong. There is %i more left." % guesses_left)

else:
  print("\nNo more attempts.\nGame Over")