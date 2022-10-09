from datetime import datetime

import pytest

from onerecord.client import ONERecordClient
from onerecord.enums import LogisticsObjectType, NotificationEventType
from onerecord.exceptions import ONERecordClientException
from onerecord.models.api import Notification
from onerecord.models.cargo import Event, LogisticsObject, Piece


def test_initiate_client():
    with pytest.raises(ValueError):
        ONERecordClient()
    client = ONERecordClient(company_identifier="cgnbeerbrewery")
    assert client is not None


def test_client_create_logistics_object_piece():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )

    piece = Piece(
        **{
            "company_identifier": "cgnbeerbrewery",
            "goods_description": "six pack of Koelsch beer",
            "gross_weight": {"unit": "KGM", "value": 3.922},
        }
    )

    piece_response = client.create_logistics_object(logistics_object=piece)

    assert piece.id is not None
    assert piece_response is not None
    assert piece_response.id is not None
    assert piece == piece_response


def test_client_get_existing_logistics_object():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )

    piece = client.get_logistics_object_by_uri(
        uri="http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145"
    )

    assert piece is not None
    assert piece.id is not None
    assert type(piece) is Piece


def test_client_get_non_existing_logistics_object():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )

    with pytest.raises(ONERecordClientException):
        client.get_logistics_object_by_uri(
            uri="http://localhost:8080/companies/cgnbeerbrewery/los/piece-asd"
        )


def test_client_get_all_logistics_objects():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )

    logistics_objects: list[LogisticsObject] = client.get_logistics_objects()
    assert logistics_objects is not None
    assert len(logistics_objects) > 1


def test_client_get_all_pieces():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )

    logistics_objects: list[LogisticsObject] = client.get_logistics_objects(
        logistics_object_type=LogisticsObjectType.PIECE
    )
    assert logistics_objects is not None
    assert len(logistics_objects) > 1
    assert type(logistics_objects.pop()) is Piece


def test_client_create_event():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )
    logistics_object_uri: str = (
        "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145"
    )

    event: Event = Event(
        **{
            "event_type_indicator": "FSU",
            "event_code": "FOH",
            "event_name": "Freight on Hand",
            "linked_object": {
                "@type": [LogisticsObjectType.PIECE.value],
                "@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145",
                "company_identifier": "cgnbeerbrewery",
            },
            "date_time": datetime.utcnow(),
        }
    )
    assert (
        client.create_event(
            logistics_object_uri=logistics_object_uri, event=event
        )
        is True
    )


def test_client_get_events_by_logistics_objects_uri():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )
    logistics_object_uri: str = (
        "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145"
    )

    events: list[Event] = client.get_events_by_logistics_objects_uri(
        logistics_object_uri=logistics_object_uri
    )
    assert events is not None
    assert len(events) > 0
    assert type(events.pop()) is Event


def test_send_notification():
    client = ONERecordClient(
        host="localhost", port=8080, company_identifier="cgnbeerbrewery"
    )
    callback_url = "http://localhost:8080/companies/cgnbeerbrewery/callback"
    notification: Notification = Notification(
        **{
            "event_type": NotificationEventType.OBJECT_CREATED.value,
            "topic": LogisticsObjectType.PIECE.value,
            "logistics_object": {
                "@type": [LogisticsObjectType.PIECE.value],
                "@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1261620145",
                "company_identifier": "cgnbeerbrewery",
            },
        }
    )
    assert (
        client.send_notification(
            callback_url=callback_url, notification=notification
        )
        is True
    )
