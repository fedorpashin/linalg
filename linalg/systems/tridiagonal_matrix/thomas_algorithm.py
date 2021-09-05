from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_algorithm import TridiagonalMatrixSystemAlgorithm
from linalg.systems.tridiagonal_matrix.tridiagonal_matrix_system import TridiagonalMatrixSystem
from linalg.vector import Vector

from dataclasses import dataclass

__all__ = ['ThomasAlgorithm']


@dataclass(frozen=True)
class ThomasAlgorithm(TridiagonalMatrixSystemAlgorithm):
    # flake8: noqa: E226
    def solution(self, system: TridiagonalMatrixSystem) -> Vector:
        a = system.matrix.a
        b = system.matrix.b
        c = system.matrix.c
        g = system.vector.value
        n = system.n

        α = [0. for _ in range(n - 1)]
        β = [0. for _ in range(n - 1)]
        x = [0. for _ in range(n)]

        α[0] = -b[0] / c[0]
        β[0] = g[0] / c[0]
        for i in range(1, n - 1):
            α[i] = -b[i] / (a[i-1] * α[i-1] + c[i])
            β[i] = (g[i] - a[i-1] * β[i-1]) / (a[i-1] * α[i-1] + c[i])

        x[n-1] = (g[n-1] - a[n-2] * β[n-2]) / (a[n-2] * α[n-2] + c[n-1])

        for i in range(n - 2, -1, -1):
            x[i] = α[i] * x[i+1] + β[i]

        return Vector(x)
