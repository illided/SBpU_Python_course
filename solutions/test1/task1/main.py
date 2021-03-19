from spy import *


@Spy
def foo(num):
    print(num)


if __name__ == "__main__":
    foo(30)
    foo("hello")
    foo(5)

    for (time, parameters) in print_usage_statistic(foo):
        str_parameters = ", ".join(f"{k} = {v}" for k, v in parameters.items())
        print(f"function {foo.__name__} was called at {time} " f"with parameters:\n{str_parameters}")
