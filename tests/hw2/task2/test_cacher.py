import unittest
from solutions.hw2.task2.cacher import FunctionCacher


@FunctionCacher(maximum_num_of_caches=2)
def sum_two_numbers(a: int, b: int):
    return a + b


@FunctionCacher(maximum_num_of_caches=2)
def sum_arbitrary_amount_of_numbers(*args):
    return sum([args])


@FunctionCacher(maximum_num_of_caches=2)
def join_to_string(separator: str, *args):
    return separator.join(args)


class CacherCashContentTests(unittest.TestCase):
    def tearDown(self) -> None:
        sum_two_numbers.clear_cache()
        sum_arbitrary_amount_of_numbers.clear_cache()
        join_to_string.clear_cache()

    def test_with_two_positional_arguments(self):
        sum_two_numbers(4, 5)
        self.assertEqual('Given: ((4, 5), {}) Returned: 9', sum_two_numbers.get_cache()[0])


if __name__ == "__main__":
    unittest.main()
