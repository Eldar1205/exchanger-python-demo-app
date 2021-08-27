import aiofiles
import asyncstdlib
from pydantic.types import PositiveFloat

from conversion_parameters import ConversionParameters
from conversion_spec import Coin, ConversionSpec
from conversion_spec_provider import ConversionSpecProvider


class ConversionSpecFileReader(ConversionSpecProvider):
    async def provideConversionSpec(self, conversion_parameters: ConversionParameters) -> ConversionSpec:
        source_amounts = list[PositiveFloat]()
        async with aiofiles.open(conversion_parameters.file_path) as conversion_spec_file:
            async for index, line in asyncstdlib.enumerate(conversion_spec_file):
                if index == 0:
                    source_coin = Coin(line)
                elif index == 1:
                    target_coin = Coin(line)
                else:
                    source_amounts.append(PositiveFloat(line))

        return ConversionSpec(
            source_coin=source_coin,
            target_coin=target_coin,
            source_amounts=source_amounts,
        )
