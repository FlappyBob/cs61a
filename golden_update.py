def improve_eq(update, close, guess = 1):
    while not (close(guess)):
        print(guess)
        guess = update(guess)
    return guess

def approx_eq(x, y, epi = 1e-15):
    return abs(x - y) < epi

def golden_update(guess):
    return 1 + 1 / guess

def golden_close(guess):
    return approx_eq(guess * guess, guess + 1)

def golden_output():
    return improve_eq(golden_update, golden_close)


