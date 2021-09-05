from linalg.base.any_matrix import AnyMatrix

from dataclasses import dataclass
from final_class import final

__all__ = ['CommonMatrix']


@final
@dataclass(frozen=True)
class CommonMatrix(AnyMatrix):
    value: list[list[float]]

    def __post_init__(self):
        size = len(self.value[0])
        for row in self.value[1:]:
            assert len(row) == size
