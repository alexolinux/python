# Funcao removedora de Vogais.

def anti_vowel(text):
	fmt = ""
	vowel = "aeiouAEIOU"
	
	for c in text:
		if c not in vowel:
			fmt += c
	return fmt
	
print(anti_vowel("Python!"))