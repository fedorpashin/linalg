from linalg.matrices.square import SquareMatrix

from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['TridiagonalMatrix']


@final
@dataclass(frozen=True)
class TridiagonalMatrix(SquareMatrix):
    a: list[float]
    b: list[float]
    c: list[float]

    @cached_property  # type: ignore
    @overrides
    def n(self):
        return len(self.c)
