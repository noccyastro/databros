from datetime import datetime
from . import Person, BaseModel

__all__ = ("POBoxItem",)


class POBoxItem(BaseModel):
    sender: Person
    description: str
    date: datetime
