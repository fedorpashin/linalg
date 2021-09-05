from linalg.vector import Vector
from typing import Final

import unittest


class TestVector(unittest.TestCase):
    value: Final = [1, 2, 3]
    vector: Final = Vector(value)

    def test_vector(self):
        self.assertEqual(
            self.vector.value,
            self.value
        )
