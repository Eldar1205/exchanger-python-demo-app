from abc import ABC, abstractmethod

from conversion_parameters import ConversionParameters
from conversion_spec import ConversionSpec


class ConversionSpecProvider(ABC):
    @abstractmethod
    async def provide_conversion_spec(self, conversion_parameters: ConversionParameters) -> ConversionSpec:
        pass
