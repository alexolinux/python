n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in range(0, len(lists)):
    results += lists[numbers]
  return results
    
 
print flatten(n)