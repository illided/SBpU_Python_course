import datetime
from copy import deepcopy
import functools
from typing import List, Dict, Any, Callable, Type


class Spy:
    launch_times: "List[Type[datetime]]"
    kwargs_history: List[Dict[str, Any]]

    def __init__(self, function: Callable):
        self.kwargs_history = []
        self.launch_times = []
        self.function = function
        self.__name__ = function.__name__
        functools.update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        cached_kwargs = deepcopy(kwargs)
        cached_kwargs.update(zip(self.function.__code__.co_varnames, args))
        self.kwargs_history.append(cached_kwargs)
        self.launch_times.append(datetime.datetime.now())
        return self.function(*args, **kwargs)

    def clear(self):
        self.kwargs_history.clear()
        self.launch_times.clear()


def print_usage_statistic(spy: Spy):
    if not isinstance(spy, Spy):
        raise TypeError("Can't load statistic without spy decorator")
    for time, kwarg in zip(spy.launch_times, spy.kwargs_history):
        yield time, kwarg
