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


class CacherTests(unittest.TestCase):
    def tearDown(self) -> None:
        sum_two_numbers.clear_cache()
        sum_arbitrary_amount_of_numbers.clear_cache()
        join_to_string.clear_cache()
        end_string.clear_cache()

    def test_calling_with_zero_cache(self):
        self.assertEqual(0, len(end_string.get_cache()))

    def test_with_two_positional_arguments(self):
        sum_two_numbers(4, 5)
        self.assertEqual("Given: ((4, 5), {}) Returned: 9", sum_two_numbers.last_call_info())

    def test_with_two_named_arguments(self):
        sum_two_numbers(a=4, b=5)
        self.assertEqual("Given: ((), {'a': 4, 'b': 5}) Returned: 9", sum_two_numbers.last_call_info())

    def test_with_arbitrary_num_of_arguments(self):
        sum_arbitrary_amount_of_numbers(1, 2, 3, 4, 5)
        self.assertEqual("Given: ((1, 2, 3, 4, 5), {}) Returned: 15", sum_arbitrary_amount_of_numbers.last_call_info())

    def test_with_one_positional_and_some_optional_arguments(self):
        join_to_string(".", "hello", "world")
        self.assertEqual("Given: (('.', 'hello', 'world'), {}) Returned: hello.world", join_to_string.last_call_info())

    def test_with_argument_by_default(self):
        end_string("hello")
        self.assertEqual("Given: (('hello',), {}) Returned: hello.", end_string.last_call_info())

    def test_with_unnamed_argument_by_default_but_filled_manually(self):
        end_string("hello", " world!")
        self.assertEqual("Given: (('hello', ' world!'), {}) Returned: hello world!", end_string.last_call_info())

    def test_with_named_argument_by_default_but_filled_manually(self):
        end_string("hello", ending=" world!")
        self.assertEqual(
            "Given: (('hello',), {'ending': ' world!'}) Returned: hello world!", end_string.last_call_info()
        )

    def test_getting_correct_num_of_cache_values(self):
        for i in range(10):
            sum_two_numbers(i, i)
        self.assertEqual(2, len(sum_two_numbers.get_cache()))

    def test_trying_to_call_with_negative_num_of_cache_calls(self):
        with self.assertRaises(TypeError):

            @FunctionCacher(maximum_num_of_caches=-100)
            def inner():
                return "hello"

    def test_trying_to_call_with_zero_maximum_num_of_cache(self):
        with self.assertRaises(TypeError):

            @FunctionCacher(maximum_num_of_caches=0)
            def inner():
                return "hello"


if __name__ == "__main__":
    unittest.main()
