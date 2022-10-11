import datetime
import importlib
import json
from typing import Any, Optional

from pydantic import PositiveInt

from onerecord.models import Thing
from onerecord.models.api import (
    LogisticsObjectRef,
    Operation,
    OperationObject,
    PatchRequest,
)
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
    "https://onerecord.iata.org/Value": "Value",
    "https://onerecord.iata.org/Waybill": "Waybill",
}
data_type_iri_mapping: dict = {
    str: "http://www.w3.org/2001/XMLSchema#string",
    bool: "http://www.w3.org/2001/XMLSchema#boolean",
    float: "http://www.w3.org/2001/XMLSchema#double",
    int: "http://www.w3.org/2001/XMLSchema#integer",
    PositiveInt: "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
    datetime.timedelta: "http://www.w3.org/2001/XMLSchema#duration",
    datetime.datetime: "http://www.w3.org/2001/XMLSchema#dateTime",
}


def dict_to_thing(
    thing_dict: Any,
) -> Optional[Thing]:
    if type(thing_dict) in data_type_iri_mapping:
        return thing_dict
    if "@type" in thing_dict:
        input_thing_type: Optional[str] = next(
            (t for t in type_class_mapping if t in thing_dict["@type"]),
            None,
        )
        if input_thing_type:
            if type(thing_dict["@type"]) is str:
                thing_dict["@type"] = [thing_dict["@type"]]
            module = importlib.import_module("onerecord.models.cargo")
            class_ = getattr(module, type_class_mapping[input_thing_type])
            return class_(**thing_dict)
    return None


def dict_to_logistics_object(
    logistics_object_dict: dict,
) -> Optional[LogisticsObject]:
    if "@type" in logistics_object_dict:
        logistics_object_type: Optional[str] = next(
            (t for t in type_class_mapping if t in logistics_object_dict["@type"]),
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
    if logistics_object_dict:
        return dict_to_logistics_object(logistics_object_dict=logistics_object_dict)
    return None


def json_to_logistics_objects(
    logistics_objects_json: str,
) -> list[LogisticsObject]:
    """Parses the given JSON to a list of LogisticObject"""
    logistic_objects: list[LogisticsObject] = []
    logistics_objects_list: list = json.loads(logistics_objects_json)
    if len(logistics_objects_list) > 0:
        for logistics_object_dict in logistics_objects_list:
            logistic_object = dict_to_logistics_object(
                logistics_object_dict=logistics_object_dict
            )
            if logistic_object:
                logistic_objects.append(logistic_object)

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


def _generate_operation_object_from_patch(patch: dict) -> Optional[OperationObject]:
    if "value" in patch:
        value = str(patch["value"])
        if type(patch["value"]) in data_type_iri_mapping:
            return OperationObject(
                datatype=data_type_iri_mapping[type(patch["value"])],
                value=value,
            )
        elif hasattr(patch["value"], "type"):
            if type(patch["value"]) in data_type_iri_mapping:
                return OperationObject(
                    datatype=data_type_iri_mapping[type(patch["value"])],
                    value=value,
                )

            elif type(getattr(patch["value"], "type")) is str:
                return OperationObject(
                    datatype=getattr(patch["value"], "type"), value=value
                )
            elif type(getattr(patch["value"], "type")) is list:
                data_type_iri: Optional[str] = next(
                    (
                        t
                        for t in type_class_mapping
                        if t in getattr(patch["value"], "type")
                    ),
                    None,
                )
                if data_type_iri:
                    return OperationObject(datatype=data_type_iri, value=value)
    return None


def _generate_patches(src: Thing, dst: Thing) -> list[dict]:
    src_dict: dict = src.dict(exclude_none=True, by_alias=True)
    dst_dict: dict = dst.dict(exclude_none=True, by_alias=True)
    patches: list[dict] = []
    src_keys = set(src_dict.keys()) - {"id", "@id", "type", "@type"}
    dst_keys = set(dst_dict.keys()) - {"id", "@id", "type", "@type"}

    if src_keys and dst_keys:
        removed_properties = sorted(src_keys - dst_keys)
        for removed_property in removed_properties:
            patches.append(
                {
                    "op": "del",
                    "path": removed_property,
                    "value": dict_to_thing(src_dict[removed_property]),
                }
            )

        added_properties = sorted(dst_keys - src_keys)
        for added_property in added_properties:
            patches.append(
                {
                    "op": "add",
                    "path": added_property,
                    "value": dict_to_thing(dst_dict[added_property]),
                }
            )

        replaced_property_candidates = sorted(src_keys & dst_keys)
        for replaced_property_candidate in replaced_property_candidates:
            if (
                src_dict[replaced_property_candidate]
                != dst_dict[replaced_property_candidate]
            ):
                patches.append(
                    {
                        "op": "del",
                        "path": replaced_property_candidate,
                        "value": dict_to_thing(src_dict[replaced_property_candidate]),
                    }
                )

                patches.append(
                    {
                        "op": "add",
                        "path": replaced_property_candidate,
                        "value": dict_to_thing(dst_dict[replaced_property_candidate]),
                    }
                )

    return patches


def generate_patch_request(
    original_logistics_object: LogisticsObject,
    updated_logistics_object: LogisticsObject,
    requestor_company_identifier: str,
) -> PatchRequest:
    # TODO: must be further optimized and tested more thoroughly
    operations: list[Operation] = []
    patches: list[dict] = _generate_patches(
        original_logistics_object, updated_logistics_object
    )

    for patch in patches:
        patch["path"] = patch["path"].replace("~0", "~").replace("~1", "/")
        if patch["path"].startswith("/"):
            patch["path"] = patch["path"][1:]
        o = _generate_operation_object_from_patch(patch)
        if o:
            operations.append(
                Operation(
                    o=o,
                    op=patch["op"],
                    p=patch["path"],
                )
            )

    patch_request: PatchRequest = PatchRequest(
        logistics_object_ref=LogisticsObjectRef(
            logistics_object_id=original_logistics_object.id,
            logistics_object_type=original_logistics_object.type[0],
        ),
        revision=getattr(original_logistics_object, "revision")
        if hasattr(original_logistics_object, "revision")
        else 1,
        requestor_company_identifier=requestor_company_identifier,
        operations=operations,
    )
    return patch_request
