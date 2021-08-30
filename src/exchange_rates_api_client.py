import aiohttp
import orjson
from pydantic.types import PositiveFloat

from conversion_spec import Currency
from exchange_rate_provider import ExchangeRateProvider


class ExchangeRatesApiClient(ExchangeRateProvider):
    async def provide(self, source_currency: Currency, target_currency: Currency) -> PositiveFloat:
        exchange_rate_api_url = self.__build_exchange_rate_api_url(source_currency, target_currency)

        async with aiohttp.ClientSession() as session:
            async with session.get(exchange_rate_api_url) as response:
                response.raise_for_status()
                json_body = await response.text()

                return orjson.loads(json_body)["result"]

    def __build_exchange_rate_api_url(self, source_currency: Currency, target_currency: Currency) -> str:
        return f"https://api.exchangerate.host/convert?from={source_currency}&to={target_currency}"
