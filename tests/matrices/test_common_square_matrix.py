from linalg.matrices.common_square_matrix import CommonSquareMatrix

from typing import Final

import unittest


class TestCommonSquareMatrix(unittest.TestCase):
    value: Final = (
        [[1, 2],
         [3, 4]]
    )
    matrix: Final = CommonSquareMatrix(value)

    def test_value(self):
        self.assertEqual(
            self.matrix.value,
            self.value
        ),

    def test_n(self):
        self.assertEqual(self.matrix.n, 2)

    def test_invalid_matrix(self):
        with self.assertRaises(AssertionError):
            CommonSquareMatrix(
                [[1, 2, 3],
                 [4, 5, 6]]
            )
