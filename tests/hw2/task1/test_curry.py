import unittest

from solutions.hw2.task1.curry import curry_explicit, uncurry_explicit


def f(x, y, z):
    return f"{[x, y, z]}"


def return_itself(x):
    return x


def return_eight():
    return 8


class CurryingTest(unittest.TestCase):
    def test_correct_currying(self):
        g = curry_explicit(f, 3)
        self.assertEqual("[1, 2, 3]", g(1)(2)(3))

    def test_too_small_currying(self):
        g = curry_explicit(f, 2)
        with self.assertRaises(TypeError):
            g(1)(2)(3)

    def test_too_big_currying(self):
        g = curry_explicit(f, 5)
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
            curry_explicit(f, -100)


class UncurryTest(unittest.TestCase):
    def test_uncurry_with_no_curried_args(self):
        g = curry_explicit(f, 3)
        h = uncurry_explicit(g, 3)
        self.assertEqual("[1, 2, 3]", h(1, 2, 3))

    def test_uncurry_with_curried_args(self):
        g = curry_explicit(f, 3)(1)(2)
        h = uncurry_explicit(g, 1)
        self.assertEqual("[1, 2, 3]", h(3))

    def test_uncurry_declared_arity_too_big(self):
        g = curry_explicit(f, 3)
        h = uncurry_explicit(g, 5)
        with self.assertRaises(TypeError):
            h(1, 2, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()
