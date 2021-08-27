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
        self.__conversionSpecProvider = conversion_spec_provider
        self.__moneyConverter = money_converter
        self.__conversionResultsReporter = conversion_results_reporter

    async def execute(self, conversion_parameters: ConversionParameters) -> None:
        conversion_spec = await self.__conversionSpecProvider.provideConversionSpec(conversion_parameters)
        conversion_results = await self.__moneyConverter.convert(conversion_spec)
        await self.__conversionResultsReporter.report(conversion_spec, conversion_results)
