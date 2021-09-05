from linalg.systems.common.common_system import CommonSystem
from linalg.matrices.common_square_matrix import CommonSquareMatrix
from linalg.vector import Vector

from typing import Final

import unittest


class TestAnySystem(unittest.TestCase):
    system: Final = CommonSystem(
        CommonSquareMatrix(
            [[1, 2],
             [3, 4]]
        ),
        Vector([1, 2])
    )

    def test_n(self):
        self.assertEqual(
            self.system.n,
            self.system.matrix.n
        )
