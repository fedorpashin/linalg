from linalg.factories.default_algorithm import DefaultAlgorithm
from linalg.systems.common.common_system import CommonSystem
from linalg.vector import Vector
from linalg.matrices.common_square import CommonSquareMatrix
from linalg.matrices.tridiagonal import TridiagonalMatrix
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.systems.common.default_common_system_algorithm import DefaultCommonSystemAlgorithm
from linalg.systems.tridiagonal_matrix.default_tridiagonal_matrix_algorithm import DefaultTridiagonalMatrixSystemAlgorithm  # noqa

import unittest


class TestDefaultAlgorithm(unittest.TestCase):
    def test_common_system(self):
        self.assertEqual(
            DefaultAlgorithm(
                CommonSystem(
                    CommonSquareMatrix(
                        [[1, 2],
                         [3, 4]]
                    ),
                    Vector(
                        [1, 2]
                    )
                )
            ),
            DefaultCommonSystemAlgorithm()
        )

    def test_tridiagonal(self):
        self.assertEqual(
            DefaultAlgorithm(
                TridiagonalMatrixSystem(
                    TridiagonalMatrix(
                        [1, 2],
                        [3, 4],
                        [5, 6, 7]
                    ),
                    Vector(
                        [1, 2, 3]
                    )
                )
            ),
            DefaultTridiagonalMatrixSystemAlgorithm()
        )
