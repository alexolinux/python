'''
Lambda Functions
One of the more powerful aspects of Python is that it allows for a style of programming
called functional programming, which means that you’re allowed to pass functions around
just as if they were variables or values. Sometimes we take this for granted, but not all
languages allow this!

lambda arguments : expression

    lambda x: x % 3 == 0
Is the same as
    def by_three(x):
      return x % 3 == 0

Ex.:
    my_list = range(16)
    print filter(lambda x: x % 3 == 0, my_list)
'''

# Below, a set of lambda usages

languages = ["HTML", "JavaScript", "Python", "Ruby", "Java", "C#"]

# Add arguments to the filter()
print(filter(lambda x: x == "Python", languages))

# Squares from a range
squares = [x ** 2 for x in range(1, 11)]
print(filter(lambda x: x >= 30 and x <= 70, squares))

# Filtering a messy message (It was tested only by Python2.7)
#garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
#message = (filter(lambda x: x != "X", message))
#print(message)