pyg = 'ay'

# Esta é a Entrada.
print("Welcome to PigLatin Game!")
original = input('Enter a word:')

# Condição verificadora:
# - Se String for maior que Zero.
# - Se String for Alfanumérica.
if len(original) > 0 and original.isalpha():
  word = original.lower()
  # VAR: Primeira Letra da String.
  first = word[0]
  # VAR: Concatena Strings.
  new_word = word + first + pyg

  # VAR: Começa a partir da Segunda
  # letra da String, após transformacoes
  # sofridas nas Variáveis Anteriores.
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
    print('empty')
