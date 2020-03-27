# Checagem de idade
# Faixa etaria

idade = int(input("Informe a sua idade: \t"))

if (idade < 18):
    print("Este conteúdo não é permitido para menores.")

else:
    if (idade >= 65 and idade < 150):
        print("Sua entrada é gratuita!")
    elif (idade <= 0 or idade >= 150):
        print("Idade não corresponde à realidade!")
    else:
        print("Você deverá comprar sua entrada no guichê.")