from linalg.solution import Solution
from linalg.systems.tridiagonal_matrix.thomas_algorithm import ThomasAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.matrices.tridiagonal_matrix import TridiagonalMatrix
from linalg.vector import Vector

from typing import Final

import unittest


class TestSolution(unittest.TestCase):
    system: Final = TridiagonalMatrixSystem(
        TridiagonalMatrix(
            [1, 2],
            [1, 2],
            [1, 2, 3]
        ),
        Vector([4, 5, 6])
    )

    def test_value(self):
        self.assertEqual(
            Solution(
                self.system,
                ThomasAlgorithm()
            ).value,
            ThomasAlgorithm().solution(self.system).value
        )

    def test_repr(self):
        solution = Solution(self.system)
        self.assertEqual(
            solution.__repr__(),
            solution.value.__repr__()
        )
