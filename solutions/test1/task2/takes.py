from typing import Callable, List, Dict


def takes(function=None, *, types=List[type]):
    if function:
        return TakesImpl(function, types)

    def wrapper(func):
        return TakesImpl(func, types)

    return wrapper


class TakesImpl:
    type_list: List[type]
    type_dict: Dict[str, type]

    def __init__(self, function: Callable, type_list):
        self.function = function
        self.type_list = type_list
        self.type_dict = dict(zip(function.__code__.co_varnames, type_list))
        print(self.type_dict)

    def __call__(self, *args, **kwargs):
        for i in range(len(args)):
            if i == len(self.type_list):
                raise TypeError("Not for all arguments type was declared")
            if not isinstance(args[i], self.type_list[i]):
                raise TypeError("Argument has type other than declared")
        for kwarg in kwargs:
            if kwarg not in self.type_dict:
                raise TypeError("Not for all arguments type was declared")
            if not isinstance(kwarg, self.type_dict.get(kwarg)):
                raise TypeError("Argument has type other than declared")
        return self.function(*args, **kwargs)
