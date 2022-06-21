"""Higher Order Function"""

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def pi_term(k):
    return 8/ ((4 * k - 3) * (4 * k - 1))

def summation(k, term):
    """sum the first N numbers of a sequence

    >>> summation(5, cube)
    225 
    """
    # Take the name of the function as an argument
    total, n = 0, 1
    while n <= k:
        total, k = total + term(k), n + 1
    return total 

def sum_natural(k):
    """Sum the natural number of the first N numbers 
    >>> sum_natural(5)
    15
    """
    return summation(k, identity) # Take the name of the function as an argument

def sum_cubes(k):
    """Sum the first N cubes of the first N numbers
    >>> sum_cubes(5)
    225
    """
    return summation(k, cube)
