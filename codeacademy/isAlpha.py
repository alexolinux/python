cap = raw_input("Digite um texto qualquer: \n")
check = cap.isalpha()

if check == False:
  print "Contem espaco entre letras/numeros"
else:
  print cap