from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.utils import to_camel


class Thing(BaseModel):
    id: str = Field(default=None, alias="@id")

    class Config:
        allow_population_by_field_name = True
        alias_generator = to_camel
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%SZ")}
