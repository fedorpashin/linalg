from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.matrices.tridiagonal import TridiagonalMatrix
from linalg.vector import Vector

from typing import Final

import unittest


class TestTridiagonalMatrixSystem(unittest.TestCase):
    matrix: Final = TridiagonalMatrix(
        [1, 2],
        [1, 2],
        [1, 2, 3]
    )
    vector: Final = Vector([4, 5])
    system: Final = TridiagonalMatrixSystem(matrix, vector)

    def test_value(self):
        self.assertEqual(self.system.matrix, self.matrix)
        self.assertEqual(self.system.vector, self.vector)
