# Funcao de Inversao de String por Loop.

def reverse(text):
  st = ""

  for c in text:
    st = c + st
  return st

print(reverse("Python!"))
