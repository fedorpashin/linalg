from linalg.base.any_system import AnySystem
from linalg.vector import Vector

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T', bound=AnySystem)

__all__ = ['AnyAlgorithm']


class AnyAlgorithm(ABC, Generic[T]):
    @abstractmethod
    def solution(self, system: T) -> Vector:
        pass
