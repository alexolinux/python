def is_prime(n):
  if n < 2:
    return False
  else:
    for i in range(2, n-1):
      if n % 2 == 0:
        return False
    else:
       return True

print(is_prime(5))
