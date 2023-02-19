# Calculating average

student = str(input('Name of student:\n'))
a1 = float(input('First exam grade: \t'))
a2 = float(input('Second exam grade: \t'))

def average(a1, a2):
  av = (a1 + a2) / 2
  return av

print('Student {} obtained the following average: {:.2f}'.format(student, average(a1, a2)))
