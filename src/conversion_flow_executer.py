from conversion_parameters import ConversionParameters
from conversion_results_reporter import ConversionResultsReporter
from conversion_spec_provider import ConversionSpecProvider
from money_converter import MoneyConverter


class ConversionFlowExecuter:
    def __init__(
        self,
        conversion_spec_provider: ConversionSpecProvider,
        money_converter: MoneyConverter,
        conversion_results_reporter: ConversionResultsReporter,
    ) -> None:
        self.__conversion_spec_provider = conversion_spec_provider
        self.__money_converter = money_converter
        self.__conversion_results_reporter = conversion_results_reporter

    async def execute(self, conversion_parameters: ConversionParameters) -> None:
        conversion_spec = await self.__conversion_spec_provider.provide_conversion_spec(conversion_parameters)
        conversion_results = await self.__money_converter.convert(conversion_spec)
        await self.__conversion_results_reporter.report(conversion_spec, conversion_results)
