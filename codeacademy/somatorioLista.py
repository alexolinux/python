# Codigo Python como exemplo de utilizacao da
# Funcao que faz o somatario dos valores de uma
# Lista. ATENCAO PARA O "return" FORA DO LOOP
# DO CODIGO ALGORITMICO.
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0, len(numbers)):
    result += numbers[i]
  return result

print total(n)
