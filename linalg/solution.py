from linalg.base.any_vector import AnyVector
from linalg.base.any_system import AnySystem
from linalg.base.any_algorithm import AnyAlgorithm
from linalg.factories.default_algorithm import DefaultAlgorithm

from dataclasses import dataclass
from typing import TypeVar
from final_class import final
from overrides import overrides

from functools import cached_property

__all__ = ['Solution']

T = TypeVar('T', bound=AnySystem)


@final
@dataclass
class Solution(AnyVector):
    __system: T  # type: ignore
    __algorithm: AnyAlgorithm[T]

    def __init__(self, system: T, algorithm: AnyAlgorithm[T] = None):
        self.__system = system
        self.__algorithm = DefaultAlgorithm(self.system) if algorithm is None else algorithm

    @cached_property  # type: ignore
    @overrides
    def value(self) -> list[float]:
        return self.algorithm.solution(self.system).value

    @property
    def system(self):
        return self.__system

    @property
    def algorithm(self):
        return self.__algorithm
