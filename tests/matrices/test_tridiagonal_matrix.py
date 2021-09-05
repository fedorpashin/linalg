from linalg.matrices.tridiagonal import TridiagonalMatrix

from typing import Final

import unittest


class TestTridiagonalMatrix(unittest.TestCase):
    a: Final = [1, 2]
    b: Final = [1, 2]
    c: Final = [1, 2, 3]
    matrix = TridiagonalMatrix(a, b, c)

    def test_value(self):
        self.assertEqual(self.matrix.a, self.a)
        self.assertEqual(self.matrix.b, self.b)
        self.assertEqual(self.matrix.c, self.c)

    def test_n(self):
        self.assertEqual(self.matrix.n, 3)
