from datetime import datetime

from pydantic import Field, PositiveInt

from onerecord.enums import (
    ChangeRequestStatus,
    LogisticsObjectType,
    NotificationEventType,
)
from onerecord.models.cargo import Branch, Company, LogisticsObject, Thing

"""
Based on IATA ONE Record API Ontology Version 1.1 (2021-04-20)
see https://raw.githubusercontent.com/IATA-Cargo/ONE-Record/eb404f134c18f8aac0bfe51666c081ba971f3c4d/working_draft/ontology/IATA-1R-API-Ontology.ttl
"""


class AuditTrail(Thing):
    """
    Audit trail of a Logistics Object"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/AuditTrail", alias="@type"
    )
    change_requests: "list[ChangeRequest]" = Field(
        alias="https://onerecord.iata.org/api/AuditTrail#changeRequests",
        description="List of change requests that were sent as PATCH on for a Logistics Object",
    )
    errors: "list[Error]" = Field(
        default=None,
        alias="https://onerecord.iata.org/api/AuditTrail#errors",
        description="Non mandatory error details",
    )
    latest_revision: PositiveInt = Field(
        alias="https://onerecord.iata.org/api/AuditTrail#latestRevision",
        description="Latest revision of the Logistics Object",
    )
    lo_initial_snapshot: "Memento" = Field(
        alias="https://onerecord.iata.org/api/AuditTrail#loInitialSnapshot",
        description="Initial message of the Logistics Object at the creation moment, represented via a Memento",
    )
    logistics_object_ref: "LogisticsObjectRef" = Field(
        alias="https://onerecord.iata.org/api/AuditTrail#logisticsObjectRef",
        description="Logistics Object Reference for which the audit trail applies",
    )


class ChangeRequest(Thing):
    """
    Change Request for the audit trail"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/ChangeRequest", alias="@type"
    )
    company_id: str = Field(
        alias="https://onerecord.iata.org/api/ChangeRequest#companyId",
        description="Company which sent the change request",
    )
    patch_request: "PatchRequest" = Field(
        alias="https://onerecord.iata.org/api/ChangeRequest#patchRequest",
        description="PATCH body of a change request sent for a specific Logistics Object",
    )
    requesting_party: "Branch" = Field(
        alias="https://onerecord.iata.org/api/ChangeRequest#requestingParty",
        description="The party that has requested the change request",
    )
    status: ChangeRequestStatus = Field(
        alias="https://onerecord.iata.org/api/ChangeRequest#status",
        description="ACCEPTED or REJECTED",
    )
    timestamp: datetime = Field(
        alias="https://onerecord.iata.org/api/ChangeRequest#timestamp",
        description="Timestamp of the change request",
    )


class CompanyInformation(Thing):
    """
    Company information in the Internet of Logistics"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/CompanyInformation", alias="@type"
    )
    company: "Company" = Field(
        alias="https://onerecord.iata.org/api/CompanyInformation#company",
        description="Company details",
    )
    company_id: str = Field(
        alias="https://onerecord.iata.org/api/CompanyInformation#companyId",
        description="Company Id, for example airline code.",
    )
    errors: "list[Error]" = Field(
        default=None,
        alias="https://onerecord.iata.org/api/CompanyInformation#errors",
        description="Non mandatory error details",
    )
    server_endpoint: str = Field(
        alias="https://onerecord.iata.org/api/CompanyInformation#serverEndpoint",
        description="Endpoint of the company in the Internet of Logistics",
    )
    supported_content_types: list[str] = Field(
        alias="https://onerecord.iata.org/api/CompanyInformation#supportedContentTypes",
        description="Supported message types of the server",
    )
    supported_logistics_objects: list[str] = Field(
        alias="https://onerecord.iata.org/api/CompanyInformation#supportedLogisticsObjects",
        description="Supported logistics object types on the server",
    )


class DelegationRequest(Thing):
    """
    Delegation Request to 3rd parties"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/DelegationRequest", alias="@type"
    )
    action: str = Field(
        alias="https://onerecord.iata.org/api/DelegationRequest#action",
        description="REVOKE or DELEGATE",
    )
    operations: list[str] = Field(
        alias="https://onerecord.iata.org/api/DelegationRequest#operations",
        description="GET or PATCH",
    )
    target_companies: list[str] = Field(
        alias="https://onerecord.iata.org/api/DelegationRequest#targetCompanies",
        description="Parties that receive the delegated rights",
    )
    target_logistics_objects: "list[LogisticsObjectRef]" = Field(
        alias="https://onerecord.iata.org/api/DelegationRequest#targetLogisticsObjects",
        description="Identifiers of the logistics objects to which the access is requested",
    )


class Details(Thing):
    """
    Error details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Details", alias="@type"
    )
    attribute: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Details#attribute",
        description="Field of the object for which the error applies",
    )
    code: str = Field(
        alias="https://onerecord.iata.org/api/Details#code",
        description="Error code",
    )
    message: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Details#message",
        description="Message of the error",
    )
    resource: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Details#resource",
        description="Object for which the error applies",
    )


class Error(Thing):
    """
    Error model"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Error", alias="@type"
    )
    details: "list[Details]" = Field(
        alias="https://onerecord.iata.org/api/Error#details",
        description="Error details",
    )
    title: str = Field(
        alias="https://onerecord.iata.org/api/Error#title",
        description="Brief description of the error",
    )


class LogisticsObjectRef(Thing):
    """
    Reference to a Logistics Object"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/LogisticsObjectRef", alias="@type"
    )
    logistics_object_id: str = Field(
        alias="https://onerecord.iata.org/api/LogisticsObjectRef#logisticsObjectId",
        description="Id of the reference Logistics Object",
    )
    logistics_object_type: LogisticsObjectType = Field(
        alias="https://onerecord.iata.org/api/LogisticsObjectRef#logisticsObjectType",
        description="Type of the reference Logistics Object",
    )


class Memento(Thing):
    """
    Version of a Logistics Object"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Memento", alias="@type"
    )
    created: datetime = Field(
        alias="https://onerecord.iata.org/api/Memento#created",
        description="Date and time of the memento creation",
    )
    created_by: str = Field(
        alias="https://onerecord.iata.org/api/Memento#createdBy",
        description="Name of the memento creator",
    )
    data: "LogisticsObject" = Field(
        alias="https://onerecord.iata.org/api/Memento#data",
        description="The actual data",
    )
    label: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Memento#label",
        description="Label of the memento",
    )
    original: str = Field(
        alias="https://onerecord.iata.org/api/Memento#original",
        description="First version of the Logistics Object",
    )


class MementoEntry(Thing):
    """
    Memento entry from the time map"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/MementoEntry", alias="@type"
    )
    date_time: datetime = Field(
        alias="https://onerecord.iata.org/api/MementoEntry#datetime",
        description="Creation date of the memento",
    )
    label: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/MementoEntry#label",
        description="Non mandatory label of the memento",
    )
    memento: "Memento" = Field(
        alias="https://onerecord.iata.org/api/MementoEntry#memento",
        description="Link to the memento",
    )


class MementoList(Thing):
    """
    Memento list model"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/MementoList", alias="@type"
    )
    memento_entry: "list[MementoEntry]" = Field(
        alias="https://onerecord.iata.org/api/MementoList#mementoEntry",
        description="List of mementos of a Logistics Object",
    )


class Mementos(Thing):
    """
    Memento list model"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Mementos", alias="@type"
    )
    first_memento: str = Field(
        alias="https://onerecord.iata.org/api/Mementos#firstMemento",
        description="First memento of the Logistics Object",
    )
    last_memento: str = Field(
        alias="https://onerecord.iata.org/api/Mementos#lastMemento",
        description="Last memento of the Logistics Object",
    )
    list: "MementoList" = Field(
        alias="https://onerecord.iata.org/api/Mementos#list",
        description="List of mementos of a Logistics Object",
    )


class Notification(Thing):
    """
    Notification sent by the publisher to the subscriber"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Notification", alias="@type"
    )
    event_type: NotificationEventType = Field(
        alias="https://onerecord.iata.org/api/Notification#eventType",
        description="OBJECT_CREATED or OBJECT_UPDATED",
    )
    logistics_object: "LogisticsObject" = Field(
        alias="https://onerecord.iata.org/api/Notification#logisticsObject",
        description="Logistics Object for which the notification is sent",
    )
    topic: str = Field(
        alias="https://onerecord.iata.org/api/Notification#topic",
        description="Type of Logistics Object",
    )


class Operation(Thing):
    """
    Operation Request contained in the PATCH body"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Operation", alias="@type"
    )
    o: "OperationObject" = Field(
        alias="https://onerecord.iata.org/api/Operation#o",
        description="PATCH object to modify",
    )
    op: str = Field(
        alias="https://onerecord.iata.org/api/Operation#op",
        description="Operation objects must have exactly one op (operation) member; this value indicates which operation is to be performed. The value must be one of add or del; all other values result in an error",
    )
    p: str = Field(
        alias="https://onerecord.iata.org/api/Operation#p",
        description="Operations objects must have exactly one p, predicate, member. The value of this member must be an IRI",
    )


class OperationObject(Thing):
    """
    Object to modify in the PATCH request"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/OperationObject", alias="@type"
    )
    datatype: str = Field(
        alias="https://onerecord.iata.org/api/OperationObject#datatype",
        description="Data type of the field to update",
    )
    value: str = Field(
        alias="https://onerecord.iata.org/api/OperationObject#value",
        description="Value to update",
    )


class PatchRequest(Thing):
    """
    PATCH Request body containing updates on a Logistics Object"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/PatchRequest", alias="@type"
    )
    description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/PatchRequest#description",
        description="Reason for the change (optional)",
    )
    logistics_object_ref: "LogisticsObjectRef" = Field(
        alias="https://onerecord.iata.org/api/PatchRequest#logisticsObjectRef",
        description="Reference of the Logistics Object to which the "
        "change request is applied to",
    )
    operations: "list[Operation]" = Field(
        alias="https://onerecord.iata.org/api/PatchRequest#operations",
        description="List of operations to apply as PATCH on a "
        "Logistics Object",
    )
    requestor_company_identifier: str = Field(
        alias="https://onerecord.iata.org/api/PatchRequest#requestorCompanyIdentifier",
        description="The company identifier of the entity that is "
        "requesting the change request",
    )
    revision: str = Field(
        alias="https://onerecord.iata.org/api/PatchRequest#revision",
        description="Revision number of the Logistics Object",
    )


class Subscription(Thing):
    """
    Subscription information sent to the publisher"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Subscription", alias="@type"
    )
    cache_for: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#cacheFor",
        description="Duration of the period to cache the subscription information in seconds",
    )
    callback_url: str = Field(
        alias="https://onerecord.iata.org/api/Subscription#callbackUrl",
        description="Callback URL of the Client Subscription API where the subscriber receives Logistics Objects",
    )
    content_types: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#contentTypes",
        description="Content types that the subscriber wants to receive in the notifications",
    )
    errors: "list[Error]" = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#errors",
        description="Non mandatory error details",
    )
    my_company_identifier: str = Field(
        alias="https://onerecord.iata.org/api/Subscription#myCompanyIdentifier",
        description="The company identifier from the Internet of Logistics of my company.",
    )
    secret: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#secret",
        description="Either a secret or API Key that ensures that only companies with this subscription information can POST to the subscriber callback endpoint",
    )
    send_logistics_object_body: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#sendLogisticsObjectBody",
        description="Flag specifying if the publisher should send the whole logistics object or not in the notification object",
    )
    subscribe_to_status_updates: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Subscription#subscribeToStatusUpdates",
        description="Flag specifying if the subscriber wants to receive updates for a Logistics Object",
    )
    subscribed_to: str = Field(
        alias="https://onerecord.iata.org/api/Subscription#subscribedTo",
        description="Company Identifier of the company the subscriber wants to subscribe to (delegation scenario).",
    )
    topic: str = Field(
        alias="https://onerecord.iata.org/api/Subscription#topic",
        description="The Logistics Object type to which the subscriber wants subscribe to",
    )


class Timemap(Thing):
    """
    Timemap of a Logistics Object containing mementos and timegate URI"""

    type: list[str] = Field(
        "https://onerecord.iata.org/api/Timemap", alias="@type"
    )
    mementos: "Mementos" = Field(
        alias="https://onerecord.iata.org/api/Timemap#mementos",
        description="List of mementos of a Logistics Object",
    )
    original: str = Field(
        alias="https://onerecord.iata.org/api/Timemap#original",
        description="Link to the initial version of the Logistics Object",
    )
    timegate: str = Field(
        default=None,
        alias="https://onerecord.iata.org/api/Timemap#timegate",
        description="Link to the time gate of the Logistics Object, if applicable",
    )


AuditTrail.update_forward_refs()
ChangeRequest.update_forward_refs()
CompanyInformation.update_forward_refs()
DelegationRequest.update_forward_refs()
Details.update_forward_refs()
Error.update_forward_refs()
LogisticsObjectRef.update_forward_refs()
Memento.update_forward_refs()
MementoEntry.update_forward_refs()
MementoList.update_forward_refs()
Mementos.update_forward_refs()
Notification.update_forward_refs()
Operation.update_forward_refs()
OperationObject.update_forward_refs()
PatchRequest.update_forward_refs()
Subscription.update_forward_refs()
Timemap.update_forward_refs()
