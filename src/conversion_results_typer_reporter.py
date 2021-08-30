from typing import Sequence

import typer
from pydantic.types import PositiveFloat

from conversion_results_reporter import ConversionResultsReporter
from conversion_spec import ConversionSpec


class ConversionResultsTyperReporter(ConversionResultsReporter):
    async def report(self, conversion_spec: ConversionSpec, results: Sequence[PositiveFloat]) -> None:
        # TODO: Is this the proper way to implement the async method such that it runs synchronously without "await"?
        # Asked in SO: https://stackoverflow.com/questions/68957729/python-implement-async-abstract-method-synchronously
        for source, dest in zip(conversion_spec.source_amounts, results):
            typer.echo(
                f"{source} {conversion_spec.source_currency} -> {dest} {conversion_spec.target_currency}"
            )
