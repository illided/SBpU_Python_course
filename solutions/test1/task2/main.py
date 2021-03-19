from takes import *


@takes(types=[int, int])
def return_sum(x, y, z=6):
    return x + y + z


def main():
    return_sum(8, 0, z=9)


if __name__ == "__main__":
    main()
