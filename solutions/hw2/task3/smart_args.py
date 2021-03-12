from typing import Callable, List, Dict, Any
import copy
import inspect


class Evaluated:
    def __init__(self, eval_func: Callable[[], Any]):
        self.eval_func = eval_func
        self.check_for_mixed_usage()

    def check_for_mixed_usage(self):
        if self.eval_func is Isolated:
            raise TypeError("Can't use evaluated and isolated together")


class Isolated:
    pass


def get_keyword_defaults(function) -> Dict[str, Any]:
    signature = inspect.signature(function)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty and v.kind == inspect.Parameter.KEYWORD_ONLY
    }


def get_isolated_kwargs_names(keyword_defaults) -> List[str]:
    isolated_kwargs_names = []
    for key, value in keyword_defaults:
        if isinstance(value, Isolated):
            isolated_kwargs_names.append(key)
    return isolated_kwargs_names


def get_evaluated_kwargs_name_function_pairs(keyword_defaults) -> Dict[str, Callable[[], Any]]:
    evaluated_kwargs_name_function_pairs = {}
    for key, value in keyword_defaults:
        if isinstance(value, Evaluated):
            evaluated_kwargs_name_function_pairs[key] = value.eval_func
    return evaluated_kwargs_name_function_pairs


class SmartArgs:
    evaluated_kwargs: Dict[str, Callable[[], Any]]
    isolated_kwargs: List[str]

    def __init__(self, function: Callable):
        self.function = function
        all_keyword_defaults = get_keyword_defaults(self.function).items()
        self.isolated_kwargs = get_isolated_kwargs_names(all_keyword_defaults)
        self.evaluated_kwargs = get_evaluated_kwargs_name_function_pairs(all_keyword_defaults)

    def __call__(self, *args, **kwargs):
        self.replace_isolated_with_copies(kwargs)
        self.fill_with_evaluated(kwargs)
        return self.function(*args, **kwargs)

    def replace_isolated_with_copies(self, kwargs):
        for key, value in kwargs.items():
            if key in self.isolated_kwargs:
                kwargs[key] = copy.deepcopy(kwargs[key])

    def fill_with_evaluated(self, kwargs):
        for key, func in self.evaluated_kwargs.items():
            if key not in kwargs:
                kwargs[key] = func()
