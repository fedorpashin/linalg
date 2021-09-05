# linalg

[![build](https://github.com/fedorpashin/statistical-modeling/workflows/build/badge.svg)](https://github.com/fedorpashin/linalg/actions)
[![codecov](https://codecov.io/gh/fedorpashin/linalg/branch/master/graph/badge.svg?token=TFJEK2G1FB)](https://codecov.io/gh/fedorpashin/linalg)
[![Maintainability](https://api.codeclimate.com/v1/badges/9aba06e9b8fbb065a7e0/maintainability)](https://codeclimate.com/github/fedorpashin/linalg/maintainability)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Managed By Self XDSD](https://self-xdsd.com/b/mbself.svg)](https://self-xdsd.com/p/fedorpashin/linalg?provider=github)

## Usage

```python
import linalg as la

print(
    la.Solution(
        la.System(
            la.Matrix(
                [4, 9],
                [23, 5],
                [5, 16, 2]
            ),
            la.Vector(
                [5, 8, 1]
            )
        ),
        la.ThomasAlgorithm()  # optional
    )
)
```
