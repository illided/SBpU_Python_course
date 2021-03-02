import unittest
from solutions.hw1.task1.vectors import *
from math import pi


class MyTestCase(unittest.TestCase):
    def test_scalar_when_vectors_correct(self):
        self.assertEqual(3, scalar([1, 1, 1], [1, 2, 0]))

    def test_scalar_when_vectors_have_different_length(self):
        self.assertRaises(TypeError, scalar, [1, 0], [1, 0, 0])

    def test_module(self):
        self.assertEqual(5, module([3, 4]))

    def test_angle(self):
        self.assertEqual(pi / 2, angle([1, 0], [0, 1]))

    def test_get_vector_sum_2_vectors_same_length(self):
        self.assertEqual([1, 1], get_vector_sum([1, 0], [0, 1]))

    def test_get_vector_sum_2_vectors_different_length(self):
        self.assertRaises(TypeError, get_vector_sum, [1, 0, 0], [1, 0])

    def test_get_vector_sum_many_vectors_same_length(self):
        self.assertEqual(
            [1, 1, 1, 1, 1],
            get_vector_sum([1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]),
        )

    def test_get_vector_sum_many_vectors_different_length(self):
        self.assertRaises(
            TypeError, get_vector_sum, [1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0]
        )


if __name__ == "__main__":
    unittest.main()
