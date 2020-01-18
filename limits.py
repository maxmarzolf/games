from sympy import limit, Symbol, oo

x = Symbol('x')


def the_limit(random_function):
    return limit(random_function, 0, oo, '+')
