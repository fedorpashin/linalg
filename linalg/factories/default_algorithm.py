from linalg.systems.common.common_system import CommonSystem
from linalg.systems.common.common_system_algorithm import CommonSystemAlgorithm
from linalg.systems.common.default_common_system_algorithm import DefaultCommonSystemAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_algorithm import TridiagonalMatrixSystemAlgorithm
from linalg.systems.tridiagonal_matrix.default_tridiagonal_matrix_algorithm import DefaultTridiagonalMatrixSystemAlgorithm

from multimethod import multimeta
from final_class import final

__all__ = ['DefaultAlgorithm']


@final
class DefaultAlgorithm(metaclass=multimeta):
    def __new__(cls, system: CommonSystem) -> CommonSystemAlgorithm:
        return DefaultCommonSystemAlgorithm()

    def __new__(cls, system: TridiagonalMatrixSystem) -> TridiagonalMatrixSystemAlgorithm:  # type: ignore
        return DefaultTridiagonalMatrixSystemAlgorithm()
