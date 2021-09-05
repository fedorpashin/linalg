from linalg.systems.common.common_system_algorithm import CommonSystemAlgorithm
from linalg.systems.common.common_system import CommonSystem
from linalg.vector import Vector

from dataclasses import dataclass

__all__ = ['GaussianElimination']


@dataclass(frozen=True)
class GaussianElimination(CommonSystemAlgorithm):
    def solution(self, system: CommonSystem) -> Vector:
        # @todo #6:120min Implement Gaussian Elimination
        pass
