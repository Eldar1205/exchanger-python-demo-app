import aiofiles
import asyncstdlib
from pydantic.types import PositiveFloat

from conversion_parameters import ConversionParameters
from conversion_spec import Coin, ConversionSpec
from conversion_spec_provider import ConversionSpecProvider


class ConversionSpecFileReader(ConversionSpecProvider):
    async def provide_conversion_spec(self, conversion_parameters: ConversionParameters) -> ConversionSpec:
        source_coin: Coin
        target_coin: Coin
        source_amounts: tuple[PositiveFloat]

        async with aiofiles.open(conversion_parameters.file_path) as conversion_spec_file:
            source_coin, target_coin, *source_amounts = await asyncstdlib.tuple(conversion_spec_file)

        return ConversionSpec(
            source_coin=source_coin,
            target_coin=target_coin,
            source_amounts=source_amounts,
        )
