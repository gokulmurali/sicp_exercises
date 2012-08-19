def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def productnum(v, a, b, c):
    if a > b:
        return v
    elif even(c) or c == 0 or a == b:
        return productnum(v*a, a+2, b, c+1)
    else:
        return productnum(v*a, a, b, c+1)

def productden(v, a, b, c):
    if a > b:
        return v
    elif even(c):
        return productden(v*a, a+2, b, c+1)
    else:
        return productden(v*a, a, b, c+1)

def pi(n):
    x = productnum(1, 2, n, 0)
    y = productden(1,3, n-1,1)
    return 4 * ((x+.00)/y) 
    #return (4 * (productnum(1,2,n,0) / productden(1, 3, n-1, 1)))

def check(n):
    if even(n):
        return pi(n)
    else:
        return pi(n-1)


print check(8)
print check(100)
print check(125)
print check(150)
print check(171)
