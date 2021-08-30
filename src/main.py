import asyncio
import sys
from pathlib import Path

import typer
from lagom.container import Container
from lagom.definitions import Singleton

from conversion_flow_executer import ConversionFlowExecuter
from conversion_parameters import ConversionParameters
from conversion_results_reporter import ConversionResultsReporter
from conversion_results_typer_reporter import ConversionResultsTyperReporter
from conversion_spec_file_reader import ConversionSpecFileReader
from conversion_spec_provider import ConversionSpecProvider
from currency_converter import CurrencyConverter
from exchange_rate_provider import ExchangeRateProvider
from exchange_rates_api_client import ExchangeRatesApiClient


async def _main(conversion_spec_file_path: Path) -> None:
    # MyPy is instructed to ignore cases where abstract class is registered a concrete class because
    # it misclassifies the registered class for the DI container as needing to be a concrete class
    container = Container()
    container[ExchangeRateProvider] = Singleton(ExchangeRatesApiClient)  # type: ignore
    container[ConversionSpecProvider] = Singleton(ConversionSpecFileReader)  # type: ignore
    container[CurrencyConverter] = Singleton(CurrencyConverter)
    container[ConversionResultsReporter] = Singleton(ConversionResultsTyperReporter)  # type: ignore
    container[ConversionFlowExecuter] = Singleton(ConversionFlowExecuter)

    conversion_flow_executer = container[ConversionFlowExecuter]
    await conversion_flow_executer.execute(ConversionParameters(file_path=conversion_spec_file_path))


def main(
    conversion_spec_file_path: Path = typer.Argument(
        default=None,
        help="A path to the conversion spec file, can be absolute or relative to the working directory",
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
    )
) -> None:
    # Workaround to make asyncio work on Windows: https://github.com/encode/httpx/issues/914#issuecomment-622586610
    # Also mentioned at SO question: https://stackoverflow.com/questions/61543406/asyncio-run-runtimeerror-event-loop-is-closed
    if sys.platform.startswith("win") and sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(_main(conversion_spec_file_path))


if __name__ == "__main__":
    typer.run(main)
