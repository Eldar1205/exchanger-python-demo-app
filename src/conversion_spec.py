from typing import NewType, Sequence

from pydantic import BaseModel
from pydantic.types import PositiveFloat

Currency = NewType("Currency", str)


class ConversionSpec(BaseModel):
    source_currency: Currency
    target_currency: Currency
    source_amounts: Sequence[PositiveFloat]

    class Config:
        allow_mutation = False
