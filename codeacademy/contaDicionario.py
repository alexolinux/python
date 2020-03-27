# How can I access a dictionary key value inside of a loop?
# EXPLANATION:
# One approach to writing our scrabble_score() function involves using a for each 
# loop to access the dictionary value of each character in the given word.
# Since we are given a word as a string, we can iterate through it using a for each loop, 
# where each time the loop loops, the loop variable becomes the next character in the string.
# Were also given a dictionary where each key is an alphabetical letter corresponding with a value.
# Convenient!
# Inside of the loop, we can access the value stored in a key by writing dictionary_name[key_name]. 
# That will give us the value of the character, which we can add to some total and return.

# Funcao que retorna valor total de elementos de uma palavra dada como entrada.

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word: object) -> object:
  word = word.lower()
  total = 0
  
  for letter in word:
    for char in score:
      if letter == char:
        total = total + score[char]
  return total

print(scrabble_score("alex"))