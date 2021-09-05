from linalg.matrices.square import SquareMatrix
from linalg.base.any_vector import AnyVector

from abc import ABC
from dataclasses import dataclass

__all__ = ['AnySystem']


@dataclass(frozen=True)
class AnySystem(ABC):
    matrix: SquareMatrix
    vector: AnyVector
