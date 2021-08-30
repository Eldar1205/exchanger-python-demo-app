from abc import ABC, abstractmethod

from pydantic.types import PositiveFloat

from conversion_spec import Currency


class ExchangeRateProvider(ABC):
    @abstractmethod
    async def provide(self, source_currency: Currency, target_currency: Currency) -> PositiveFloat:
        pass
