# Python possui 'tipagem dinâmica'
# Obtemos seu tipo com método <type(VAR)>

num_int = 5
num_dec = 7.3
val_str = "Conteúdo da Variável val_str."

# Formas de exibição do conteúdo de uma variável

# Integer
print("O valor da variavel é:", num_int)
print("O valor da variavel é: %i" %num_int)
print("O valor da variavel é: " + str(num_int))
print("O tipo da variavel é: ", type(num_int))

# Decimal
print("Concatenando decimal:", num_dec)
print("Concatenando decimal: %.2f" %num_dec)
print("Concatenando decimal: " + str(num_dec))
print("O tipo da variavel é: ", type(num_dec))

# String
print("Concatenando string:", val_str)
print("Concatenando string: %s" %val_str)
print("Concatenando string: " + val_str)
print("O tipo da variavel é: ", type(val_str))