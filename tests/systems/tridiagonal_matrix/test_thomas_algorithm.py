from linalg.systems.tridiagonal_matrix.thomas_algorithm import ThomasAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.matrices.tridiagonal_matrix import TridiagonalMatrix
from linalg.vector import Vector

import unittest
from numpy.testing import assert_almost_equal


class TestThomasAlgorithm(unittest.TestCase):
    def test_solution(self):
        assert_almost_equal(
            ThomasAlgorithm().solution(
                TridiagonalMatrixSystem(
                    TridiagonalMatrix(
                        [3, 1, 3],
                        [2, 4, 5],
                        [10, 10, 7, 4],
                    ),
                    Vector([3, 4, 5, 6])
                )
            ).value,
            [0.14877589, 0.75612053, -1.00188324, 2.25141243]
        )
