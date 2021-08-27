from abc import ABC, abstractmethod

from pydantic.types import PositiveFloat

from conversion_spec import Coin


class ExchangeRateProvider(ABC):
    @abstractmethod
    async def provide(self, source_coin: Coin, target_coin: Coin) -> PositiveFloat:
        pass
