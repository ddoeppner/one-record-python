from json import JSONDecodeError

import pytest

from onerecord.models.cargo import LogisticsObject, Piece
from onerecord.utils import json_to_logistics_object, json_to_logistics_objects


def test_json_to_logistics_object():
    logistics_object_json: str = '{"@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145", "@type": ["https://onerecord.iata.org/Piece", "https://onerecord.iata.org/LogisticsObject"], "https://onerecord.iata.org/Piece#grossWeight": {"@id": "_:1957521880", "@type": [ "https://onerecord.iata.org/Value"], "https://onerecord.iata.org/Value#value": 3.922, "https://onerecord.iata.org/Value#unit": "KGM"}, "https://onerecord.iata.org/LogisticsObject#revision": 0, "https://onerecord.iata.org/LogisticsObject#companyIdentifier": "http://localhost:8080/companies/cgnbeerbrewery", "https://onerecord.iata.org/Piece#goodsDescription": "six pack of Koelsch beer"}'
    logistics_object: LogisticsObject = json_to_logistics_object(
        logistics_object_json=logistics_object_json
    )
    assert logistics_object is not None
    assert type(logistics_object) is Piece


def test_json_to_logistics_object_invalid():
    with pytest.raises(JSONDecodeError):
        invalid_logistics_object_json: str = '{ype": ["https://onerecord.iata.org/Piece", "https://onerecord.iata.org/LogisticsObject"], "https://onerecord.iata.org/Piece#grossWeight": {"@id": "_:1957521880", "@type": [ "https://onerecord.iata.org/Value"], "https://onerecord.iata.org/Value#value": 3.922, "https://onerecord.iata.org/Value#unit": "KGM"}, "https://onerecord.iata.org/LogisticsObject#revision": 0, "https://onerecord.iata.org/LogisticsObject#companyIdentifier": "http://localhost:8080/companies/cgnbeerbrewery", "https://onerecord.iata.org/Piece#goodsDescription": "six pack of Koelsch beer"}'
        json_to_logistics_object(
            logistics_object_json=invalid_logistics_object_json
        )

    unknown_logistics_object_json: str = '{"@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145", "@type": ["https://onerecord.iata.org/Beer", "https://onerecord.iata.org/LogisticsObject"], "https://onerecord.iata.org/Piece#grossWeight": {"@id": "_:1957521880", "@type": [ "https://onerecord.iata.org/Value"], "https://onerecord.iata.org/Value#value": 3.922, "https://onerecord.iata.org/Value#unit": "KGM"}, "https://onerecord.iata.org/LogisticsObject#revision": 0, "https://onerecord.iata.org/LogisticsObject#companyIdentifier": "http://localhost:8080/companies/cgnbeerbrewery", "https://onerecord.iata.org/Piece#goodsDescription": "six pack of Koelsch beer"}'
    unknown_logistics_objects: LogisticsObject = json_to_logistics_object(
        logistics_object_json=unknown_logistics_object_json
    )

    assert unknown_logistics_objects is None


def test_json_to_logistics_objects():
    logistics_objects_json: str = '[{"@id":"http://localhost:8080/companies/cgnbeerbrewery/piece-1153586115","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/Piece#grossWeight":{"@id":"_:1683317490","@type":["https://onerecord.iata.org/Value"],"https://onerecord.iata.org/Value#value":3.922,"https://onerecord.iata.org/Value#unit":"KGM"},"https://onerecord.iata.org/LogisticsObject#revision":0,"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"http://localhost:8080/companies/cgnbeerbrewery","https://onerecord.iata.org/Piece#goodsDescription":"six pack of Koelsch beer"},{"@id":"http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/Piece#grossWeight":{"@id":"_:1957521880","@type":["https://onerecord.iata.org/Value"],"https://onerecord.iata.org/Value#value":3.922,"https://onerecord.iata.org/Value#unit":"KGM"},"https://onerecord.iata.org/LogisticsObject#revision":0,"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"http://localhost:8080/companies/cgnbeerbrewery","https://onerecord.iata.org/Piece#goodsDescription":"six pack of Koelsch beer"}]'
    logistics_objects: list[LogisticsObject] = json_to_logistics_objects(
        logistics_objects_json=logistics_objects_json
    )
    assert logistics_objects is not None
    assert len(logistics_objects) == 2
