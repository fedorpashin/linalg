from linalg.base.any_vector import AnyVector

from typing import Union
from dataclasses import dataclass
from final_class import final
from overrides import overrides

__all__ = ['Vector']


@final
@dataclass(frozen=True)
class Vector(AnyVector):
    __value: Union[list[float], list[int]]

    @property  # type: ignore
    @overrides
    def value(self):
        return self.__value
