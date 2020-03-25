print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: \n")
content = original.title()
#content = len(original)

if len(content) > 0:
  print("Conteudo '%s' existente!" % content)
  print("Tamanho: \n %i" % len(content))
else:
	print("Conteudo Vazio.")