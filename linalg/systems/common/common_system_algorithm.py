from linalg.base.any_algorithm import AnyAlgorithm
from linalg.systems.common.common_system import CommonSystem
from linalg.vector import Vector

from abc import abstractmethod

__all__ = ['CommonSystemAlgorithm']


class CommonSystemAlgorithm(AnyAlgorithm[CommonSystem]):
    @abstractmethod
    def solution(self, system: CommonSystem) -> Vector:
        pass
