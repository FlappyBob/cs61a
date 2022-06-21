def approx_eq(x, y, epi = 1e-15):
    return abs(x - y) < epi    

def improve_eq(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def find_zero(f, df): # These two inputs are all functions
    def near_zero(x):
        return approx_eq(f(x), 0)
    def newton_update(x):
        return x - f(x) / df(x)
    return improve_eq(newton_update, near_zero)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def root(n, a):
    return find_zero(lambda x: power(x, n) - a,
                     lambda x: n * power(x, n - 1))
