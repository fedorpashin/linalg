from linalg.base.any_system import AnySystem
from linalg.matrices.common_square_matrix import CommonSquareMatrix
from linalg.base.any_vector import AnyVector

from dataclasses import dataclass

__all__ = ['CommonSystem']


@dataclass(frozen=True)
class CommonSystem(AnySystem):
    matrix: CommonSquareMatrix
    vector: AnyVector
