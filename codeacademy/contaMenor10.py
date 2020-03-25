# Esta Função faz a contagem dos números menores que 10.
def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      print 'Menor que 10 em lista lotto: ', n
      total = total + 1
  return total

# Lista lotto será usada para contagem de números
# Na função count_small.
lotto = [4, 8, 15, 16, 23, 42]
print 'lista lotto: ', lotto
small = count_small(lotto)
print small
