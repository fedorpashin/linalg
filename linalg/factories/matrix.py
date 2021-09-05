from linalg.matrices.common_square_matrix import CommonSquareMatrix
from linalg.matrices.common_matrix import CommonMatrix
from linalg.matrices.tridiagonal_matrix import TridiagonalMatrix

from typing import Union
from multimethod import multimeta


class Matrix(metaclass=multimeta):
    def __new__(cls, value: list[list[Union[float, int]]]):
        if len(value[0]) == len(value):
            return CommonSquareMatrix(value)
        else:
            return CommonMatrix(value)

    def __new__(  # type: ignore
            cls,
            a: list[Union[float, int]],
            b: list[Union[float, int]],
            c: list[Union[float, int]],
    ):
        return TridiagonalMatrix(a, b, c)
