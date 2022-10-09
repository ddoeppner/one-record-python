from onerecord.models.cargo import Piece

"""
Simple Piece

Description:
Create a single piece and print out some characteristics and
the JSON encoded Piece.
"""
piece = Piece(
    **{
        "company_identifier": "cgnbeerbrewery",
        "goods_description": "six pack of Koelsch beer",
        "gross_weight": {"unit": "KGM", "value": 3.922},
    }
)

print(piece.goods_description)

print(piece.json(exclude_none=True, by_alias=True))

print(type(piece))

print(type(piece.gross_weight))
