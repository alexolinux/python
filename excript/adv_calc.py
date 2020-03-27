

# Testando calculos com potenciação & raiz.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print("Tipo de operação")
op = input("1. Digite <1> para potência\n2. Digite <2> para raiz quadrada\n->")

if(op == '1'):
    res = float(n1 ** n2)
    print("Potência de %.2f elevado a %.2f é %.2f" %(n1, n2 ,res))
elif(op == '2'):
    res = float(n1 ** 0.5)
    print("Raiz Quadrada de %.f é %.4f" %(n1, res))
else:
    print("Entrada Inválida!\nBye! Bye!")
