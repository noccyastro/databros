from textwrap import indent
from databros.model.person import Person
from databros.model.ticket import Ticket, TicketStatus, TicketType
from .. import model
from . import people

tickets = [
    Ticket(
        owner=people.crooked,
        status=TicketStatus.Pending,
        type=TicketType.Gold,
    ),
    Ticket(
        owner=people.scarling,
        status=TicketStatus.Pending,
        type=TicketType.Gold,
    ),
    Ticket(
        owner=people.huse,
        status=TicketStatus.Pending,
        type=TicketType.Gold,
    ),
    Ticket(
        owner=people.haruka,
        status=TicketStatus.Pending,
        type=TicketType.Silver,
    ),
    Ticket(
        owner=people.haughtwheels,
        status=TicketStatus.Redeemed,
        type=TicketType.Gold,
        redeemed_for="VIP",
    ),
    Ticket(
        owner=people.bluethegauntlet,
        status=TicketStatus.Pending,
        type=TicketType.Platinum,
    ),
    Ticket(
        owner=people.mroutsideworld,
        status=TicketStatus.Pending,
        type=TicketType.Gold,
    ),
    Ticket(
        owner=people.adarkthunder,
        status=TicketStatus.Redeemed,
        type=TicketType.Gold,
        redeemed_for="financial stream",
        note="was not fufilled prior to the change in redeems",
    ),
    Ticket(
        owner=people.dondaler,
        status=TicketStatus.Unknown,
        type=TicketType.Bronze,
    ),
    Ticket(
        owner=people.deathmaster2192,
        status=TicketStatus.Unknown,
        type=TicketType.Bronze,
    ),
]


def _print():
    import json

    print(json.dumps([json.loads(t.json()) for t in tickets], indent=2))
