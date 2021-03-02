import unittest
from solutions.hw1.task1.matrices import Matrix, transpose


class MyTestCase(unittest.TestCase):
    def test_get_dimensions(self):
        self.assertEqual({"rows": 3, "columns": 2}, Matrix([0, 1], [0, 1], [0, 1]).get_dimensions())

    def test_eq_two_equal_matrices(self):
        self.assertTrue(Matrix([0, 1], [0, 1]) == Matrix([0, 1], [0, 1]))

    def test_eq_two_different_matrices_with_same_dimensions(self):
        self.assertFalse(Matrix([0, 1], [0, 1]) == Matrix([1, 0], [1, 0]))

    def test_eq_two_different_matrices_with_different_dimensions(self):
        self.assertFalse(Matrix([0, 1]) == Matrix([1, 0], [1, 0]))

    def test_str(self):
        self.assertEqual("[[0, 1], [0, 1]]", str(Matrix([0, 1], [0, 1])))

    def test_addition_matrices_with_same_dimension(self):
        self.assertEqual(Matrix([1, 1], [1, 1]), Matrix([-100, 100], [100, -100]) + Matrix([101, -99], [-99, 101]))

    def test_addition_matrices_with_different_dimensions(self):
        self.assertRaises(TypeError, Matrix.__mul__, Matrix([0, 1]), Matrix([1, 0, 1]))


if __name__ == "__main__":
    unittest.main()
