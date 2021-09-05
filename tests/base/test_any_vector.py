from linalg.vector import Vector

from typing import Final

import unittest


class TestAnyVector(unittest.TestCase):
    vector: Final = Vector([1, 2, 3])

    def test_n(self):
        self.assertEqual(self.vector.n, 3)
