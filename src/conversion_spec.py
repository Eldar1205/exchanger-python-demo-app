from typing import NewType, Sequence

from pydantic import BaseModel
from pydantic.types import PositiveFloat

Coin = NewType("Coin", str)


class ConversionSpec(BaseModel):
    source_coin: Coin
    target_coin: Coin
    source_amounts: Sequence[PositiveFloat]

    class Config:
        allow_mutation = False
