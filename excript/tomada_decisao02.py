#Operadores relacionais comparativos

numero01 = int(input("Digite primeiro número: "))
numero02 = int(input("Digite segundo número: "))

if(numero01 == numero02):
    print("Números %d e %d são iguais" %(numero01, numero02))
else:
    if(numero01 != numero02):
        print("Números %d e %d são diferentes" %(numero01, numero02))
    if(numero01 > numero02):
        print("Número %d maior que %d" %(numero01, numero02))
    if(numero01 < numero02):
        print("Número %d menor que %d" % (numero01, numero02))
