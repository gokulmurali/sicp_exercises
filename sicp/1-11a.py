
def f(n):
    if n < 3:
      return n
    else:
      return (f(n-1) + 2 * (f(n-2)) + 3 * (f(n-3)))


print f(1)
print f(2)
print f(3)
print f(4)
print f(5)
