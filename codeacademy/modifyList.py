# Dada a lista n, a funcao double_list leva
# o argumento x. i itera a lista pelo seu
# tamanho, multiplicando cada elemento por 2
# e retorna a lista alterada.

n = [3, 5, 7]

# Don't forget to return your new list!
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x


print(double_list(n))
