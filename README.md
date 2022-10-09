# ONE Record with Python
![Made with love for Digital Cargo](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%20for-Digital%20Cargo-informational)
[![GitHub](https://img.shields.io/github/license/leoll2/copyright_notice_precommit)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
> **Note:** This library is based on the latest IATA ONE Record ontology (working draft)

---
## What is ONE Record?
> ONE Record is a standard for data sharing and creates a single record view of the shipment.
> This standard defines a common data model for the data that is shared via standardized and secured web API.
> (Source: [IATA - ONE Record](https://www.iata.org/one-record/))

---

## Requirements
- Python version 3.9+

---

## Installation

Install, upgrade and uninstall **ONE Record with Python** with these commands::

    $ pip install onerecord
    $ pip install --upgrade onerecord
    $ pip uninstall onerecord

## A Simple Example

```py
from onerecord.models.cargo import Piece
from onerecord.client import ONERecordClient

piece = Piece(**{'company_identifier': 'cgnbeerbrewery',
                         'goods_description': 'six pack of Koelsch beer',
                         'gross_weight': {'unit': 'KGM', 'value': 3.922}})

piece.goods_description
#> 'six pack of Koelsch beer'
print(piece.json(exclude_none=True, by_alias=True))
#> {"@type": "https://onerecord.iata.org/Piece", "https://onerecord.iata.org/LogisticsObject#companyIdentifier": "cgnbeerbrewery", "https://onerecord.iata.org/Piece#goodsDescription": "six pack of Koelsch beer", "https://onerecord.iata.org/Piece#grossWeight": {"@type": "https://onerecord.iata.org/Value", "https://onerecord.iata.org/Value#unit": "KGM", "https://onerecord.iata.org/Value#value": 3.922}}
print(type(piece))
#> <class 'onerecord.models.cargo.Piece'>
print(type(piece.gross_weight))
#> <class 'onerecord.models.cargo.Value'>

client = ONERecordClient(host="localhost", port=8080, company_identifier="cgnbeerbrewery")
piece = client.create_logistics_object(piece)
print(piece.id)
#> http://localhost:8080/companies/cgnbeerbrewery/los/piece-1067358949
```

---

## ONE Record Version Support

| ONE Record with Python | IATA Data Model Ontology                                                                                                                                  | IATA API Ontology                                                                                                                                        | IATA API Spec                                                                                                    |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| v0.1.0               | [v2.0.0](https://raw.githubusercontent.com/IATA-Cargo/ONE-Record/eb404f134c18f8aac0bfe51666c081ba971f3c4d/working_draft/ontology/IATA-1R-DM-Ontology.ttl) | [v1.1](https://raw.githubusercontent.com/IATA-Cargo/ONE-Record/eb404f134c18f8aac0bfe51666c081ba971f3c4d/working_draft/ontology/IATA-1R-API-Ontology.ttl) | [v1.1](https://github.com/IATA-Cargo/ONE-Record/tree/706b01f81e7b4618b6ec84fdb38bfd2ff6a1e3e8/working_draft/API) |
| ...                   | ...                                                                                                                                                       | ...                                                                                                                                                      | ...                                                                                                              |
| ...                   | ...                                                                                                                                                       | ...                                                                                                                                                      | ...                                                                                                              |

---

## Dependencies

This **ONE Record with Python** distribution is tested on Python 3.9 and 3.10.

The dependencies are:

- pydantic: Data validation using Python type hints (https://pydantic-docs.helpmanual.io)
- requests: HTTP for Humans (https://requests.readthedocs.io)
