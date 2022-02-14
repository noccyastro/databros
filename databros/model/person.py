from pydantic import Field, constr
from .base import BaseModel

__all__ = ("Person",)


class Person(BaseModel):
    display_name: str
    names: set[constr(to_lower=True)] = Field(default_factory=set)

    def __init__(self, **data):
        super().__init__(**data)
        self.names.add(self.display_name.lower())
