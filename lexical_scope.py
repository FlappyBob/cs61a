def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    ''' of which is never being called'''
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)
