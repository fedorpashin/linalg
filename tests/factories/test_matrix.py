from linalg.factories.matrix import Matrix
from linalg.matrices.common_matrix import CommonMatrix
from linalg.matrices.common_square_matrix import CommonSquareMatrix
from linalg.matrices.tridiagonal_matrix import TridiagonalMatrix

import unittest


class TestMatrix(unittest.TestCase):
    def test_common(self):
        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [[1, 2, 3],
                     [4, 5, 6]]
                )),
                CommonMatrix
            )

        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [[1., 2., 3.],
                     [4., 5., 6.]]
                )),
                CommonMatrix
            )

    def test_common_square(self):
        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [[1, 2],
                     [3, 4]]
                )),
                CommonSquareMatrix
            )

        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [[1., 2.],
                     [3., 4.]]
                )),
                CommonSquareMatrix
            )

    def test_tridiagonal(self):
        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [1, 2],
                    [3, 4],
                    [5, 6, 7]
                )),
                TridiagonalMatrix
            )

        with self.subTest():
            self.assertEqual(
                type(Matrix(
                    [1., 2.],
                    [3., 4.],
                    [5., 6., 7.]
                )),
                TridiagonalMatrix
            )
