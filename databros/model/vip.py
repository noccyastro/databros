from datetime import datetime
from . import Person, BaseModel

__all__ = ("VIP",)


class VIP(BaseModel):
    person: Person
    reason: str
    date: datetime
