import unittest

from solutions.hw2.task1.curry import curry_explicit, uncurry_explicit


def return_three_things_in_a_string(x, y, z):
    return f"{[x, y, z]}"


def return_itself(x):
    return x


def return_eight():
    return 8


def multiply_all(*args):
    result = 1
    for x in args:
        result = result * x
    return result


class CurryingTest(unittest.TestCase):
    def test_correct_currying(self):
        g = curry_explicit(return_three_things_in_a_string, 3)
        self.assertEqual("[1, 2, 3]", g(1)(2)(3))

    def test_too_small_currying(self):
        g = curry_explicit(return_three_things_in_a_string, 2)
        with self.assertRaises(TypeError):
            g(1)(2)(3)

    def test_too_big_currying(self):
        g = curry_explicit(return_three_things_in_a_string, 5)
        with self.assertRaises(TypeError):
            g(1)(2)(3)(4)(5)

    def test_one_to_one_currying(self):
        g = curry_explicit(return_itself, 1)
        self.assertEqual(10, g(10))

    def test_zero_to_zero_currying(self):
        g = curry_explicit(return_eight, 0)
        self.assertEqual(8, g())

    def test_calling_with_no_arguments_when_non_zero_arity(self):
        g = curry_explicit(return_itself, 1)
        with self.assertRaises(TypeError):
            g()

    def test_calling_with_negative_currying(self):
        with self.assertRaises(TypeError):
            curry_explicit(return_three_things_in_a_string, -100)

    def test_infinite_arity(self):
        curried_product_func = curry_explicit(multiply_all, 3)
        self.assertEqual(6, curried_product_func(1)(2)(3))

    def test_with_zero_arity_trying_to_call_two_times(self):
        f0 = curry_explicit(lambda *xs: print(xs), 0)
        with self.assertRaises(TypeError):
            f0()()

    def test_with_zero_arity_trying_to_call_with_argument(self):
        f0 = curry_explicit(lambda *xs: print(xs), 0)
        with self.assertRaises(TypeError):
            f0(1)


class UncurryTest(unittest.TestCase):
    def test_with_no_curried_args(self):
        g = curry_explicit(return_three_things_in_a_string, 3)
        h = uncurry_explicit(g, 3)
        self.assertEqual("[1, 2, 3]", h(1, 2, 3))

    def test_with_curried_args(self):
        g = curry_explicit(return_three_things_in_a_string, 3)(1)(2)
        h = uncurry_explicit(g, 1)
        self.assertEqual("[1, 2, 3]", h(3))

    def test_declared_arity_too_big(self):
        g = curry_explicit(return_three_things_in_a_string, 3)
        h = uncurry_explicit(g, 5)
        with self.assertRaises(TypeError):
            h(1, 2, 3, 4, 5)

    def test_infinite_arity(self):
        curried_product_func = curry_explicit(multiply_all, 3)
        uncurried_product_func = uncurry_explicit(curried_product_func, 3)
        with self.assertRaises(TypeError):
            uncurried_product_func(1, 2, 3, 4)

    def test_with_zero_arity_correct_call(self):
        f = curry_explicit(return_eight, 0)
        g = uncurry_explicit(f, 0)
        self.assertEqual(8, g())


if __name__ == "__main__":
    unittest.main()
