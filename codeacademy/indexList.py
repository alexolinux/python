# Handling with indexes in the python list

animals = ["mouse", "dog", "duck", "dolphin", "fennec fox"]

# Use index() to find "duck"
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")

print(animals) # Observe what prints after the insert operation