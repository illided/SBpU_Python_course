from typing import Callable, List
from collections import OrderedDict
import functools
import copy
import inspect


class Evaluated:
    eval_func: Callable

    def __init__(self, eval_func):
        self.eval_func = eval_func


class Isolated:
    pass


def get_keyword_defaults(function) -> dict:
    signature = inspect.signature(function)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty and v.kind == inspect.Parameter.KEYWORD_ONLY
    }


class SmartArgs:
    function: Callable
    evaluated_kwargs: dict
    isolated_kwargs: List[str]

    def __init__(self, function: Callable):
        self.function = function
        defaults_kwargs = get_keyword_defaults(function)
        evaluated_kwargs, isolated_kwargs = {}, []
        for key, value in defaults_kwargs.items():
            if isinstance(value, Evaluated):
                evaluated_kwargs[key] = value.eval_func
            elif isinstance(value, Isolated):
                isolated_kwargs.append(key)
        self.isolated_kwargs = isolated_kwargs
        self.evaluated_kwargs = evaluated_kwargs

    def __call__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key in self.isolated_kwargs:
                kwargs[key] = copy.deepcopy(kwargs[key])
        for key, func in self.evaluated_kwargs.items():
            if key not in kwargs:
                kwargs[key] = func()
        return self.function(*args, **kwargs)
