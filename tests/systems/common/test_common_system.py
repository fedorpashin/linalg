from linalg.systems.common.common_system import CommonSystem
from linalg.matrices.common_square import CommonSquareMatrix
from linalg.vector import Vector

from typing import Final

import unittest


class TestCommonSystem(unittest.TestCase):
    matrix: Final = CommonSquareMatrix(
        [[1, 2],
         [3, 4]]
    )
    vector: Final = Vector([5, 6])
    system: Final = CommonSystem(matrix, vector)

    def test_value(self):
        self.assertEqual(self.system.matrix, self.matrix)
        self.assertEqual(self.system.vector, self.vector)
