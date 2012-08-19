def squre(n):
    return n * n

def fibiter(a, b, p, q, count):
    if count == 0:
        return b
    elif count % 2 == 0:
        
        return fibiter(a, b, (squre(q) + squre(p)), ((2 * p) * q) + (q * q), (count / 2))
    else:
        return fibiter(((b * q) + (a * q) + (a * p)), ((b * p)+( a * q)), p, q, (count -1))

def fib(n):
    return fibiter(1,0,0,1,n)


print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(4)
print fib(5)

