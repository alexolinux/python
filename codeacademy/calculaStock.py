# About Dictioraries:
# dict = {"key" : value}


# Estudo para percorrer listas e calcular quantidade e valor de produtos.
# O desafio fica para calcular o valor total de produtos em estoque.

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana" : 4,
  "apple" : 2,
  "orange" : 1.5,
  "pear"	:	3  
}
print ('Dict prices has'), len(prices), 'price items.\n'

# Deve-se criar esta variável zerada para ser utilizada
# futuramente para calcular o valor total dos produtos
# em estoque. O esquema é criar fora do loop...

total = 0

for product in prices:
  print product
  print "Price: %.2f" % prices[product]
  print "Stock: %d" % stock[product]
  total_by_product = prices[product] * stock[product]
  total += total_by_product
  
  print
  print 'Valor Total de', product, '= R$', total_by_product
  print

print "Valor Total: ", total
