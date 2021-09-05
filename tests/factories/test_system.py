from linalg.factories.system import System
from linalg.vector import Vector
from linalg.systems.common.common_system import CommonSystem
from linalg.matrices.common_square import CommonSquareMatrix
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.matrices.tridiagonal import TridiagonalMatrix

import unittest


class TestSystem(unittest.TestCase):
    def test_common(self):
        self.assertEqual(
            type(System(
                CommonSquareMatrix(
                    [[1, 2],
                     [3, 4]]
                ),
                Vector([1, 2])
            )),
            CommonSystem
        )

    def test_tridiagonal_matrix(self):
        self.assertEqual(
            type(System(
                TridiagonalMatrix(
                    [1, 2],
                    [3, 4],
                    [5, 6, 7]
                ),
                Vector([1, 2])
            )),
            TridiagonalMatrixSystem
        )
