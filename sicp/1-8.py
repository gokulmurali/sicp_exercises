
def improveguess(y, x):
  return ((x / (y * y)) + (2 * y)) / 3

def cube(x):
  return x * x * x

def goodenough(guess, x):
    if (abs(cube(guess) - x)) / guess < 0.0001:
      return True
    else:return False

def cuberootiter(guess, x):
  if goodenough(guess, x):
      return guess
  else:
      return cuberootiter(improveguess(guess, x), x)

def cuberoot(x):
    return cuberootiter(1.0, x)

print cuberoot(8)    
