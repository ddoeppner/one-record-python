import importlib
import json
from typing import Optional

from onerecord.models.cargo import Event, LogisticsObject

type_class_mapping: dict = {
    "https://onerecord.iata.org/Booking": "Booking",
    "https://onerecord.iata.org/BookingOption": "BookingOption",
    "https://onerecord.iata.org/BookingOptionRequest": "BookingOptionRequest",
    "https://onerecord.iata.org/BookingTimes": "BookingTimes",
    "https://onerecord.iata.org/CO2CalcMethod": "CO2CalcMethod",
    "https://onerecord.iata.org/CO2Emissions": "CO2Emissions",
    "https://onerecord.iata.org/CarrierProduct": "CarrierProduct",
    "https://onerecord.iata.org/Characteristics": "Characteristics",
    "https://onerecord.iata.org/CustomsInfo": "CustomsInfo",
    "https://onerecord.iata.org/DgDeclaration": "DgDeclaration",
    "https://onerecord.iata.org/DgProductRadioactive": "DgProductRadioactive",
    "https://onerecord.iata.org/DgRadioactiveIsotope": "DgRadioactiveIsotope",
    "https://onerecord.iata.org/EpermitConsignment": "EpermitConsignment",
    "https://onerecord.iata.org/EpermitSignature": "EpermitSignature",
    "https://onerecord.iata.org/Insurance": "Insurance",
    "https://onerecord.iata.org/IotDevice": "IotDevice",
    "https://onerecord.iata.org/ItemDg": "ItemDg",
    "https://onerecord.iata.org/Item": "Item",
    "https://onerecord.iata.org/LiveAnimalsEpermit": "LiveAnimalsEpermit",
    "https://onerecord.iata.org/PackagingType": "PackagingType",
    "https://onerecord.iata.org/PieceDg": "PieceDg",
    "https://onerecord.iata.org/PieceLiveAnimals": "PieceLiveAnimals",
    "https://onerecord.iata.org/Piece": "Piece",
    "https://onerecord.iata.org/Price": "Price",
    "https://onerecord.iata.org/ProductDg": "ProductDg",
    "https://onerecord.iata.org/Product": "Product",
    "https://onerecord.iata.org/Ranges": "Ranges",
    "https://onerecord.iata.org/Ratings": "Ratings",
    "https://onerecord.iata.org/Request": "Request",
    "https://onerecord.iata.org/Routing": "Routing",
    "https://onerecord.iata.org/Schedule": "Schedule",
    "https://onerecord.iata.org/SecurityDeclaration": "SecurityDeclaration",
    "https://onerecord.iata.org/SensorGeoloc": "SensorGeoloc",
    "https://onerecord.iata.org/SensorOther": "SensorOther",
    "https://onerecord.iata.org/Sensor": "Sensor",
    "https://onerecord.iata.org/ServiceRequest": "ServiceRequest",
    "https://onerecord.iata.org/Shipment": "Shipment",
    "https://onerecord.iata.org/SpecialHandling": "SpecialHandling",
    "https://onerecord.iata.org/TransportMeans": "TransportMeans",
    "https://onerecord.iata.org/TransportMovement": "TransportMovement",
    "https://onerecord.iata.org/TransportSegment": "TransportSegment",
    "https://onerecord.iata.org/ULD": "ULD",
    "https://onerecord.iata.org/Waybill": "Waybill",
}


def dict_to_logistics_object(
    logistics_object_dict: dict,
) -> Optional[LogisticsObject]:
    if "@type" in logistics_object_dict:
        logistics_object_type: Optional[str] = next(
            (
                t
                for t in type_class_mapping
                if t in logistics_object_dict["@type"]
            ),
            None,
        )
        if logistics_object_type:
            module = importlib.import_module("onerecord.models.cargo")
            class_ = getattr(module, type_class_mapping[logistics_object_type])
            return class_(**logistics_object_dict)
    return None


def json_to_logistics_object(
    logistics_object_json: str,
) -> Optional[LogisticsObject]:
    """Parses the given dict to a LogisticObject"""
    logistics_object_dict: dict = json.loads(logistics_object_json)
    return dict_to_logistics_object(
        logistics_object_dict=logistics_object_dict
    )


def json_to_logistics_objects(
    logistics_objects_json: str,
) -> list[LogisticsObject]:
    """Parses the given JSON to a list of LogisticObject"""
    logistic_objects: list[LogisticsObject] = []
    logistics_objects_list: list = json.loads(logistics_objects_json)
    if len(logistics_objects_list) > 0:
        for logistics_object_dict in logistics_objects_list:
            logistics_object: Optional[
                LogisticsObject
            ] = dict_to_logistics_object(
                logistics_object_dict=logistics_object_dict
            )
            if logistics_object:
                logistic_objects.append(logistics_object)

    return logistic_objects


def json_to_events(events_json: str) -> list[Event]:
    """Parses the given JSON to a list of Event"""
    events: list[Event] = []
    events_list: list = json.loads(events_json)
    if len(events_list) > 0:
        for event_dict in events_list:
            event: Event = Event(**event_dict)
            if event:
                events.append(event)
    return events
