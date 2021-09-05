from linalg.matrices.square import SquareMatrix

from typing import Union
from dataclasses import dataclass
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['CommonSquareMatrix']


@final
@dataclass(frozen=True)
class CommonSquareMatrix(SquareMatrix):
    value: list[list[Union[float, int]]]

    def __post_init__(self):
        size = len(self.value)
        for row in self.value[1:]:
            assert len(row) == size

    @cached_property  # type: ignore
    @overrides
    def n(self):
        return len(self.value)
