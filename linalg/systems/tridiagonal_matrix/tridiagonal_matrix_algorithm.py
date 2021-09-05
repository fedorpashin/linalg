from linalg.base.any_algorithm import AnyAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.vector import Vector

from abc import abstractmethod

__all__ = ['TridiagonalMatrixSystemAlgorithm']


class TridiagonalMatrixSystemAlgorithm(AnyAlgorithm[TridiagonalMatrixSystem]):
    @abstractmethod
    def solution(self, system: TridiagonalMatrixSystem) -> Vector:
        pass
