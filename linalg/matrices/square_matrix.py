from linalg.base.any_matrix import AnyMatrix

from abc import abstractmethod

__all__ = ['SquareMatrix']


class SquareMatrix(AnyMatrix):
    @abstractmethod
    def n(self):
        pass
