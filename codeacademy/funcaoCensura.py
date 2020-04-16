"""
This function catches a sentence and filters word to changing letters for stars
"""

def censor(text, word):
    #Separate words in a phrase
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0

    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print censor("this hack is wack hack", "hack")