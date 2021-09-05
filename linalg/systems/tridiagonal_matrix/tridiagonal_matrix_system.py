from linalg.base.any_system import AnySystem
from linalg.matrices.tridiagonal import TridiagonalMatrix
from linalg.base.any_vector import AnyVector

from dataclasses import dataclass

__all__ = ['TridiagonalMatrixSystem']


@dataclass(frozen=True)
class TridiagonalMatrixSystem(AnySystem):
    matrix: TridiagonalMatrix
    vector: AnyVector
