from typing import Callable


def curry_explicit(func: Callable, arity: int):
    def insert(arg, function):
        return lambda *args: function(arg, *args)

    def inner(arg=None):
        return curry_explicit(insert(arg, func), arity - 1)

    if arity == 0:
        return func()
    elif arity < 0:
        raise ValueError("Arity can't be negative")
    return inner


def uncurry_explicit(func: Callable, arity: int):
    def inner(*args):
        if len(args) != arity:
            raise ValueError("Wrong number of arguments or wrong arity")
        output = func
        for i in range(arity):
            output = output(args[i])
        return output

    return inner
