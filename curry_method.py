"""Curried function :  use higher-order functions to convert a function
 that takes multiple arguments into a chain of functions that each take
  a single argument
  
  specifically, we can create a new function g(x)(y) that is equivalent to the function f(x, y)"""


def curried_func(x):
    def g(y):
        return pow(x, y)
    return g 

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

map_to_range(1, 10, curried_func(2))