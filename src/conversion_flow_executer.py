from conversion_parameters import ConversionParameters
from conversion_results_reporter import ConversionResultsReporter
from conversion_spec_provider import ConversionSpecProvider
from currency_converter import CurrencyConverter


class ConversionFlowExecuter:
    def __init__(
        self,
        conversion_spec_provider: ConversionSpecProvider,
        currency_converter: CurrencyConverter,
        conversion_results_reporter: ConversionResultsReporter,
    ) -> None:
        self.__conversion_spec_provider = conversion_spec_provider
        self.__currency_converter = currency_converter
        self.__conversion_results_reporter = conversion_results_reporter

    async def execute(self, conversion_parameters: ConversionParameters) -> None:
        conversion_spec = await self.__conversion_spec_provider.provide_conversion_spec(conversion_parameters)
        conversion_results = await self.__currency_converter.convert(conversion_spec)
        await self.__conversion_results_reporter.report(conversion_spec, conversion_results)
