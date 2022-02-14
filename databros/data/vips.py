from datetime import datetime
from . import people
from ..model import VIP


vips = [
    VIP(
        person=people.bao,
        reason="Good Friends",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.beautifulorigin,
        reason="Word of the day",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.chibi,
        reason="Good Friends",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.codemiko,
        reason="Good Friends",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.haruka,
        reason="Good Friends",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.haughtwheels,
        reason="Golden Ticket Redeem",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.kode,
        reason="Channel Points",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.lord_df_01,
        reason="Offline bet keeper and announcer",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.suitwo,
        reason="Slam stat keeper",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.oczu_,
        reason="Gamble bet tracker",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.reldeth,
        reason="Mini discovers data keeper",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.slyicet,
        reason="Channel Points (first)",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
    VIP(
        person=people.tranguul,
        reason="PR person of Nagzz",
        date=datetime.strptime("01/01/21", "%d/%m/%y"),
    ),
]


def _print():
    import json

    print(json.dumps([json.loads(v.json()) for v in vips], indent=2))
