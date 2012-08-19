
def fiter(n, n1, n2, n3):
    if n < 3:
        return n1
    else:
        return fiter((n-1), (n1+(2*n2)+(3*n3)), n1, n2)


def f(n):
    if n == 1: return 1
    else:
        return fiter(n, 2, 1, 0)

print f(1)
print f(2)
print f(3)
print f(4)
print f(5)
