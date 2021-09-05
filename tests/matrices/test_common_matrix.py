from linalg.matrices.common import CommonMatrix

from typing import Final

import unittest


class TestCommonMatrix(unittest.TestCase):
    value: Final = (
         [[1, 2, 3],
          [4, 5, 6]]
    )

    def test_value(self):
        self.assertEqual(
            CommonMatrix(self.value).value,
            self.value
        )
