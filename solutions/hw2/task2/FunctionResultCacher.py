from typing import List, Any, Tuple, Callable
import functools


class FunctionCache:
    nameless_args: Tuple
    named_args: dict
    result: Any

    def __init__(self, _args: Tuple, _kwargs: dict, _result):
        self.nameless_args = _args
        self.named_args = _kwargs
        self.result = _result


class FunctionResultCacher:
    function: Callable
    maximum_num_of_caches: int
    cache: List[FunctionCache]

    def __init__(self, _function, _maximum_num_of_caches):
        self.function = _function
        self.maximum_num_of_caches = _maximum_num_of_caches

    def __call__(self):
        @functools.wraps(self.function)
        def caching_wrapper(*args, **kwargs):
            result = self.function(*args, **kwargs)
            if self.is_cache_full():
                self.cache.pop()
            self.cache.append(FunctionCache(args, kwargs, result))
            return result

        return caching_wrapper

    def is_cache_full(self):
        return len(self.cache) == self.maximum_num_of_caches
