from typing import Callable


def curry_explicit(func: Callable, arity: int):
    def insert(arg, function):
        return lambda *args: function(arg, *args)

    def inner(arg):
        return curry_explicit(insert(arg, func), arity - 1)

    if arity == 0 or arity == 1:
        return func
    elif arity < 0:
        raise TypeError("Arity can't be negative")
    return inner


def uncurry_explicit(func: Callable, arity: int):
    def inner(*args):
        if len(args) != arity:
            raise TypeError("Wrong number of arguments or wrong arity")
        output = func
        for i in range(arity):
            if not callable(output):
                raise TypeError("Declared arity was too big")
            output = output(args[i])
        return output

    return inner
