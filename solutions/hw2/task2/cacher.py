from typing import List, Any, Tuple, Callable
import functools


class FunctionCache:
    nameless_args: Tuple
    named_args: dict
    result: Any

    def __init__(self, args: Tuple, kwargs: dict, result):
        self.nameless_args = args
        self.named_args = kwargs
        self.result = result

    def __str__(self):
        return f"Given: ({self.nameless_args}, {self.named_args}) Returned: {self.result}"


class _FunctionResultCacher:
    function: Callable
    maximum_num_of_caches: int
    cache: List[FunctionCache]

    def __init__(self, function=None, *, maximum_num_of_caches):
        if maximum_num_of_caches < 1:
            raise TypeError("Can't have empty cache")

        self.function = function
        self.maximum_num_of_caches = maximum_num_of_caches
        self.cache = []

        functools.update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        if self.is_cache_full():
            self.cache.pop(0)
        self.cache.append(FunctionCache(args, kwargs, result))
        return result

    def is_cache_full(self):
        return len(self.cache) == self.maximum_num_of_caches

    def get_cache(self):
        return [str(c) for c in self.cache]

    def clear_cache(self):
        self.cache.clear()


def FunctionCacher(function=None, *, maximum_num_of_caches: int):
    if function:
        return _FunctionResultCacher(function, maximum_num_of_caches=maximum_num_of_caches)
    else:

        def wrapper(func):
            return _FunctionResultCacher(func, maximum_num_of_caches=maximum_num_of_caches)

        return wrapper
