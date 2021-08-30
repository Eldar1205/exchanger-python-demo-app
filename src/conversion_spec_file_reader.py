import aiofiles
import asyncstdlib
from pydantic.types import PositiveFloat

from conversion_parameters import ConversionParameters
from conversion_spec import ConversionSpec, Currency
from conversion_spec_provider import ConversionSpecProvider


class ConversionSpecFileReader(ConversionSpecProvider):
    async def provide_conversion_spec(self, conversion_parameters: ConversionParameters) -> ConversionSpec:
        source_currency: Currency
        target_currency: Currency
        source_amounts: tuple[PositiveFloat]

        async with aiofiles.open(conversion_parameters.file_path) as conversion_spec_file:
            source_currency, target_currency, *source_amounts = await asyncstdlib.tuple(conversion_spec_file)

        return ConversionSpec(
            source_currency=source_currency,
            target_currency=target_currency,
            source_amounts=source_amounts,
        )
