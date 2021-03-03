import unittest
from solutions.hw1.task1.matrices import Matrix, transpose


class MyTestCase(unittest.TestCase):
    def test_get_dimensions(self):
        self.assertEqual({"rows": 3, "columns": 2}, Matrix([1, 8], [-6, 2], [2, 2]).get_dimensions())

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
        self.assertRaises(TypeError, Matrix.__add__, Matrix([0, 1]), Matrix([1, 0, 1]))

    def test_multiplication_valid_for_mul_matrices(self):
        self.assertEqual(
            Matrix([9, -49, -28], [-4, -56, -32], [4, 0, 0]),
            Matrix([1, 8], [-6, 2], [2, 2]) * Matrix([1, 7, 4], [1, -7, -4]),
        )

    def test_multiplication_non_valid_for_mul_matrices(self):
        self.assertRaises(
            TypeError, Matrix.__mul__, Matrix([1, 7, 4], [1, -7, -4]), Matrix([1, 8], [-6, 2], [2, 2], [0, 0])
        )

    def test_transpose_not_in_place(self):
        self.assertEqual(Matrix([1, 2, 3], [4, 5, 6]), transpose(Matrix([1, 4], [2, 5], [3, 6])))

    def test_transpose_in_place(self):
        a = Matrix([1, 2, 3], [4, 5, 6])
        transpose(a, in_place=True)
        self.assertTrue(Matrix([1, 4], [2, 5], [3, 6]) == a)


if __name__ == "__main__":
    unittest.main()
