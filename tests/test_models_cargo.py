import pytest
from pydantic import ValidationError

from onerecord.enums import LogisticsObjectType, NotificationEventType
from onerecord.models.api import Notification, Subscription


def test_create_piece():
    with pytest.raises(ValidationError):
        Notification(**{"event_type": "something"})
    notification = Notification(
        **{
            "event_type": "OBJECT_CREATED",
            "topic": LogisticsObjectType.PIECE.value,
            "logistics_object": {
                "@id": "http://localhost:8080/companies/cgnbeerbrewery/los/piece-4711-1337-1",
                "company_identifier": "cgnbeerbrewery",
            },
        }
    )
    assert notification is not None
    assert notification.event_type == NotificationEventType.OBJECT_CREATED
    assert notification.id is None


def test_create_shipment():
    with pytest.raises(ValidationError):
        Subscription()
    subscription = Subscription(
        **{
            "callback_url": "http://localhost:8080/companies/cgnbeerbrewery/callback",
            "my_company_identifier": "cgnbeerbrewery",
            "subscribed_to": "cgnbeerbrewery",
            "topic": LogisticsObjectType.PIECE.value,
        }
    )
    assert subscription is not None
    assert subscription.topic == LogisticsObjectType.PIECE.value
    assert subscription.id is None
