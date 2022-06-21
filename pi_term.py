''' About converging function to pi'''
from operator import mul

def pi_term(l):
    return 8 / mul(4 * l - 3, 4 * l - 1)

def summation(n, term):
    total, k = 0, 1
    while k < n:
        total += term(k)
        k += 1
    return total