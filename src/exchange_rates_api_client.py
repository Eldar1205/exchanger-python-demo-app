import aiohttp
import orjson
from pydantic.types import PositiveFloat

from conversion_spec import Coin
from exchange_rate_provider import ExchangeRateProvider


class ExchangeRatesApiClient(ExchangeRateProvider):
    async def provide(self, source_coin: Coin, target_coin: Coin) -> PositiveFloat:
        exchange_rate_api_url = self.__build_exchange_rate_api_url(
            source_coin, target_coin
        )

        async with aiohttp.ClientSession() as session:
            async with session.get(exchange_rate_api_url) as response:
                response.raise_for_status()
                jsonBody = await response.text()

                return orjson.loads(jsonBody)["result"]

    def __build_exchange_rate_api_url(
        self, source_coin: Coin, target_coin: Coin
    ) -> str:
        return (
            f"https://api.exchangerate.host/convert?from={source_coin}&to={target_coin}"
        )
