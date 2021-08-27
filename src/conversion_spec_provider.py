from abc import ABC, abstractmethod

from conversion_parameters import ConversionParameters
from conversion_spec import ConversionSpec


class ConversionSpecProvider(ABC):
    @abstractmethod
    async def provideConversionSpec(
        self, conversion_parameters: ConversionParameters
    ) -> ConversionSpec:
        pass
