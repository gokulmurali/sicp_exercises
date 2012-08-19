
def fastiter(b, n, a):
    if n == 0:
        return a
    elif n % 2 == 0:
        return fastiter((b * b), (n / 2), a)
    else:
        return fastiter(b,(n - 1),(a * b))

def fast(b, n):
    return fastiter(b, n, 1)

print fast(2, 2)
print fast(2, 3)

