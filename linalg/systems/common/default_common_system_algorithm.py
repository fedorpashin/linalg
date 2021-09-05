from linalg.systems.common.common_system_algorithm import CommonSystemAlgorithm
from linalg.systems.common.gaussian_elimination import GaussianElimination

__all__ = ['DefaultCommonSystemAlgorithm']


class DefaultCommonSystemAlgorithm:
    def __new__(cls) -> CommonSystemAlgorithm:
        return GaussianElimination()
