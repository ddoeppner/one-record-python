import unittest
from datetime import datetime

import pytest
import requests_mock

from onerecord.client import ONERecordClient
from onerecord.enums import LogisticsObjectType, NotificationEventType
from onerecord.exceptions import ONERecordClientException
from onerecord.models.api import Notification
from onerecord.models.cargo import Event, LogisticsObject, Piece


def text_create_piece_callback(request, context):
    context.status_code = 201
    context.headers = {
        "Location": "http://localhost:8080/companies/test/los/piece-1260233867"
    }
    return '{"@id":"http://localhost:8080/companies/test/los/piece-1260233867","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/Piece#grossWeight":{"@id":"_:1794007512","@type":["https://onerecord.iata.org/Value"],"https://onerecord.iata.org/Value#value":3.922,"https://onerecord.iata.org/Value#unit":"KGM"},"https://onerecord.iata.org/LogisticsObject#revision":0,"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"http://localhost:8080/companies/test","https://onerecord.iata.org/Piece#goodsDescription":"six pack of Koelsch beer"}'


def text_get_piece_callback(request, context):
    context.status_code = 200
    return '{"@id":"http://localhost:8080/companies/test/los/piece-1260233867","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/Piece#grossWeight":{"@id":"_:1794007512","@type":["https://onerecord.iata.org/Value"],"https://onerecord.iata.org/Value#value":3.922,"https://onerecord.iata.org/Value#unit":"KGM"},"https://onerecord.iata.org/LogisticsObject#revision":0,"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"http://localhost:8080/companies/test","https://onerecord.iata.org/Piece#goodsDescription":"six pack of Koelsch beer"}'


def text_pieces_callback(request, context):
    context.status_code = 200
    return '[{"@id":"http://localhost:8080/companies/test/los/piece-1260233867","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/Piece#grossWeight":{"@id":"_:1794007512","@type":["https://onerecord.iata.org/Value"],"https://onerecord.iata.org/Value#value":3.922,"https://onerecord.iata.org/Value#unit":"KGM"},"https://onerecord.iata.org/LogisticsObject#revision":0,"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"http://localhost:8080/companies/test","https://onerecord.iata.org/Piece#goodsDescription":"six pack of Koelsch beer"}]'


def text_piece_events_callback(request, context):
    context.status_code = 200
    return '[{"@id":"http://localhost:8080/companies/test/los/piece-1260233867/event-1150940089","@type":["https://onerecord.iata.org/Event"],"https://onerecord.iata.org/Event#dateTime":"2022-10-10T19:49:10Z","https://onerecord.iata.org/Event#linkedObject":{"@id":"http://localhost:8080/companies/test/los/piece-1260233867","@type":["https://onerecord.iata.org/Piece","https://onerecord.iata.org/LogisticsObject"],"https://onerecord.iata.org/LogisticsObject#companyIdentifier":"test"},"https://onerecord.iata.org/Event#eventTypeIndicator":"FSU","https://onerecord.iata.org/Event#eventCode":"FOH","https://onerecord.iata.org/Event#eventName":"Freight on Hand"}]'


class TestONERecordClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ONERecordClient(company_identifier="test")
        super().setUp()

    def tearDown(self) -> None:
        self.client.close()

    @requests_mock.mock()
    def test_create_logistics_object(self, m):
        m.post(
            "http://localhost:8080/companies/test/los",
            text=text_create_piece_callback,
        )
        piece = Piece(
            **{
                "company_identifier": "cgnbeerbrewery",
                "goods_description": "six pack of Koelsch beer",
                "gross_weight": {"unit": "KGM", "value": 3.922},
            }
        )

        piece_response = self.client.create_logistics_object(logistics_object=piece)
        assert piece_response is not None
        assert piece_response.id is not None
        assert (
            piece_response.id
            == "http://localhost:8080/companies/test/los/piece-1260233867"
        )

    @requests_mock.mock()
    def test_create_invalid_logistics_object(self, m):
        m.post("http://localhost:8080/companies/test/los", status_code=500)
        with pytest.raises(ValueError):
            self.client.create_logistics_object(logistics_object=None)

    def test_initiate_client(self):
        with pytest.raises(ValueError):
            ONERecordClient()
        client = ONERecordClient(company_identifier="cgnbeerbrewery")
        assert client is not None

    @requests_mock.mock()
    def test_client_get_existing_logistics_object(self, m):
        m.get(
            "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1260233867",
            status_code=200,
            text=text_get_piece_callback,
        )
        piece = self.client.get_logistics_object_by_uri(
            uri="http://localhost:8080/companies/cgnbeerbrewery/los/piece-1260233867"
        )

        assert piece is not None
        assert piece.id is not None
        assert type(piece) is Piece

    @requests_mock.mock()
    def test_client_get_non_existing_logistics_object(self, m):
        m.get(
            "http://localhost:8080/companies/test/los/piece-asd",
            status_code=404,
        )
        with pytest.raises(ONERecordClientException):
            self.client.get_logistics_object_by_uri(
                uri="http://localhost:8080/companies/test/los/piece-asd"
            )

    @requests_mock.mock()
    def test_client_get_all_logistics_objects(self, m):
        m.get(
            "http://localhost:8080/companies/test/los",
            status_code=200,
            text=text_pieces_callback,
        )
        logistics_objects: list[LogisticsObject] = self.client.get_logistics_objects()
        assert logistics_objects is not None
        assert len(logistics_objects) > 0

    @requests_mock.mock()
    def test_client_get_all_pieces(self, m):
        m.get(
            "http://localhost:8080/companies/test/los?type=https://onerecord.iata.org/Piece",
            status_code=200,
            text=text_pieces_callback,
        )
        logistics_objects: list[LogisticsObject] = self.client.get_logistics_objects(
            logistics_object_type=LogisticsObjectType.PIECE
        )
        assert logistics_objects is not None
        assert len(logistics_objects) > 0
        assert type(logistics_objects.pop()) is Piece

    @requests_mock.mock()
    def test_client_create_event(self, m):
        m.post(
            "http://localhost:8080/companies/test/los/piece-1260233867/events",
            status_code=201,
        )
        logistics_object_uri: str = (
            "http://localhost:8080/companies/test/los/piece-1260233867"
        )

        event: Event = Event(
            **{
                "event_type_indicator": "FSU",
                "event_code": "FOH",
                "event_name": "Freight on Hand",
                "linked_object": {
                    "@type": [LogisticsObjectType.PIECE.value],
                    "@id": "http://localhost:8080/companies/test/los/piece-1260233867",
                    "company_identifier": "test",
                },
                "date_time": datetime.utcnow(),
            }
        )
        assert (
            self.client.create_event(
                logistics_object_uri=logistics_object_uri, event=event
            )
            is True
        )

    @requests_mock.mock()
    def test_client_get_events_by_logistics_objects_uri(self, m):
        m.get(
            "http://localhost:8080/companies/test/los/piece-1260233867/events",
            status_code=200,
            text=text_piece_events_callback,
        )
        logistics_object_uri: str = (
            "http://localhost:8080/companies/test/los/piece-1260233867"
        )

        events: list[Event] = self.client.get_events_by_logistics_objects_uri(
            logistics_object_uri=logistics_object_uri
        )
        assert events is not None
        assert len(events) > 0
        assert type(events.pop()) is Event

    @requests_mock.mock()
    def test_send_notification(self, m):
        m.post(
            "http://localhost:8080/companies/cgnbeerbrewery/callback",
            status_code=200,
        )

        callback_url = "http://localhost:8080/companies/cgnbeerbrewery/callback"
        notification: Notification = Notification(
            **{
                "event_type": NotificationEventType.OBJECT_CREATED.value,
                "topic": LogisticsObjectType.PIECE.value,
                "logistics_object": {
                    "@type": [LogisticsObjectType.PIECE.value],
                    "@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-1260233867",
                    "company_identifier": "cgnbeerbrewery",
                },
            }
        )
        assert (
            self.client.send_notification(
                callback_url=callback_url, notification=notification
            )
            is True
        )

    @requests_mock.mock()
    def test_update_logistics_object(self, m):
        m.patch(
            "http://localhost:8080/companies/test/los/piece-1260233867", status_code=204
        )
        m.get(
            "http://localhost:8080/companies/test/los/piece-1260233867",
            text=text_get_piece_callback,
            status_code=200,
        )
        updated_piece: Piece = Piece(
            **{
                "@id": "http://localhost:8080/companies/test/los/piece-1260233867",
                "https://onerecord.iata.org/Piece#grossWeight": {
                    "https://onerecord.iata.org/Value#value": 4.922,
                    "https://onerecord.iata.org/Value#unit": "KGM",
                },
                "https://onerecord.iata.org/LogisticsObject#companyIdentifier": "http://localhost:8080/companies/test",
                "https://onerecord.iata.org/Piece#goodsDescription": "six pack of Koelsch beer",
            }
        )
        assert (
            self.client.update_logistics_object(updated_logistics_object=updated_piece)
            is True
        )
