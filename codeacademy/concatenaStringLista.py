# Funcao que concatena Strings de uma Lista.

n = ["Michael", "Lieberman"]

def join_strings(words):
  result = ""
  for i in range(len(words)):
    print (words[i])
    result += words[i]
  return result
  
join_strings(n)