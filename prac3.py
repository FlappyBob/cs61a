def square_root_update(x, a):
    return (x + a/x) / 2

def cube_root_update(x, a):
    return (2*x + a/ (x*x))/3

def approx_eq(x, y, epi = 1e-15):
    return abs(x -y) < epi    

def square_root(a):
    return improve_eq(lambda x: square_root_update(x, a),
               lambda x: approx_eq(x*x, a))

def cube_root(a):
    def update(x):
        return cube_root_update(x, a)
    def close(x):
        return approx_eq(pow(x, 3), a)
    return improve_eq(update, close)

def improve_eq(update, close, guess = 1, max_update = 100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1
    return guess
