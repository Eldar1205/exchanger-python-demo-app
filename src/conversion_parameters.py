from pathlib import Path

from pydantic import BaseModel


class ConversionParameters(BaseModel):
    file_path: Path

    class Config:
        allow_mutation = False
