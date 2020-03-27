# Verificacao se resultado e Verdadeiro ou Falso

n1 = float(input('Informe um numero:\n'))
n2 = float(input('Informe outro numero:\n'))

if (n1 != n2):
    if (n1 > n2):
        print('Primeiro numero é maior: %.2f' %n1)
    else:
        print('Segundo numero é maior: %.2f' %n2)
else:
    print('Os números são iguais.')
