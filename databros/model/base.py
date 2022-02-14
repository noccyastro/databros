from pydantic import BaseModel as PydanticBaseModel, Field, Extra
from uuid import UUID, uuid4
from typing import Union

__all__ = ("BaseModel",)


class BaseModel(PydanticBaseModel):
    class Config:
        extra = Extra.forbid

    id: Union[str, UUID] = Field(default_factory=uuid4)
