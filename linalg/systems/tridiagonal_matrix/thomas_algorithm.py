from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_algorithm import TridiagonalMatrixSystemAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.vector import Vector

from dataclasses import dataclass

__all__ = ['ThomasAlgorithm']


@dataclass(frozen=True)
class ThomasAlgorithm(TridiagonalMatrixSystemAlgorithm):
    def solution(self, system: TridiagonalMatrixSystem) -> Vector:
        # @todo #6:120min Implement Thomas Algorithm
        pass
