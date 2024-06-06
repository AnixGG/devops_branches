def plus_plus(n):
    return n + 2

  
def minus_minus(n):
    return n - 2
  

def factorial(n):
    if n == 0:
        return 1
    c = 1
    for i in range(1, n+1):
        c *= i
    return c