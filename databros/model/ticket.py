from pydantic import Field, ValidationError, validator
from typing import Optional
from enum import Enum
from . import Person, BaseModel

__all__ = ("TicketType", "TicketStatus", "Ticket")


class TicketType(str, Enum):
    Platinum = "platinum"
    Gold = "gold"
    Silver = "silver"
    Bronze = "bronze"


class TicketStatus(str, Enum):
    Pending = "pending"
    Redeemed = "redeemed"
    Unknown = "unknown"


class Ticket(BaseModel):
    owner: Person
    type: TicketType
    status: TicketStatus = Field(default=TicketStatus.Pending)
    redeemed_for: Optional[str] = None
    note: Optional[str] = None

    @validator("redeemed_for")
    def validate_redeemed_for(cls, redeemed_for, values, **kwargs):
        if values["status"] != TicketStatus.Redeemed and redeemed_for is not None:
            raise ValidationError(
                'if status is not "Reedmed" then "redeemed_for" must not be set'
            )
        elif values["status"] == TicketStatus.Redeemed and redeemed_for is None:
            raise ValidationError(
                'if status is "Reedmed" then "redeemed_for" must be set'
            )
        return redeemed_for
