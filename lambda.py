def compose1_ver_1(f, g):
    return lambda x: f(g(x))

def compose1_ver_2(f, g):
    def h(x):
        return f(g(x))
    return h

""" Those two expressions are basically the same thing but differs in function diagrams."""

# Instruction!!!:
# To put it into https://pythontutor.com/ for better understanding. 