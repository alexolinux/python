# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  # *OBS: Atenção para o 'return', Ele deverá estar
  # Fora do loop for.
  return count

# Lista para ser utilizada.
str_list = ["pig", "fizz", "cat", "bat", "fizz", "bitch"]
cata_fizz = fizz_count(str_list)
print 'Total da String FIZZ: ', cata_fizz, 'encontrado(s).'
