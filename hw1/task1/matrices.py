from vectors import *
import copy


class Matrix:
    content: List[Vector]

    def __init__(self, first: Vector, *args: Vector):
        if not all(len(first) == len(vector) for vector in args):
            raise TypeError("Rows must be the same length")
        self.content = [first, *args]

    def __str__(self):
        return str(self.content)

    def __add__(self, other):
        return Matrix(*[get_vector_sum(x, y) for x, y in zip(self.content, other.content)])

    def get_dimensions(self):
        return {'columns': len(self.content), 'rows': len(self.content[0])}

    def __mul__(self, other):
        if self.get_dimensions()['rows'] != other.get_dimensions()['columns']:
            raise TypeError("Matrices can't be multiplied")
        new = []
        other_transposed = transpose(other)
        for row in self.content:
            new.append([scalar(row, column) for column in other_transposed.content])
        return Matrix(*new)


def transpose(matrix: Matrix, in_place=False) -> Matrix:
    transposed = [list(t) for t in zip(*matrix.content)]
    if in_place:
        matrix.content = transposed
        transposed = copy.deepcopy(transposed)
    return Matrix(*transposed)
