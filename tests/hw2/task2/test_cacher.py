import unittest
from solutions.hw2.task2.cacher import FunctionCacher


@FunctionCacher(maximum_num_of_caches=2)
def sum_two_numbers(a: int, b: int):
    return a + b


@FunctionCacher(maximum_num_of_caches=2)
def sum_arbitrary_amount_of_numbers(*args):
    return sum(args)


@FunctionCacher(maximum_num_of_caches=2)
def join_to_string(separator: str, *args):
    return separator.join(args)


@FunctionCacher(maximum_num_of_caches=2)
def end_string(string: str, ending: str = "."):
    return string + ending


class CacherTestsForOneCall(unittest.TestCase):
    def tearDown(self) -> None:
        sum_two_numbers.clear_cache()
        sum_arbitrary_amount_of_numbers.clear_cache()
        join_to_string.clear_cache()
        end_string.clear_cache()

    def test_calling_with_zero_cache(self):
        with self.assertRaises(ValueError):
            sum_two_numbers.get_cached_result(1, 2)

    def test_with_two_positional_arguments(self):
        sum_two_numbers(4, 5)
        self.assertEqual(9, sum_two_numbers.get_cached_result(4, 5))

    def test_with_two_named_arguments(self):
        sum_two_numbers(a=4, b=5)
        self.assertEqual(9, sum_two_numbers.get_cached_result(a=4, b=5))

    def test_with_arbitrary_num_of_arguments(self):
        sum_arbitrary_amount_of_numbers(1, 2, 3, 4, 5)
        self.assertEqual(15, sum_arbitrary_amount_of_numbers.get_cached_result(1, 2, 3, 4, 5))

    def test_with_one_positional_and_some_optional_arguments(self):
        join_to_string(".", "hello", "world")
        self.assertEqual("hello.world", join_to_string.get_cached_result(".", "hello", "world"))

    def test_with_argument_by_default(self):
        end_string("hello")
        self.assertEqual("hello.", end_string.get_cached_result("hello"))

    def test_with_unnamed_argument_by_default_but_filled_manually(self):
        end_string("hello", " world!")
        self.assertEqual("hello world!", end_string.get_cached_result("hello", " world!"))

    def test_with_named_argument_by_default_but_filled_manually(self):
        end_string("hello", ending=" world!")
        self.assertEqual("hello world!", end_string.get_cached_result("hello", ending=" world!"))

    def test_trying_to_call_with_negative_num_of_cache_calls(self):
        with self.assertRaises(TypeError):

            @FunctionCacher(maximum_num_of_caches=-100)
            def inner():
                return "hello"


class CacherTestsArbitraryNumOfCalls(unittest.TestCase):
    def test_getting_correct_num_of_cache_values(self):
        sum_two_numbers(0, 0)
        for i in range(10):
            sum_two_numbers(i, i)
        with self.assertRaises(ValueError):
            sum_two_numbers.get_cached_result(0, 0)

    def test_trying_to_call_with_zero_maximum_num_of_cache(self):
        @FunctionCacher(maximum_num_of_caches=0)
        def multiply(a: int, b: int):
            return a*b

        multiply(1, 2)
        with self.assertRaises(ValueError):
            multiply.get_cached_result(1, 2)


if __name__ == "__main__":
    unittest.main()
