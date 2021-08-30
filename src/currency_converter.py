from typing import Sequence

from pydantic.types import PositiveFloat

from conversion_spec import ConversionSpec
from exchange_rate_provider import ExchangeRateProvider


class CurrencyConverter:
    def __init__(self, exchange_rate_provider: ExchangeRateProvider) -> None:
        self.__exchangeRateProvider = exchange_rate_provider

    async def convert(self, spec: ConversionSpec) -> Sequence[PositiveFloat]:
        exchange_rate = await self.__exchangeRateProvider.provide(spec.source_currency, spec.target_currency)

        return tuple(map(lambda x: x * exchange_rate, spec.source_amounts))
