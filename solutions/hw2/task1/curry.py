from typing import Callable


def curry_explicit(func: Callable, arity: int) -> Callable:
    """
    Currying - transformation of a function from many arguments into a set
    of functions, each of which is a function from one argument.
    When called with function f return f_0 from the function set,
    and f_0(arg) will return f_1.
    Function f_arity will return f(*args).

    :param func: function to curry
    :param arity: arity of the function. Also determines the length of the set
    :return: function f_0 from the description
    """

    def insert(arg, function) -> Callable:
        return lambda *args: function(arg, *args)

    def inner(arg):
        return curry_explicit(insert(arg, func), arity - 1)

    if arity == 0 or arity == 1:
        return func
    elif arity < 0:
        raise TypeError("Arity can't be negative")
    return inner


def uncurry_explicit(func: Callable, arity: int) -> Callable:
    """
    Inverse of curry explicit function.
    When called on function f_i with declared arity n will return function
    F with arity n-i.

    :param func: function to uncurry
    :param arity: arity declared previously
    :return: function F from the description
    """

    def wrapper(*args):
        check_num_of_args(args)
        return calculate_from_curried_func(args)

    def check_num_of_args(args):
        if len(args) != arity:
            raise TypeError("Wrong number of arguments or wrong arity")

    def calculate_from_curried_func(args):
        if arity == 0:
            return func()
        output = func
        for i in range(arity):
            if not callable(output):
                raise TypeError("Declared arity was too big")
            output = output(args[i])
        return output

    return wrapper
