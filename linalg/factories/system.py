from linalg.base.any_vector import AnyVector
from linalg.matrices.common_square_matrix import CommonSquareMatrix
from linalg.systems.common.common_system import CommonSystem
from linalg.matrices.tridiagonal_matrix import TridiagonalMatrix
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem

from multimethod import multimeta


class System(metaclass=multimeta):
    def __new__(cls, matrix: CommonSquareMatrix, vector: AnyVector):
        return CommonSystem(matrix, vector)

    def __new__(cls, matrix: TridiagonalMatrix, vector: AnyVector):  # type: ignore
        return TridiagonalMatrixSystem(matrix, vector)
