
def double(x):
    return x + x

def halve(x):
    return (x/2)

def even(x):
    if x % 2 == 0: return True
    else: return False


def mul(a, b):
    if b == 0:
        return 0
    elif even(b):
        return (double(a * halve(b)))
    else:
        return (a + (a * (b-1)))

print mul(2, 3)
print mul(2, 4)
