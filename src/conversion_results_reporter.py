from abc import ABC, abstractmethod
from typing import Sequence

from pydantic.types import PositiveFloat

from conversion_spec import ConversionSpec


class ConversionResultsReporter(ABC):
    @abstractmethod
    async def report(self, conversion_spec: ConversionSpec, results: Sequence[PositiveFloat]) -> None:
        pass
