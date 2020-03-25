# PYTHON NOTES #
# ONDE ESTOU:	CONDITIONALS & CONTROL FLOW (or)

# Access by Index #-------------------------
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""

* OBS.: "Methods that use dot notation only work with strings."
my_string = "thoughtness"
print len(my_string)
print my_string.upper()

# String Formatting with % #-------------------------
name = "Mike"
print "Hello %s" % (name)

# TIP CALCULATOR ####################################
#https://www.youtube.com/watch?v=eGIEBz5cC4Q

# BOOLEAN TYPE EXAMPLE ---------------------------------
# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True
three = 19 <= 19
print "Booleano: ", three
	Booleano:  True		<-- Print Result.

# Make me false!
	bool_two = 188 < (189 - 2)
	print bool_two
	false 				<-- Print Result.

	OBS.:
		Use at least three different ones!
		Don't just use True and False! That's cheating!

# Logical "OR" and Boolean Types

	bool_two = 50 == 200 / 4 or 10 > 4
	print bool_two		<-- Print Result.

	bool_three = 100 ** 0.5 >= 50 or False
	print bool_three	<-- Print Result.

# Logical Not: The boolean operator not returns 
# True for false statements and False for true statements.

	EX.:	bool_five = 10 > 8+2 or not not False
			# is not not False (it's True!)
			print bool_five		<-- Print Result.

# This and That (or This, But Not That!).
	# OBS.:	(Reorder your "()")
	
	1.	not is evaluated first;
	2.	and is evaluated next;
	3.	or is evaluated last.

	EX.: bool_one = False or not True and True
		 print bool_one
		 	False 		<-- It is the result.

		 bool_four = not not True or False and not True
		 print bool_four
		 	True 		<--	It is the result.

# Função de Estudo do Controle de Fluxo.

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)