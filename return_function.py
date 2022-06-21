# make function make_adder the return value of another function

def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(3)
    6
    """
    def adder(k):
        return n + k
    return adder 

