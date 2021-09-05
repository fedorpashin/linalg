from abc import ABC, abstractmethod

__all__ = ['AnyVector']


class AnyVector(ABC):
    @property
    @abstractmethod
    def value(self) -> list[float]:
        pass

    @property
    def n(self) -> int:
        return len(self.value)
