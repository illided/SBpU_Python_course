from takes import *


@takes(types=[int, str])
def f(a, b):
    print(f"Successful call with a={a} and b={b}")


if __name__ == "__main__":
    try:
        f(1, 2)
    except TypeError as e:
        print(e)
    f(1, "ab")
