
def double(x):
    return x + x
 
def halve(x):
    return (x / 2)

def even(x):
    if x % 2 == 0:return True
    else:return False

def muliter(a, b, aa):
    if b == 0:
        return aa
    elif even(b):
        return muliter(double(a), halve(b), aa)
    else:
        return muliter(a, b-1, (aa + a))

def mul(a, b):
  return muliter(a, b , 0)

print mul(2, 3)
print mul(2, 4)
