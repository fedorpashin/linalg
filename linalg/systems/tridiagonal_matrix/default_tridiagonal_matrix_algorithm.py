from linalg.systems.tridiagonal_matrix.thomas_algorithm import ThomasAlgorithm

__all__ = ['DefaultTridiagonalMatrixSystemAlgorithm']


class DefaultTridiagonalMatrixSystemAlgorithm:
    def __new__(cls):
        return ThomasAlgorithm()
