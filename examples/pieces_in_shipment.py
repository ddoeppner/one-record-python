from onerecord.models.cargo import Piece, Shipment, Location, Event
from datetime import datetime

"""
Freight on Hand Shipment with Pieces

Description:
Create a shipment with pieces and add FOH event to pieces and shipments
"""

COMPANY_IDENTIFIER: str = "cgnbeerbrewery"

pieces: list[Piece] = []

# Pieces
for i in range(0, 10):
    pieces.append(
        Piece(
            **{
                "upid": f"4711-1337-{i + 1}",
                "company_identifier": COMPANY_IDENTIFIER,
                "goods_description": "six pack of Koelsch beer",
                "gross_weight": {"unit": "KGM", "value": 3.922},
            }
        )
    )
print(f"Created {len(pieces)} pieces")

# Shipment
# Remark: Total Gross Weight includes extra packing material of 1.5 kg
shipment: Shipment = Shipment(
    **{
        "company_identifier": COMPANY_IDENTIFIER,
        "contained_pieces": pieces,
        "total_gross_weight": {
            "unit": "KGM",
            "value": sum(piece.gross_weight.value for piece in pieces) + 1.5,
        },
        "volumetric_weight": [
            {
                "unit": "KGM",
                "value": sum(piece.gross_weight.value for piece in pieces),
            }
        ],
    }
)
print(f"Created Shipment with the {len(shipment.contained_pieces)} pieces")

# Freight on Hand Event
location_cgn_airport: Location = Location(
    **{
        "location_type": "AIRPORT",
        "code": "CGN",
        "location_name": "Cologne Bonn Airport",
    }
)

event: Event = Event(
    **{
        "event_type_indicator": "FSU",
        "event_code": "FOH",
        "event_name": "Freight on Hand",
        "location": location_cgn_airport,
        "date_time": datetime.utcnow(),
    }
)

for piece in pieces:
    if type(piece.events) is not list:
        piece.events = []
    piece.events.append(event)

shipment.events = [event]

for piece in pieces:
    print(f"Piece {piece.upid} has {len(shipment.events)} Event(s)")

print(f"Shipment has {len(shipment.events)} Event(s)")
