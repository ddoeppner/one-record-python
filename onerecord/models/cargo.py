from datetime import datetime

from pydantic import Field

from onerecord.models import Thing

"""
Based on IATA ONE Record Cargo Ontology Version 2.0.0 (2022-05-16)
see https://raw.githubusercontent.com/IATA-Cargo/ONE-Record/eb404f134c18f8aac0bfe51666c081ba971f3c4d/working_draft/ontology/IATA-1R-DM-Ontology.ttl
"""


class Address(Thing):
    """
    Address details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Address", alias="@type"
    )
    address_code: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#addressCode",
        description="Address identifier using special coding systems e.g. US CBP FIRMS code",
    )
    address_code_type: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#addressCodeType",
        description="Type of address code e.g. US CBP FIRMS",
    )
    city_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#cityCode",
        description="UN/LOCODE city code (5 letter) or IATA city code (3 letter)",
    )
    city_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#cityName",
        description="If no CityCode provided, full name of the city",
    )
    country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#country",
        description="Country details",
    )
    po_box: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#poBox",
        description="Post Office box number / code",
    )
    postal_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#postalCode",
        description="Postal / ZIP code",
    )
    region_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#regionCode",
        description="Region/ State / Department. Refer ISO 3166-2",
    )
    region_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#regionName",
        description="If no StateCode provided, full name of the region / state / province / canton",
    )
    street: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Address#street",
        description="Street address including street name, street number, building number, apartment etc",
    )


class BookingSegment(Thing):
    """
    Booking Segment refers to the arrival and location details of a Booking Option Request or a Booking Option (offer or actual booking)"""

    type: list[str] = Field(
        "https://onerecord.iata.org/BookingSegment", alias="@type"
    )
    arrival_location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingSegment#arrivalLocation",
        description="The arrival location of the Booking Segment",
    )
    booking_options: "list[BookingOption]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingSegment#bookingOptions",
        description="The Booking Option linked to the Booking Segment",
    )
    departure_location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingSegment#departureLocation",
        description="The departure location of the Booking Segment",
    )
    preferred_transport_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingSegment#preferredTransportId",
        description="When part of the Request it refers to the preferred Transport ID from the customer. When part of the BookingOption (offer or actual booking) it refers to the expected Transport ID or flight",
    )
    requests: "list[BookingOptionRequest]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingSegment#requests",
        description="The BookingOptionRequest linked to the Booking Segment",
    )


class Branch(Thing):
    """
    Company branches"""

    type: list[str] = Field("https://onerecord.iata.org/Branch", alias="@type")
    company: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Branch#company",
        description="Refers to the mother company of the branch",
    )
    contact_person: "list[Person]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Branch#contactPerson",
        description="Contact person details",
    )
    location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/Branch#location",
        description="Location and address details",
    )
    other_identifier: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Branch#otherIdentifier",
        description="Other identifiers (e.g. LEI (Legal Entity Identifier), TIN (Trader Identification Number), PIMA address, Account number, VAT/Tax id, Legal Registration id, DUNS number, etc)",
    )
    iata_cargo_agent_location_identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#iataCargoAgentLocationIdentifier",
        description="IATA CASS cargo agent 4 digit branch number / location identifier",
    )


class CommonObjects(Thing):
    type: list[str] = Field(
        "https://onerecord.iata.org/CommonObjects", alias="@type"
    )
    company_identifier: str = Field(
        alias="https://onerecord.iata.org/CommonObjects#companyIdentifier",
        description="Company identifier from the Internet of Logistics of the entity that hosts the Common Object.",
    )


class Company(Thing):
    """
    Company details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Company", alias="@type"
    )
    branch: "CompanyBranch" = Field(
        default=None,
        alias="https://onerecord.iata.org/Company#branch",
        description="Company branches",
    )
    company_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Company#companyName",
        description="Name of company or organization",
    )
    iata_cargo_agent_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Company#iataCargoAgentCode",
        description="IATA accredited cargo agent 7 digit number",
    )


class CompanyBranch(Thing):
    """
    Company branches"""

    type: list[str] = Field(
        "https://onerecord.iata.org/CompanyBranch", alias="@type"
    )
    branch_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#branchName",
        description="Company branch name",
    )
    company: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#company",
        description="Refers to the mother company of the branch",
    )
    contact_persons: "list[Person]" = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#contactPersons",
        description="Contact person details",
    )
    location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#location",
        description="Location and address details",
    )
    other_identifiers: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/CompanyBranch#otherIdentifiers",
        description="Other identifiers (e.g. LEI (Legal Entity Identifier), TIN (Trader Identification Number), PIMA address, Account number, VAT/Tax id, Legal Registration id, DUNS number, etc)",
    )


class Contact(Thing):
    """
    Contact details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Contact", alias="@type"
    )
    contact_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Contact#contactType",
        description="Type of the contact details, e.g. Phone number, Mail address",
    )
    contact_value: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Contact#contactValue",
        description="Value of the contact detail, e.g. phone number",
    )
    other: "ContactOther" = Field(
        default=None,
        alias="https://onerecord.iata.org/Contact#other",
        description="Other contact options e.g. Skype, Whatsapp, Viber, Fax etc",
    )


class ContactOther(Thing):
    """
    Other contact options e.g. Skype, Whatsapp, Viber, Fax etc"""

    type: list[str] = Field(
        "https://onerecord.iata.org/ContactOther", alias="@type"
    )


class Country(Thing):
    """
    Country details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Country", alias="@type"
    )
    country_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Country#countryCode",
        description="Country ISO code. Refer ISO 3166-2",
    )
    country_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Country#countryName",
        description="Full country name, Refer ISO 3166-2",
    )


class Dimensions(Thing):
    """
    Dimension details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Dimensions", alias="@type"
    )
    height: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Dimensions#height",
        description="Height",
    )
    length: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Dimensions#length",
        description="Length",
    )
    volume: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Dimensions#volume",
        description="Volume",
    )
    width: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Dimensions#width",
        description="Width",
    )


class EmbeddedObject(Thing):
    """
    Embedded Object parent class, containing all common properties for Embedded Object"""

    type: list[str] = Field(
        "https://onerecord.iata.org/EmbeddedObject", alias="@type"
    )


class Event(Thing):
    """
    Event details"""

    type: list[str] = Field("https://onerecord.iata.org/Event", alias="@type")
    date_time: datetime = Field(
        alias="https://onerecord.iata.org/Event#dateTime",
        description="Date and time of the event",
    )
    event_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#eventCode",
        description="Movement or milestone code. Can refer to CXML Code List 1.18, e.g. DEP, ARR, FOH, RCS but not restricted to it.",
    )
    event_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#eventName",
        description="If no EventCode provided, event name - e.g. Security clearance",
    )
    event_type_indicator: str = Field(
        alias="https://onerecord.iata.org/Event#eventTypeIndicator",
        description="Indicates type of event e.g.  Scheduled, Estimated, Actual",
    )
    linked_object: "LogisticsObject" = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#linkedObject",
        description="Refers to the URI of the linked object(s)",
    )
    location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#location",
        description="Location of event",
    )
    performed_by: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#performedBy",
        description="Party performing the event",
    )
    performed_by_person: "Person" = Field(
        default=None,
        alias="https://onerecord.iata.org/Event#performedByPerson",
        description="",
    )


class ExternalReference(Thing):
    """
    Reference documents details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/ExternalReference", alias="@type"
    )
    document_checksum: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentChecksum",
        description="Checksum of the document to validate its integrity",
    )
    document_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentId",
        description="Unique document identifier",
    )
    document_link: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentLink",
        description="Link to the document, e.g. URL of the file where it is hosted",
    )
    document_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentName",
        description="If no DocumentType provided, name of the referenced document",
    )
    document_originator: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentOriginator",
        description="Document originator details and contacts",
    )
    document_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentType",
        description="Type of the referenced document . Can refer UNEDIFACT 1001  e.g. 740 - Air Waybill, but not limited to",
    )
    document_version: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#documentVersion",
        description="Document version number",
    )
    expiry_date: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#expiryDate",
        description="Document expiry date",
    )
    location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#location",
        description="Location of the document, e.g. location where the document was emitted",
    )
    valid_from: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/ExternalReference#validFrom",
        description="Document validity start date",
    )


class Geolocation(Thing):
    """
    Geolocation details - e.g. for drones, automated vehicles..."""

    type: list[str] = Field(
        "https://onerecord.iata.org/Geolocation", alias="@type"
    )
    elevation: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Geolocation#elevation",
        description="Elevation from sea level - Change of data type to Value as of ontology v1.1",
    )
    geolocation_unit: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Geolocation#geolocationUnit",
        description="re of the Geolocation coordinates, standard is Degree",
    )
    latitude: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Geolocation#latitude",
        description="Location latitude - Change of data type to string as of version 1.2",
    )
    longitude: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Geolocation#longitude",
        description="Location longitude - Change of data type to string as of version 1.2",
    )


class HandlingInstructions(Thing):
    """
    Used to provide handling instructions such as Special service request (SSR), Special handling codes (SPH) or Other service information (OSI)"""

    type: list[str] = Field(
        "https://onerecord.iata.org/HandlingInstructions", alias="@type"
    )
    requested_by: "Person" = Field(
        default=None,
        alias="https://onerecord.iata.org/HandlingInstructions#requestedBy",
        description="Refers to the person that requests the handling/service",
    )
    service_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/HandlingInstructions#serviceDescription",
        description="Free text description of the handling instructions",
    )
    service_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/HandlingInstructions#serviceType",
        description="Refers to the type of handling information provided: Special Service Request (SSR), Special Handling Codes (SPH) or Other Service Information (OSI)",
    )
    service_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/HandlingInstructions#serviceTypeCode",
        description="Service Type code linked top the Service Type.Refers to Code List 1.14 or 1.16 if service type is Special Handling.",
    )


class Location(Thing):
    """
    Loading location details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Location", alias="@type"
    )
    address: "Address" = Field(
        default=None,
        alias="https://onerecord.iata.org/Location#address",
        description="Address details",
    )
    code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Location#code",
        description="Location code of airport, freight terminal, seaport, rail station. UN/LOCODE city code (5 letter) or IATA airport code (3 letter)",
    )
    geolocation: "Geolocation" = Field(
        default=None,
        alias="https://onerecord.iata.org/Location#geolocation",
        description="Geolocation details",
    )
    location_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Location#locationName",
        description="Full name of the location",
    )
    location_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Location#locationType",
        description="Location type - e.g. Airport, Freight terminal, Rail station, Seaport, etc",
    )


class LogisticsObject(Thing):
    """
    Logistics Object parent class, containing all common properties for logistics objects."""

    type: list[str] = Field(
        "https://onerecord.iata.org/LogisticsObject", alias="@type"
    )
    company_identifier: str = Field(
        alias="https://onerecord.iata.org/LogisticsObject#companyIdentifier",
        description="Company identifier from the Internet of Logistics of the entity that hosts the Logistics Object.",
    )
    events: "list[Event]" = Field(
        default=None,
        alias="https://onerecord.iata.org/LogisticsObject#events",
        description="Events object",
    )
    iot_devices: "list[IotDevice]" = Field(
        default=None,
        alias="https://onerecord.iata.org/LogisticsObject#iotDevices",
        description="Allows to link Logistic Objects with IoT Devices",
    )


class Measurements(Thing):
    """
    Measurements details for Sensors, either generic or geolocation measurements are recorded"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Measurements", alias="@type"
    )
    measurement_timestamp: datetime = Field(
        alias="https://onerecord.iata.org/Measurements#measurementTimestamp",
        description="Timestamp for the measurement",
    )


class MovementTimes(Thing):
    """
    Times refering to Transport Movements, used to describe specfic times such as Actual Departure time, etc."""

    type: list[str] = Field(
        "https://onerecord.iata.org/MovementTimes", alias="@type"
    )
    direction: str = Field(
        default=None,
        alias="https://onerecord.iata.org/MovementTimes#direction",
        description="Direction to indicate if it's Inbound or Outbound",
    )
    movement_milestone: str = Field(
        default=None,
        alias="https://onerecord.iata.org/MovementTimes#movementMilestone",
        description="The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.",
    )
    movement_timestamp: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/MovementTimes#movementTimestamp",
        description="Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.",
    )
    time_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/MovementTimes#timeType",
        description="The type of time can be Actual, Estimated ot Scheduled",
    )


class OtherIdentifier(Thing):
    """
    Other identifiers"""

    type: list[str] = Field(
        "https://onerecord.iata.org/OtherIdentifier", alias="@type"
    )
    identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/OtherIdentifier#identifier",
        description="Item identifier",
    )
    other_identifier_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/OtherIdentifier#otherIdentifierType",
        description="Identifier type or description",
    )


class OtherParty(Thing):
    """
    Company details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/OtherParty", alias="@type"
    )
    company_details: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/OtherParty#companyDetails",
        description="Company details",
    )


class Party(Thing):
    """
    Refers to a Company and its role in a specific context, e.g Company A as shipper. Cargo-XML Code List 1.15 can be used as a reference with the addition of Notify Party"""

    type: list[str] = Field("https://onerecord.iata.org/Party", alias="@type")
    other_identifiers: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Party#otherIdentifiers",
        description="Reference to other identifiers for parties. In the context of the AWB, otherIdentifier object can be used with types 'PrimaryID' (internal ID), 'Additional ID' (Standard ID) or 'AccountID' (Account numbers).",
    )
    party_details: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Party#partyDetails",
        description="Reference to the Company",
    )
    party_role: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Party#partyRole",
        description="Role fo the Company in the context. Can refer to Code List 1.36 in the CXML Toolkit",
    )


class Person(Thing):
    """
    Person details"""

    type: list[str] = Field("https://onerecord.iata.org/Person", alias="@type")
    associated_branch: "CompanyBranch" = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#associatedBranch",
        description="Refers to the Branch the person is associated with",
    )
    contact: "list[Contact]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#contact",
        description="Contact details",
    )
    contact_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#contactType",
        description="Contact type - e.g. Emergency contact, Customs contact, Customer contact",
    )
    department: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#department",
        description="Department / Division / Unit",
    )
    documents: "list[ExternalReference]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#documents",
        description="Linked documents to the person, e.g. driver's license, ID, etc.",
    )
    employee_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#employeeId",
        description="Employee ID",
    )
    first_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#firstName",
        description="First name / given name",
    )
    job_title: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#jobTitle",
        description="Job title / position",
    )
    last_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#lastName",
        description="Last name / family name / surname",
    )
    middle_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#middleName",
        description="Middle name/ other name",
    )
    salutation: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Person#salutation",
        description="Salutation",
    )


class RegulatedEntity(Thing):
    """
    Regulated Entity"""

    type: list[str] = Field(
        "https://onerecord.iata.org/RegulatedEntity", alias="@type"
    )
    entity: "CompanyBranch" = Field(
        alias="https://onerecord.iata.org/RegulatedEntity#entity",
        description="Branch/Company",
    )
    expiry_date: datetime = Field(
        alias="https://onerecord.iata.org/RegulatedEntity#expiryDate",
        description="Expiry date 4 digits month/year",
    )
    regulated_entity_category: str = Field(
        default=None,
        alias="https://onerecord.iata.org/RegulatedEntity#regulatedEntityCategory",
        description="Party type - e.g. RA - Regulated Agent, KC - Known Consignor, AO - Aircraft Operator, RC - Regulated Carrier",
    )
    regulated_entity_identifier: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/RegulatedEntity#regulatedEntityIdentifier",
        description="Regulated entity identifier (e.g. Regulated Agent Identifier) is mandatory",
    )


class ScheduledLegs(Thing):
    """
    Scheduled Legs class to be used to identify legs. Can be used with Booking Option Request as an indicator of preferred Routing or with Booking Option when a carrier proposes a specific Routing."""

    type: list[str] = Field(
        "https://onerecord.iata.org/ScheduledLegs", alias="@type"
    )
    arrival_date: list[datetime] = Field(
        default=None,
        alias="https://onerecord.iata.org/ScheduledLegs#arrivalDate",
        description="Arrival date and time of the leg",
    )
    arrival_location: "Location" = Field(
        alias="https://onerecord.iata.org/ScheduledLegs#arrivalLocation",
        description="Arrival location of the leg",
    )
    departure_date: list[datetime] = Field(
        default=None,
        alias="https://onerecord.iata.org/ScheduledLegs#departureDate",
        description="Departure date and time of the leg",
    )
    departure_location: "Location" = Field(
        alias="https://onerecord.iata.org/ScheduledLegs#departureLocation",
        description="Departure Location of the leg",
    )
    sequence_number: int = Field(
        alias="https://onerecord.iata.org/ScheduledLegs#sequenceNumber",
        description="Sequence number of the leg",
    )
    transport_id: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/ScheduledLegs#transportId",
        description="Transport Id of the leg. E.g. Flight number, truck route identifier, etc.",
    )


class Value(Thing):
    """
    Volumetric weight details"""

    type: list[str] = Field("https://onerecord.iata.org/Value", alias="@type")
    unit: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Value#unit",
        description="Unit of measurement/ unit of account e.g. CMT - Centimetre,  LTR - Litre (1 DM3), KGM - Kilogram, CHF - Swiss Franc",
    )
    value: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Value#value",
        description="Value",
    )


class VolumetricWeight(Thing):
    """
    Unit of measurement details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/VolumetricWeight", alias="@type"
    )
    chargeable_weight: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/VolumetricWeight#chargeableWeight",
        description="Chargeable weight",
    )
    conversion_factor: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/VolumetricWeight#conversionFactor",
        description="Volume to weight conversion factor",
    )


class Booking(LogisticsObject):
    """
    Booking details - Deprecated, BookingOption should be used instead"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Booking", alias="@type"
    )
    carrier: "list[Company]" = Field(
        alias="https://onerecord.iata.org/Booking#carrier",
        description="Carrier details",
    )
    carrier_product_info: "CarrierProduct" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#carrierProductInfo",
        description="Reference to the Carrier products included in the offer",
    )
    consignee: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#consignee",
        description="Consignee details",
    )
    freight_forwarder: "list[Company]" = Field(
        alias="https://onerecord.iata.org/Booking#freightForwarder",
        description="Freight Forwarder details",
    )
    notify_party: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#notifyParty",
        description="Other parties to be notified of the booking evolution",
    )
    price: "Price" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#price",
        description="Price of the Booking (if different from the offer)",
    )
    request_ref: "Request" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#requestRef",
        description="Reference to the Request",
    )
    routing: "Routing" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#routing",
        description="Routing details of the offer, to be compared with routing preferences of the quote request",
    )
    shipment_details: "Shipment" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#shipmentDetails",
        description="Details of the shipement that is to be shipped",
    )
    shipper: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#shipper",
        description="Shipper information",
    )
    transport_movement: "TransportSegment" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#transportMovement",
        description="Transport segment linked to the offer, including the Departure and Arrival locations",
    )
    waybill_number: "Waybill" = Field(
        default=None,
        alias="https://onerecord.iata.org/Booking#waybillNumber",
        description="House or Master Waybill unique identifier",
    )


class BookingOption(LogisticsObject):
    """
    Booking details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/BookingOption", alias="@type"
    )
    booking_segment: "BookingSegment" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#bookingSegment",
        description="Booking Segment of the Booking Option",
    )
    booking_status: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#bookingStatus",
        description="Status of the Booking with regards to the step in the Sales and Booking process: Quoted, Booked (to be confirmed)",
    )
    booking_times: "BookingTimes" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#bookingTimes",
        description="booking times details of the Booking Option (proposed or actual)",
    )
    carrier: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#carrier",
        description="Carrier details",
    )
    carrier_product_info: "CarrierProduct" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#carrierProductInfo",
        description="Reference to the Carrier products included in the offer",
    )
    consignee: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#consignee",
        description="Consignee details",
    )
    freight_forwarder: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#freightForwarder",
        description="Freight forwarder details",
    )
    notify_party: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#notifyParty",
        description="Other parties to be notified of the booking evolution",
    )
    offer_valid_from: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#offerValidFrom",
        description="Starting datetime of availability of the booking option",
    )
    offer_valid_to: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#offerValidTo",
        description="Ending datetime of availability of the booking option",
    )
    parties: "list[Party]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#parties",
        description="Parties involved in the Booking Option (e.g. shipper, forwarder, ...)",
    )
    price: "Price" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#price",
        description="Price of the Booking (if different from the offer)",
    )
    request_match_ind: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#requestMatchInd",
        description="Indicates if the offer is a perfect match to the quote request (boolean)",
    )
    request_ref: "BookingOptionRequest" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#requestRef",
        description="Reference to the Booking option request",
    )
    routing: "Routing" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#routing",
        description="Routing details of the offer, to be compared with routing preferences of the quote request",
    )
    schedule: "Schedule" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#schedule",
        description="Schedule details of the Booking Option (proposed or actual)",
    )
    shipment_details: "Shipment" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#shipmentDetails",
        description="Details of the shipement that is to be shipped",
    )
    shipment_security_status: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#shipmentSecurityStatus",
        description="Indicate the secruty state of the shipment, screened or not",
    )
    shipper: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#shipper",
        description="Shipper details",
    )
    transport_movement: "list[TransportSegment]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#transportMovement",
        description="Transport segment linked to the offer, including the Departure and Arrival locations",
    )
    waybill_number: "Waybill" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOption#waybillNumber",
        description="House or Master Waybill unique identifier",
    )


class BookingOptionRequest(LogisticsObject):
    """
    Request object, refers to the Quote request or Booking request"""

    type: list[str] = Field(
        "https://onerecord.iata.org/BookingOptionRequest", alias="@type"
    )
    allotment: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#allotment",
        description="Reference to the Allotment as per the contracts between forwarders and carriers",
    )
    booking_segment: "BookingSegment" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#bookingSegment",
        description="The Booking Segment linked to the Booking Optio Request",
    )
    expected_commodities: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#expectedCommodities",
        description="Expected commodity for quote request purposes only. To be defined by MCD",
    )
    parties: "list[Party]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#parties",
        description="Parties involved if known",
    )
    ratings_preference: "Ratings" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#ratingsPreference",
        description="Ratings preferences of the request",
    )
    request_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#requestType",
        description="Identification of the request type: Quote or Booking (to be confirmed)",
    )
    requested_handling: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#requestedHandling",
        description="Requested handling information for quote request purposes only",
    )
    routing_preferences: "Routing" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#routingPreferences",
        description="Routing details that are part of the request, these details will be used to determine if the offer is a perfect match",
    )
    schedule_preferences: "list[Schedule]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#schedulePreferences",
        description="Schedule preferences of the request",
    )
    shipment_details: "Shipment" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#shipmentDetails",
        description="Details of the shipement that is to be shipped",
    )
    shipment_security_status: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#shipmentSecurityStatus",
        description="Indicate the security state of the shipment, screened or not",
    )
    time_preferences: "BookingTimes" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#timePreferences",
        description="Schedule preferences of the request",
    )
    transport_movement: "list[TransportSegment]" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#transportMovement",
        description="Transport segment linked to the request, including the Departure and Arrival locations requested",
    )
    units_preference: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingOptionRequest#unitsPreference",
        description="Unit preferences of the request (e.g. kg or cm)",
    )


class BookingTimes(LogisticsObject):
    """
    Previsouly called Schedule. This object refers to times used for the Booking Option Request (preferences part of the request) or the Booking Option (times sur as LAT where there is a commitment from the carrier)"""

    type: list[str] = Field(
        "https://onerecord.iata.org/BookingTimes", alias="@type"
    )
    booking_option: "BookingOption" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#bookingOption",
        description="Reference to the BookingOption where the booking times are used",
    )
    booking_option_request: "BookingOptionRequest" = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#bookingOptionRequest",
        description="Reference to the BookingOptionRequest where the booking times are used",
    )
    earliest_acceptance_time: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#earliestAcceptanceTime",
        description="Earliest acceptance date time (requested or proposed)",
    )
    latest_acceptance_time: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#latestAcceptanceTime",
        description="Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)",
    )
    time_of_availability: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#timeOfAvailability",
        description="Time of availability of the shipment as per CargoIQ definition",
    )
    total_transit_time: str = Field(
        default=None,
        alias="https://onerecord.iata.org/BookingTimes#totalTransitTime",
        description="Total transit time as per CargoIQ definition, expressed as a duration",
    )


class CO2CalcMethod(LogisticsObject):
    """
    CO2 calculation methods"""

    type: list[str] = Field(
        "https://onerecord.iata.org/CO2CalcMethod", alias="@type"
    )


class CO2Emissions(LogisticsObject):
    """
    CO2 Calculation"""

    type: list[str] = Field(
        "https://onerecord.iata.org/CO2Emissions", alias="@type"
    )
    calculated_emissions: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/CO2Emissions#calculatedEmissions",
        description="CO2 emissions calculated",
    )
    method_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CO2Emissions#methodName",
        description="Name of the CO2 calculation method",
    )
    method_version: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CO2Emissions#methodVersion",
        description="Version used for the calculation",
    )
    transport_movement: "TransportMovement" = Field(
        default=None,
        alias="https://onerecord.iata.org/CO2Emissions#transportMovement",
        description="Transport Movement linked to the CO2 Emissions object",
    )


class Carrier(Company):
    """
    Company details of carriers"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Carrier", alias="@type"
    )
    airline_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Carrier#airlineCode",
        description="IATA two-character airline code",
    )
    airline_prefix: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Carrier#airlinePrefix",
        description="IATA three-numeric airline prefix number",
    )
    carrier_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Carrier#carrierName",
        description="Official carrier name",
    )
    carrier_short_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Carrier#carrierShortName",
        description="Carrier short name if any",
    )


class CarrierProduct(LogisticsObject):
    """
    Carrier product details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/CarrierProduct", alias="@type"
    )
    booking_option: "BookingOption" = Field(
        default=None,
        alias="https://onerecord.iata.org/CarrierProduct#bookingOption",
        description="Reference to the BookingOption where the carrier product is used",
    )
    product_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CarrierProduct#productCode",
        description="Carrier's product code",
    )
    product_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CarrierProduct#productDescription",
        description="Carrier's product description",
    )


class Characteristics(LogisticsObject):
    """
    Product additional details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Characteristics", alias="@type"
    )
    characteristics_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Characteristics#characteristicsType",
        description="Product characteristics code - e.g. CLR - Color. Not restricted to a list.",
    )
    product: "Product" = Field(
        default=None,
        alias="https://onerecord.iata.org/Characteristics#product",
        description="Reference to the product",
    )
    value: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Characteristics#value",
        description="Product characteristics value / attribute - e.g. Blue...",
    )


class CustomsInfo(LogisticsObject):
    """
    Customs information details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/CustomsInfo", alias="@type"
    )
    customs_info_content_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#customsInfoContentCode",
        description="Customs, Security and Regulatory Control Information Identifier. Coded indicator qualifying Customs related information: Item Number 'I', Exemption Legend 'L', System Downtime Reference 'S', Unique Consignment Reference Number 'U', Movement Reference Number 'M' .Refers to Code List 1.100Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed",
    )
    customs_info_country_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#customsInfoCountryCode",
        description="Customs country code. Refer ISO 3166-2Condition:  At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed",
    )
    customs_info_note: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#customsInfoNote",
        description="Free text for customs remarks, not used in OCI Composition Rules Table",
    )
    customs_info_subject_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#customsInfoSubjectCode",
        description="Information Identifier. Code identifying a piece of information/entity e.g. 'IMP' for import, 'EXP' for export, 'AGT' for Agent, 'ISS' for The Regulated Agent Issuing the Security Status for a Consignment etc. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed",
    )
    customs_information: str = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#customsInformation",
        description="Supplementary Customs, Security and Regulatory Control Information",
    )
    piece: "Piece" = Field(
        default=None,
        alias="https://onerecord.iata.org/CustomsInfo#piece",
        description="Piece on which the Customs Info is applicable",
    )


class DgDeclaration(LogisticsObject):
    """
    Dangerous goods declaration"""

    type: list[str] = Field(
        "https://onerecord.iata.org/DgDeclaration", alias="@type"
    )
    aircraft_limitation_information: str = Field(
        alias="https://onerecord.iata.org/DgDeclaration#aircraftLimitationInformation",
        description="Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air)",
    )
    compliance_declaration_text: str = Field(
        alias="https://onerecord.iata.org/DgDeclaration#complianceDeclarationText",
        description="Contains the warning message complying with the regulations text note. This field is mandatory for air (Air)",
    )
    exclusive_use_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/DgDeclaration#exclusiveUseIndicator",
        description="Indicates an exclusive use shipment",
    )
    handling_information: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgDeclaration#handlingInformation",
        description="Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances.",
    )
    shipper_declaration_text: str = Field(
        alias="https://onerecord.iata.org/DgDeclaration#shipperDeclarationText",
        description="Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)",
    )


class DgProductRadioactive(LogisticsObject):
    """
    Details of the radioactive products"""

    type: list[str] = Field(
        "https://onerecord.iata.org/DgProductRadioactive", alias="@type"
    )
    dg_ra_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgProductRadioactive#dgRaTypeCode",
        description="The category of the package or all packed in one. Complete text to be transmitted: I-White, II-Yellow, III-Yellow instead of I, II, III",
    )
    fissile_exception_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/DgProductRadioactive#fissileExceptionIndicator",
        description="Indicates if Fissile is excepted",
    )
    fissile_exception_reference: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgProductRadioactive#fissileExceptionReference",
        description="Fissile exception reference, mandatory if Fissile Exception Indicator is true.",
    )
    isotopes: "DgRadioactiveIsotope" = Field(
        default=None,
        alias="https://onerecord.iata.org/DgProductRadioactive#isotopes",
        description="DgRadioactiveIsotope.",
    )
    transport_index_numeric: int = Field(
        default=None,
        alias="https://onerecord.iata.org/DgProductRadioactive#transportIndexNumeric",
        description="Radioactive Transport-Index value of the package or all packed in one. Conditionally mandator and applies to categories II-Yellow and III-Yellow only; field only contains the value, if printed, TI must be added as a prefix to the value  to be printed in the Packing Instructions column",
    )


class DgRadioactiveIsotope(LogisticsObject):
    """
    Details of the radioactive isotope contained in the product"""

    type: list[str] = Field(
        "https://onerecord.iata.org/DgRadioactiveIsotope", alias="@type"
    )
    activity_level_measure: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#activityLevelMeasure",
        description="Numeric expression of the activity of a radioactive Item",
    )
    criticality_safety_index_numeric: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#criticalitySafetyIndexNumeric",
        description="Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.",
    )
    isotope_id: str = Field(
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#isotopeId",
        description="Id of each radionuclide or for mixtures of radionuclides.",
    )
    isotope_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#isotopeName",
        description="The name or symbol of each radionuclide or for mixtures of radionuclides, an appropriate general description, or a list of the most restrictive radionuclides.",
    )
    low_dispersible_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#lowDispersibleIndicator",
        description="A notation that the material is low dispersible radioactive material.",
    )
    physical_chemical_form: str = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#physicalChemicalForm",
        description="A description of the physical and chemical form of the material.",
    )
    special_form_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/DgRadioactiveIsotope#specialFormIndicator",
        description="A notation that the material is special form",
    )


class EpermitConsignment(LogisticsObject):
    """
    Details of the pieces (Live animals) of the permit and specific information such as quantity measured and used to date quota"""

    type: list[str] = Field(
        "https://onerecord.iata.org/EpermitConsignment", alias="@type"
    )
    consignment_items: "PieceLiveAnimals" = Field(
        alias="https://onerecord.iata.org/EpermitConsignment#consignmentItems",
        description="Reference to te pieces (Live Animals) of the permit",
    )
    examining_quantity: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/EpermitConsignment#examiningQuantity",
        description="Quatity measured by the examining authority (box 14)",
    )
    used_to_date_quota_quantity: int = Field(
        default=None,
        alias="https://onerecord.iata.org/EpermitConsignment#usedToDateQuotaQuantity",
        description="total number of specimens exported in the current calendar year and the current annuela quota for the species concerned (box 11a)",
    )


class EpermitSignature(LogisticsObject):
    """
    Signature details of the Epermit for Live Animals"""

    type: list[str] = Field(
        "https://onerecord.iata.org/EpermitSignature", alias="@type"
    )
    security_stamp_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/EpermitSignature#securityStampId",
        description="Security Stamp ID",
    )
    signatory_company: "Company" = Field(
        alias="https://onerecord.iata.org/EpermitSignature#signatoryCompany",
        description="Signatory company name",
    )
    signatory_role: str = Field(
        alias="https://onerecord.iata.org/EpermitSignature#signatoryRole",
        description="Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority",
    )
    signature_date: datetime = Field(
        alias="https://onerecord.iata.org/EpermitSignature#signatureDate",
        description="Date and time of the signature",
    )
    signature_statement: str = Field(
        default=None,
        alias="https://onerecord.iata.org/EpermitSignature#signatureStatement",
        description="Signatory signature authentication text",
    )
    signature_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/EpermitSignature#signatureTypeCode",
        description="Code specifying a type of government action such as inspection, detention, fumigation, security.",
    )


class EventUld(Event):
    """
    Subtype of Event"""

    type: list[str] = Field(
        "https://onerecord.iata.org/EventUld", alias="@type"
    )
    loading_position: str = Field(
        default=None,
        alias="https://onerecord.iata.org/EventUld#loadingPosition",
        description="Position of the shipment in the aircraft - e.g. lower or main deck",
    )


class Insurance(LogisticsObject):
    """
    Insurance details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Insurance", alias="@type"
    )
    covering_party: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Insurance#coveringParty",
        description="Party covering the insurance",
    )
    insurance_amount: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Insurance#insuranceAmount",
        description="Insured amount - amount covered by the insurance policy",
    )
    insurance_shipment: "Shipment" = Field(
        alias="https://onerecord.iata.org/Insurance#insuranceShipment",
        description="Reference to the shipment insured",
    )
    nvd_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Insurance#nvdIndicator",
        description="When no value is declared for Insurance this field should be completed with the value TRUE otherwise FALSE",
    )


class IotDevice(LogisticsObject):
    """
    IoT Device details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/IotDevice", alias="@type"
    )
    associated_object: str = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#associatedObject",
        description="Reference of the Logistic Object to which the Connected Device is linked (URI)",
    )
    device_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#deviceDescription",
        description="Natural language description of the device. It can describe how and where the device is attached.",
    )
    device_manufacturer: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#deviceManufacturer",
        description="Manufacturer of the device",
    )
    device_model: str = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#deviceModel",
        description="Commercial denomination of the device",
    )
    device_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#deviceName",
        description="Name of the device defined by the device's owner",
    )
    device_serial_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#deviceSerialNumber",
        description="Serial number that allows to uniquely identify the device",
    )
    sensors: "list[Sensor]" = Field(
        default=None,
        alias="https://onerecord.iata.org/IotDevice#sensors",
        description="Reference to the sensors linked to the device",
    )


class Item(LogisticsObject):
    """
    Item details"""

    type: list[str] = Field("https://onerecord.iata.org/Item", alias="@type")
    batch_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#batchNumber",
        description="Production batch number / reference",
    )
    dimensions: "Dimensions" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#dimensions",
        description="Dimensions of the item",
    )
    is_in_piece: "Piece" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#isInPiece",
        description="URI of the PIECE that contains the Item",
    )
    lot_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#lotNumber",
        description="Production lot number / reference",
    )
    other_identifiers: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#otherIdentifiers",
        description="Other identifier details",
    )
    product: "Product" = Field(
        alias="https://onerecord.iata.org/Item#product",
        description="URI of the product",
    )
    product_expiry_date: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#productExpiryDate",
        description="Product expiry date - e.g. for perishables goods or goods with programmed obsolescence",
    )
    production_country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#productionCountry",
        description="Production country details",
    )
    production_date: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#productionDate",
        description="Production date",
    )
    quantity: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#quantity",
        description="Quantity of the item when applicable, witth associated units of measure",
    )
    quantity_for_unit_price: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#quantityForUnitPrice",
        description="Product quantity for unit price - e.g. 12 (eggs for one USD 1)",
    )
    target_country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#targetCountry",
        description="Item target country",
    )
    unit_price: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#unitPrice",
        description="Product price per unit in the base",
    )
    weight: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Item#weight",
        description="Weight of the item",
    )


class ItemDg(Item):
    """
    Dangerous Goods subtype of Item"""

    type: list[str] = Field("https://onerecord.iata.org/ItemDg", alias="@type")
    emergency_contact: "Person" = Field(
        alias="https://onerecord.iata.org/ItemDg#emergencyContact",
        description="Contains the Emergency contact name (e.g. the name of the agency) and phone number (min required)",
    )
    net_weight_measure: "Value" = Field(
        alias="https://onerecord.iata.org/ItemDg#netWeightMeasure",
        description="The total net weight of dangerous goods transported of this line item. For air transport the value must be the volume or mass in each package.",
    )
    reportable_quantity: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ItemDg#reportableQuantity",
        description="Reportable quantities, To and from the USA only",
    )
    supplementary_info_prefix: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ItemDg#supplementaryInfoPrefix",
        description="Additional information that may be added in addition to the proper shipping name to more fully describe the goods or to identify a particular condition",
    )
    supplementary_info_suffix: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ItemDg#supplementaryInfoSuffix",
        description="Additional information that may be added in addition to the proper shipping to more fully describe the goods or to identify a particular condition",
    )


class LiveAnimalsEpermit(LogisticsObject):
    """
    Epermit for Live Animals details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/LiveAnimalsEpermit", alias="@type"
    )
    consignee: "Company" = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#consignee",
        description="Consignee company details, including complete name and address (box 3)",
    )
    consignments: "list[EpermitConsignment]" = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#consignments",
        description="Reference to the pieces and properties linked to the Permit (box 7 to 12)",
    )
    permit_copy_indicator: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitCopyIndicator",
        description="Indicates if the permit is a copy (true) or an original (false) (box 1)",
    )
    permit_number: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitNumber",
        description="The original number is a unique number allocated to each document by the relevant Management Authority. (box 1)",
    )
    permit_type_code: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitTypeCode",
        description="Code specifying the document name. (box 1)",
    )
    permit_type_other: str = Field(
        default=None,
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitTypeOther",
        description="Description if TypeCode is Other (box 1)",
    )
    permit_valid_from: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitValidFrom",
        description="Permit Valid from (box 2)",
    )
    permit_valid_until: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#permitValidUntil",
        description="Permit Valid until (box 2)",
    )
    signatures: "list[EpermitSignature]" = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#signatures",
        description="List of all the signatures of the Epermit (applicant box 4, issuing authority box 6, issuer box 13 and examining authority box 14)",
    )
    special_conditions: str = Field(
        default=None,
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#specialConditions",
        description="Special conditions (box 5)",
    )
    transaction_purpose_code: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#transactionPurposeCode",
        description="Code indicating the purpose of the transaction (box 5a)",
    )
    transaction_purpose_text: str = Field(
        default=None,
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#transactionPurposeText",
        description="Purpose of the transaction in free text (box 5a)",
    )
    transport_contract_id: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#transportContractId",
        description="Reference to the Air Waybill or other transport contract document (box 15)",
    )
    transport_contract_type_code: str = Field(
        alias="https://onerecord.iata.org/LiveAnimalsEpermit#transportContractTypeCode",
        description="Code specifying the transport document name (box 15)",
    )


class MeasurementsGeoloc(Measurements):
    """
    Measurements details for Geolocation sensors"""

    type: list[str] = Field(
        "https://onerecord.iata.org/MeasurementsGeoloc", alias="@type"
    )
    geolocation_measurement: "Geolocation" = Field(
        default=None,
        alias="https://onerecord.iata.org/MeasurementsGeoloc#geolocationMeasurement",
        description="Geolocation measurements details",
    )


class MeasurementsOther(Measurements):
    """
    Measurements details for sensors that are not geolocation sensors"""

    type: list[str] = Field(
        "https://onerecord.iata.org/MeasurementsOther", alias="@type"
    )
    generic_measurement: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/MeasurementsOther#genericMeasurement",
        description="Value for measurements other than Geolocation, includes value and unit of measure as described in the Interactive Cargo RP",
    )


class PackagingType(LogisticsObject):
    """
    Packaging details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/PackagingType", alias="@type"
    )
    packaging_type_description: str = Field(
        alias="https://onerecord.iata.org/PackagingType#packagingTypeDescription",
        description="Free Text. Describes the package type.",
    )
    piece: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/PackagingType#piece",
        description="Piece on which the Packaging type is applicable",
    )
    type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PackagingType#typeCode",
        description="Packaging type identifier as per UNECE Rec 21 Annex V and VI e.g. 1A - Drum, steel - Packaging material code. Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations",
    )


class Piece(LogisticsObject):
    """
    Individual piece or virtual grouping of pieces"""

    type: list[str] = Field("https://onerecord.iata.org/Piece", alias="@type")
    coload: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#coload",
        description="Coload indicator for the pieces (boolean)",
    )
    contained_items: "list[Item]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#containedItems",
        description="Reference to the item(s) contained in the piece",
    )
    contained_pieces: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#containedPieces",
        description="Details of contained piece(s)",
    )
    customs_info: "list[CustomsInfo]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#customsInfo",
        description="Customs details",
    )
    declared_value_for_carriage: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#declaredValueForCarriage",
        description="The value of a shipment declared for carriage purposes , NVD if no value declared",
    )
    declared_value_for_customs: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#declaredValueForCustoms",
        description="The value of a shipment declared for customs purposes , NVD if no value declared",
    )
    dimensions: "Dimensions" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#dimensions",
        description="Dimensions details",
    )
    external_references: "list[ExternalReference]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#externalReferences",
        description="Reference documents details",
    )
    goods_description: str = Field(
        alias="https://onerecord.iata.org/Piece#goodsDescription",
        description="General goods description",
    )
    gross_weight: "Value" = Field(
        alias="https://onerecord.iata.org/Piece#grossWeight",
        description="Weight details",
    )
    handling_instructions: "list[HandlingInstructions]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#handlingInstructions",
        description="Links to Handling instructions / service requests of the piece",
    )
    load_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#loadType",
        description="Specify how the piece will be delivered (bulk or ULD)",
    )
    nvd_for_carriage: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#nvdForCarriage",
        description="When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE",
    )
    nvd_for_customs: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#nvdForCustoms",
        description="When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE",
    )
    other_identifiers: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#otherIdentifiers",
        description="Other piece identification ( e.g. Shipping Marks, Seal)",
    )
    other_party: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#otherParty",
        description="Other party company details - e.g. the party to be notified",
    )
    package_mark_coded: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#packageMarkCoded",
        description="Reference identifying how the package is marked. Field is hardcode to 'SSCC-18', 'UPC' or 'Other'",
    )
    packagede_identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#packagedeIdentifier",
        description="SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.",
    )
    packaging_type: "PackagingType" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#packagingType",
        description="Packaging details",
    )
    parties: "list[Party]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#parties",
        description="Other party company details - e.g. the party to be notified",
    )
    product: "list[Product]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#product",
        description="Product of the piece, mandatory when there are no items",
    )
    production_country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#productionCountry",
        description="Goods production country, mandatory when there are no Items",
    )
    security_declaration: "SecurityDeclaration" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#securityDeclaration",
        description="Security details of the piece",
    )
    security_status: "SecurityDeclaration" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#securityStatus",
        description="Security details",
    )
    service_request: "list[ServiceRequest]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#serviceRequest",
        description="Security requests",
    )
    shipment: "Shipment" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#shipment",
        description="Shipment on which the piece is assigned to",
    )
    shipper: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#shipper",
        description="Shipper company details - e.g. the party shipping the piece",
    )
    shipping_marks: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#shippingMarks",
        description="Shipping marks",
    )
    slac: int = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#slac",
        description="Shipper's Load And Count  ( total contained piece count as provided by shipper)",
    )
    special_handling: "list[SpecialHandling]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#specialHandling",
        description="Special Handling details",
    )
    stackable: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#stackable",
        description="Stackable indicator for the pieces (boolean)",
    )
    transport_movements: "list[TransportMovement]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#transportMovements",
        description="Transport Movements on which the piece is transported",
    )
    transport_segments: "list[TransportSegment]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#transportSegments",
        description="Segment related to the transport status",
    )
    turnable: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#turnable",
        description="Turnable indicator for the pieces (boolean)",
    )
    uld_reference: "ULD" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#uldReference",
        description="ULD on which the (virtual) piece has been loaded into - URIs of the ULD",
    )
    upid: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#upid",
        description="Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689",
    )
    volumetric_weight: "VolumetricWeight" = Field(
        default=None,
        alias="https://onerecord.iata.org/Piece#volumetricWeight",
        description="Volumetric weight details",
    )
    booking_ref: "list[Booking]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#bookingRef",
        description="Reference to the Booking or Offer",
    )
    grand_total: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#grandTotal",
        description="Total price",
    )
    ratings: "list[Ratings]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#ratings",
        description="Rating used for pricing",
    )
    valid_to: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#validTo",
        description="Terms of validity",
    )


class PieceDg(Piece):
    """
    Dangerous Goods subtype of Piece"""

    type: list[str] = Field(
        "https://onerecord.iata.org/PieceDg", alias="@type"
    )
    all_packed_in_one_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#allPackedInOneIndicator",
        description="A statement identifying that the dangerous goods listed above are all contained in the same outer packaging. Takes the form All packed in one aaaa (description of packaging type) x nn (number of packages). Applies to air transport only. (Air)",
    )
    dg_declaration: "DgDeclaration" = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#dgDeclaration",
        description="Reference to the Dangerous Goods declaration",
    )
    overpack_criticality_safety_index_numeric: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#overpackCriticalitySafetyIndexNumeric",
        description="Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.",
    )
    overpack_indicator: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#overpackIndicator",
        description="Overpack indicator",
    )
    overpack_t1: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#overpackT1",
        description="A single number assigned to a package, overpack or freight container to provide control over radiation exposure.",
    )
    overpack_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#overpackTypeCode",
        description="Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations",
    )
    q_value_numeric: float = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceDg#qValueNumeric",
        description="Most instances of all packed in one will require the addition of the Q value which  1. Applies to air transport only. (Air)",
    )


class PieceLiveAnimals(Piece):
    """
    LiveAnimals subclass of Piece"""

    type: list[str] = Field(
        "https://onerecord.iata.org/PieceLiveAnimals", alias="@type"
    )
    acquisition_datetime: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#acquisitionDatetime",
        description="Defined in Resolution Conf. 13.6 and is required for pre-Convention specimens (box 12b)",
    )
    annual_quota_quantity: int = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#annualQuotaQuantity",
        description="total number of specimens exported in the current calendar year and the current annuela quota for the species concerned (box 11a)",
    )
    associated_epermit: "EpermitConsignment" = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#associatedEpermit",
        description="Reference to the permits associated with the Live Animals",
    )
    category_code: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#categoryCode",
        description="Operations code ID. Refers to the number of the registered captive-breeding or artifical propagation operation (box 12b)",
    )
    export_trade_country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#exportTradeCountry",
        description="Country of last re-export (box 12a)",
    )
    goods_type_code: str = Field(
        alias="https://onerecord.iata.org/PieceLiveAnimals#goodsTypeCode",
        description="Appendix number of the convention (I, II or III) (box 10)",
    )
    goods_type_extension_code: str = Field(
        alias="https://onerecord.iata.org/PieceLiveAnimals#goodsTypeExtensionCode",
        description="Appendix number of the convention (I, II or III) (box 10)",
    )
    origin_reference_permit_datetime: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#originReferencePermitDatetime",
        description="Issuing date for Origin reference permit or re-export reference Certificate (box 12)",
    )
    origin_reference_permit_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#originReferencePermitId",
        description="identifier of Origin reference permit or re-export reference Certificate (box 12/12a)",
    )
    origin_reference_permit_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#originReferencePermitTypeCode",
        description="Document type code of origin reference permit or re-export reference Certificate (box 12/12a)",
    )
    origin_trade_country: "Country" = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#originTradeCountry",
        description="country of origin (box 12)",
    )
    quantity_animals: int = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#quantityAnimals",
        description="Quantity including units (box 11)",
    )
    species_common_name: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#speciesCommonName",
        description="Species common name (box 8)",
    )
    species_scientific_name: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#speciesScientificName",
        description="Species scientific name (box 7)",
    )
    specimen_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#specimenDescription",
        description="Description of specimens, including age and sex if LA (box 9)",
    )
    specimen_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/PieceLiveAnimals#specimenTypeCode",
        description="Description of specimens, CITES type code (box 9)",
    )


class Price(LogisticsObject):
    """
    Price associated to the offer/booking"""

    type: list[str] = Field("https://onerecord.iata.org/Price", alias="@type")
    booking_option: "BookingOption" = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#bookingOption",
        description="Reference to the Booking or Offer",
    )
    carrier_charge_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Price#carrierChargeCode",
        description="Charge code for carrier, eg. CA, CB, etc",
    )


class Product(LogisticsObject):
    """
    Product details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Product", alias="@type"
    )
    characteristics: "list[Characteristics]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#characteristics",
        description="Charateristics of the product",
    )
    commodity_item_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#commodityItemNumber",
        description="Indicates the specific commodity on which the rate class code is applied",
    )
    hs_code: str = Field(
        alias="https://onerecord.iata.org/Product#hsCode",
        description="Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.",
    )
    hs_commodity_description: str = Field(
        alias="https://onerecord.iata.org/Product#hsCommodityDescription",
        description="Commodity description",
    )
    hs_commodity_name: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#hsCommodityName",
        description="If no Code provided, name of commodity",
    )
    hs_type: str = Field(
        alias="https://onerecord.iata.org/Product#hsType",
        description="Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits",
    )
    is_in_items: "list[Item]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#isInItems",
        description="Reference to the Items in which the product can be found.",
    )
    is_in_pieces: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#isInPieces",
        description="Reference to the pieces where the product can be found. This needs to be filled in case there is no Item",
    )
    manufacturer: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#manufacturer",
        description="Manufacturing company details and contacts",
    )
    other_identifier: "list[OtherIdentifier]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#otherIdentifier",
        description="Other product identifier (e.g. Bar code, UPC, EAN, Amazon)",
    )
    product_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#productDescription",
        description="Product description",
    )
    product_identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Product#productIdentifier",
        description="Manufacturer's unique product identifier",
    )


class ProductDg(Product):
    """
    Dangerous Goods subtype of Product"""

    type: list[str] = Field(
        "https://onerecord.iata.org/ProductDg", alias="@type"
    )
    additional_hazard_classification_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#additionalHazardClassificationId",
        description="Identifies the subsidiary hazard class / division identification containing a numeric field separated by a decimal. There may be 0, 1 or 2 subsidiary risk classes or divisions. If there is more than one, each should be separated by a comma. The subsidiary risk must be shown in parentheses.",
    )
    authorization_information: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#authorizationInformation",
        description="Contains additional information relating to an approval, permission or other specific detail applicable to the commodity (e.g. Dangerous Goods in excepted quantities)",
    )
    dg_radioactive_material: "DgProductRadioactive" = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#dgRadioactiveMaterial",
        description="Dg Radioactive Material",
    )
    explosive_compatibility_group_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#explosiveCompatibilityGroupCode",
        description="Specifies the reference to the group which identifies the kind of substances and articles that are deemed to be compatible. Mandatory field in case of transport of explosive articles or substances",
    )
    hazard_classification_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#hazardClassificationId",
        description="Identifies the hazard class / division identification containing a numeric field separated by a decimal",
    )
    packaging_danger_level_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#packagingDangerLevelCode",
        description="Packing group, If used must reference I, II or III",
    )
    packing_instruction_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#packingInstructionNumber",
        description="The packing instruction number applicable to the UN number / proper shipping name entry. A three-numeric value which may be preceded by the letter Y.  Mandatory field for air transport (Air)",
    )
    proper_shipping_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#properShippingName",
        description="The name used to describe the particular article or substance as shown in the UN Model Regulations Dangerous Goods List",
    )
    special_provision_id: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#specialProvisionId",
        description="For Air Mode: Special Provision may show a single, double or triple digit number preceded by the letter A, against appropriate entries in the List of Dangerous Goods",
    )
    technical_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#technicalName",
        description="This is additional chemical name(s) required for some proper shipping names. When added the technical must be shown in parentheses immediately following the proper shipping name.",
    )
    un_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ProductDg#unNumber",
        description="Reference identifying the United Nations Dangerous Goods serial number assigned within the UN to substances and articles contained in a list of the dangerous goods most commonly carried. e.g. 1189 - Ethylene glycol monomethyl ether acetate",
    )


class Ranges(LogisticsObject):
    """
    Ranges details"""

    type: list[str] = Field("https://onerecord.iata.org/Ranges", alias="@type")
    amount: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#amount",
        description="Amount",
    )
    maximum_quantity: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#maximumQuantity",
        description="Maximum quantity",
    )
    minimum_quantity: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#minimumQuantity",
        description="Minimum quantity",
    )
    rate_class_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#rateClassCode",
        description="Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes",
    )
    rating_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#ratingType",
        description="rating type - Refer to CXML Code List 1.44 ULD Charge Codes",
    )
    scr: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#scr",
        description="Specific commodity rates linked to commodity",
    )
    unit_basis: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ranges#unitBasis",
        description="Specific commodity code linked to commodity",
    )


class Ratings(LogisticsObject):
    """
    Ratings details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Ratings", alias="@type"
    )
    billing_charge_identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#billingChargeIdentifier",
        description="Billing charge identifiers to be used for CASS. Refer to CargoXML Code List 1.33",
    )
    charge_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#chargeCode",
        description="Charge code, refer to CargoXML Code List 1.1",
    )
    charge_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#chargeDescription",
        description="Description of the charge e.g. Airfreight, fuel, etc.",
    )
    charge_payment_type: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#chargePaymentType",
        description="Indicates if charge is prepaid or collect (P, C)",
    )
    charge_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#chargeType",
        description="Type of charge that should match the code expressed in either chargeCode, otherChargeCode or billingChargeIndentifier data properties.",
    )
    entitlement: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#entitlement",
        description="Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3",
    )
    other_charge_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#otherChargeCode",
        description="Refer to CargoXML Code List 1.2 for Other Charges",
    )
    price_specification: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#priceSpecification",
        description="Specification of the price e.g. Street, Group, Spot, etc.",
    )
    price_specification_ref: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#priceSpecificationRef",
        description="Reference of price specifications",
    )
    quantity: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#quantity",
        description="Used if there is an applicable quantity to the rate (Usually a Time or a Number)",
    )
    ranges: "list[Ranges]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#ranges",
        description="Reference to the ranges",
    )
    ratings_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#ratingsType",
        description="Used to identify if the Ratings are Face, Published or Actual ratings. Expected values are F, A, C.",
    )
    rcp: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#rcp",
        description="IATA 3-letter code of the rate combination point",
    )
    sub_total: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Ratings#subTotal",
        description="Subtotal of the charge",
    )


class Request(LogisticsObject):
    """
    Request object, refers to the Quote request or Booking request"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Request", alias="@type"
    )
    parties: "OtherParty" = Field(
        default=None,
        alias="https://onerecord.iata.org/Request#parties",
        description="Parties involved if known",
    )
    ratings_preference: "Ratings" = Field(
        default=None,
        alias="https://onerecord.iata.org/Request#ratingsPreference",
        description="Ratings preferences of the request",
    )
    shipment_details: "Shipment" = Field(
        default=None,
        alias="https://onerecord.iata.org/Request#shipmentDetails",
        description="Details of the shipement that is to be shipped",
    )
    transport_movement: "TransportSegment" = Field(
        default=None,
        alias="https://onerecord.iata.org/Request#transportMovement",
        description="Transport segment linked to the request, including the Departure and Arrival locations requested",
    )
    units_preference: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/Request#unitsPreference",
        description="Unit preferences of the request (e.g. kg or cm)",
    )


class Routing(LogisticsObject):
    """
    Routing details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Routing", alias="@type"
    )
    aircraft_possibility_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#aircraftPossibilityCode",
        description="Aircraft possibility code",
    )
    booking_option: "BookingOption" = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#bookingOption",
        description="Reference to the BookingOption where the Routing is used",
    )
    latest_arrival_date_time: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#latestArrivalDateTime",
        description="Latest Arrival date time (requested or proposed)",
    )
    max_connections: int = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#maxConnections",
        description="Maximum number of connections of the transport movement (requested or proposed)",
    )
    online_ind: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#onlineInd",
        description="Indicates interlining (requested or proposed)",
    )
    rfs_ind: bool = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#rfsInd",
        description="Indicates if RFS (Road Feeder Services) is included (requested or proposed)",
    )
    scheduled_legs: "list[ScheduledLegs]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Routing#scheduledLegs",
        description="Scheduled Legs class to be used to identify legs. Can be used with Booking Option Request as an indicator of preferred Routing or with Booking Option when a carrier proposes a specific Routing.",
    )


class Schedule(LogisticsObject):
    """
    Scheduling details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Schedule", alias="@type"
    )
    earliest_acceptance_time: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Schedule#earliestAcceptanceTime",
        description="arliest acceptance date time (requested or proposed)",
    )
    latest_acceptance_time: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Schedule#latestAcceptanceTime",
        description="Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)",
    )
    time_of_availability: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Schedule#timeOfAvailability",
        description="Time of availability of the shipment as per CargoIQ definition",
    )
    total_transit_time: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Schedule#totalTransitTime",
        description="Total transit time as per CargoIQ definition",
    )


class SecurityDeclaration(LogisticsObject):
    """
    Security declaration details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/SecurityDeclaration", alias="@type"
    )
    additional_security_information: str = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#additionalSecurityInformation",
        description="Any additional information that may be required by an ICAO Member State",
    )
    grounds_for_exemption: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#groundsForExemption",
        description="Exemption code - e.g. BIOM- Bio-Medical Samples SMUS - small undersized shipments MAIL - mailBIOM - bio-medical samplesDIPL - diplomatic bags or diplomatic mailLFSM - life-saving materials NUCL - nuclear materialsTRNS - transfer or transshipment",
    )
    issued_by: "Person" = Field(
        alias="https://onerecord.iata.org/SecurityDeclaration#issuedBy",
        description="Name of person (or employee ID) who issued the security status",
    )
    issued_on: datetime = Field(
        alias="https://onerecord.iata.org/SecurityDeclaration#issuedOn",
        description="Date and time when the security status was issued",
    )
    other_regulated_entity: "list[RegulatedEntity]" = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#otherRegulatedEntity",
        description="Any other regulated entity that accepts custody of the cargo and accepts the security status originally issued",
    )
    other_screening_methods: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#otherScreeningMethods",
        description="Other methods used to secure the cargo",
    )
    piece: "Piece" = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#piece",
        description="Piece linked to the Security Declaration",
    )
    received_from: "RegulatedEntity" = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#receivedFrom",
        description="Regulated entity that tendered the consignment",
    )
    regulated_entity_issuer: "RegulatedEntity" = Field(
        alias="https://onerecord.iata.org/SecurityDeclaration#regulatedEntityIssuer",
        description="Regulated entity issuing the Security Declaration",
    )
    screening_method: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/SecurityDeclaration#screeningMethod",
        description="Screening methods which have been used to secure the cargoPHS – Physical Inspection and/or hand search VCK - Visual check XRY- X-ray equipment EDS - Explosive detection system EDD - Explosive detection dogsETD - Explosive trace detection equipment - particles or vapor CMD - Cargo metal detectionAOM - Subjected to any other means: this entry should be followed by free text specifying what other mean was used to secure the cargo",
    )
    security_status: str = Field(
        alias="https://onerecord.iata.org/SecurityDeclaration#securityStatus",
        description="Security status indicator (CXML 1.103) - e.g. SPX- Cargo Secure for Passenger and All-Cargo Aircraft",
    )


class Sensor(LogisticsObject):
    """
    Sensor details and measurements, linked to Connected Devices"""

    type: list[str] = Field("https://onerecord.iata.org/Sensor", alias="@type")
    iot_device: "list[IotDevice]" = Field(
        alias="https://onerecord.iata.org/Sensor#iotDevice",
        description="Reference to the IoT Device to which the sensor is linked",
    )
    sensor_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Sensor#sensorDescription",
        description="Natural language description of the sensor",
    )
    sensor_name: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Sensor#sensorName",
        description="Name of the sensor defined by the sensor's manufacturer",
    )
    sensor_serial_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Sensor#sensorSerialNumber",
        description="Serial number that allows to uniquely identify the sensor",
    )
    sensor_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Sensor#sensorType",
        description="Type of sensor as described in Interactive Cargo Recommended Practice",
    )


class SensorGeoloc(Sensor):
    """
    Sensor measurements details for Geolocation sensors (sensorType = Geolocation)"""

    type: list[str] = Field(
        "https://onerecord.iata.org/SensorGeoloc", alias="@type"
    )
    val: "list[MeasurementsGeoloc]" = Field(
        default=None,
        alias="https://onerecord.iata.org/SensorGeoloc#val",
        description="Reference to the measurements recorded by the geolocation sensor",
    )


class SensorOther(Sensor):
    """
    Sensor measurements details for sensors other than Geolocation sensors (sensorType != Geolocation)"""

    type: list[str] = Field(
        "https://onerecord.iata.org/SensorOther", alias="@type"
    )
    val: "list[MeasurementsOther]" = Field(
        default=None,
        alias="https://onerecord.iata.org/SensorOther#val",
        description="Reference to the measurements recorded by the sensor",
    )


class ServiceRequest(LogisticsObject):
    """
    Service request details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/ServiceRequest", alias="@type"
    )
    code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ServiceRequest#code",
        description="Service request code",
    )
    service_request_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ServiceRequest#serviceRequestDescription",
        description="Service request description",
    )
    statement_text: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ServiceRequest#statementText",
        description="Service request statement text",
    )
    statement_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ServiceRequest#statementType",
        description="Service request statement type - e.g. Dangerous Goods, Lithium Ion Battery, Live Animal Certificate",
    )


class Shipment(LogisticsObject):
    """
    Shipment details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Shipment", alias="@type"
    )
    contained_pieces: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#containedPieces",
        description="Details of contained piece(s)",
    )
    delivery_date: datetime = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#deliveryDate",
        description="he date at which the delivery is supposed to happen. Format is YYYYMMDD.",
    )
    delivery_location: "list[Location]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#deliveryLocation",
        description="Name and UN/LOCODE code of the point or port of departure, shipment or destination, as required under the applicable delivery term",
    )
    dimensions: "list[Dimensions]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#dimensions",
        description="Dimensions details",
    )
    external_references: "list[ExternalReference]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#externalReferences",
        description="Reference document details",
    )
    freight_forwarder: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#freightForwarder",
        description="Reference to the freight forwarder",
    )
    goods_description: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#goodsDescription",
        description="General goods description",
    )
    incoterms: list[str] = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#incoterms",
        description="Standard codes as defined by UNCEFACT and ICC that correspond to international rules for the interpretation of the most commonly used trade terms in different countries. UNECE recommendation n. 5 Incoterms 2000.",
    )
    insurance: "Insurance" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#insurance",
        description="Insurance details",
    )
    other_charges_indicator: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#otherChargesIndicator",
        description="payment of Other Charges will be made at origin (prepaid) or at destination (collect)",
    )
    parties: "list[Party]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#parties",
        description="Parties details",
    )
    shipper: "list[Company]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#shipper",
        description="Reference to the shipper",
    )
    total_gross_weight: "Value" = Field(
        alias="https://onerecord.iata.org/Shipment#totalGrossWeight",
        description="Weight details",
    )
    total_piece_count: int = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#totalPieceCount",
        description="Total Piece Count",
    )
    total_s_l_a_c: int = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#totalSLAC",
        description="Total SLAC of all piece groups",
    )
    volumetric_weight: "list[VolumetricWeight]" = Field(
        alias="https://onerecord.iata.org/Shipment#volumetricWeight",
        description="Volumetric weight details",
    )
    weight_valuation_indicator: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Shipment#weightValuationIndicator",
        description="payment for the Weight/Valuation will be made at origin (prepaid) or at destination (collect)",
    )


class SpecialHandling(LogisticsObject):
    """
    Special handling details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/SpecialHandling", alias="@type"
    )
    code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/SpecialHandling#code",
        description="Special handling code following IATA standards. Refer CXML1.16,  e.g. PEP - Fruits and Vegetables",
    )
    handling_text: str = Field(
        default=None,
        alias="https://onerecord.iata.org/SpecialHandling#handlingText",
        description="Special handling text",
    )


class TransportMeans(LogisticsObject):
    """
    Transport means details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/TransportMeans", alias="@type"
    )
    transport_company: "Company" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#transportCompany",
        description="Company operating the transport means",
    )
    transport_movement: "TransportMovement" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#transportMovement",
        description="Transport Movement on which the Transport Means is used",
    )
    transport_segment: "list[TransportSegment]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#transportSegment",
        description="Associated transport segment",
    )
    typical_c_o2_coefficient: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#typicalCO2Coefficient",
        description="Required for some CO2 calculations",
    )
    typical_fuel_consumption: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#typicalFuelConsumption",
        description="Typical fuel comsumption (e.g. 20 000L / 1 000nm)",
    )
    vehicle_model: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#vehicleModel",
        description="Model or make of the vehicle (e.g. A330-300)",
    )
    vehicle_registration: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#vehicleRegistration",
        description="Vehicle identification - e.g. aircraft registration number",
    )
    vehicle_size: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#vehicleSize",
        description="Size of the vehicle - free text",
    )
    vehicle_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMeans#vehicleType",
        description="Vehicle or container type. Refer UNECE28, e.g. 4.00.0 - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manua in section ATA/IATA Aircraft Types",
    )


class TransportMovement(LogisticsObject):
    """
    Transport movement details, replaces the TransportSegment in v1.1 and above"""

    type: list[str] = Field(
        "https://onerecord.iata.org/TransportMovement", alias="@type"
    )
    arrival_location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#arrivalLocation",
        description="Arrival location details",
    )
    distance_measured: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#distanceMeasured",
        description="Distance measured",
    )
    external_references: "ExternalReference" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#externalReferences",
        description="Reference to document or logistics object (URI)",
    )
    fuel_amount_calculated: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#fuelAmountCalculated",
        description="calculated fuel consumption, if measured not available",
    )
    fuel_amount_measured: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#fuelAmountMeasured",
        description="actual measured fuel consumption",
    )
    fuel_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#fuelType",
        description="e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]",
    )
    mode_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#modeCode",
        description="Mode of transport code, refer to UNECE Rec. 19https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_01cf19e.pdf",
    )
    mode_qualifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#modeQualifier",
        description="Pre-Carriage, Main-Carriage or On-Carriage",
    )
    movement_times: "list[MovementTimes]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#movementTimes",
        description="Reference to all Movement Times such as Departure, Arrival, etc.",
    )
    payload: "list[Value]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#payload",
        description="Actual payload for the transport",
    )
    seal: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#seal",
        description="Seal identifier",
    )
    transport_means_operators: "list[Person]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#transportMeansOperators",
        description="Name of the person operating the transport means (e.g. aircraft captain, truck driver)",
    )
    transported_pieces: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#transportedPieces",
        description="Pieces assigned to the transport segment",
    )
    unplanned_stop: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#unplannedStop",
        description="Free text field to be used for additional details regarding unplanned stops such as technical stops.",
    )


class TransportSegment(LogisticsObject):
    """
    Transport segment details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/TransportSegment", alias="@type"
    )
    co2_calculation_method: "CO2CalcMethod" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#co2CalculationMethod",
        description="Method of calculation of the CO2 emissions",
    )
    co2_emissions: "list[CO2Emissions]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#co2Emissions",
        description="Amount of CO2 emitted (e.g. 34 kg/km)",
    )
    departure_location: "Location" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#departureLocation",
        description="Departure location details",
    )
    distance_calculated: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#distanceCalculated",
        description="Distance calculated if distance measured is not available",
    )
    transport_identifier: str = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#transportIdentifier",
        description="Airline flight number, or rail /  truck / maritime line id",
    )
    transport_means: "TransportMeans" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#transportMeans",
        description="Transport means details",
    )
    transported_ulds: "list[ULD]" = Field(
        default=None,
        alias="https://onerecord.iata.org/TransportMovement#transportedUlds",
        description="ULDs assigned to the transport segment",
    )


class ULD(LogisticsObject):
    """
    Unit Load Device details"""

    type: list[str] = Field("https://onerecord.iata.org/ULD", alias="@type")
    ata_designator: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#ataDesignator",
        description="US / ATA Unit Load Device type code e.g. M2",
    )
    damage_flag: bool = Field(
        alias="https://onerecord.iata.org/ULD#damageFlag",
        description="Indicates if the ULD is Damaged",
    )
    demurrage_code: str = Field(
        alias="https://onerecord.iata.org/ULD#demurrageCode",
        description="Contains three designator of demurrage code, refer to RP 1654 (BCC, HHH, XXX, ZZZ)",
    )
    external_reference: "list[ExternalReference]" = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#externalReference",
        description="Reference documents details",
    )
    loading_indicator: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#loadingIndicator",
        description="ULD height or loading limitation code. Refer CXML Code List 1.47,  e.g. R - ULD Height above 244 centimetres",
    )
    nb_door: int = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#nbDoor",
        description="Number of doors",
    )
    nb_fittings: int = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#nbFittings",
        description="Number of fittings",
    )
    nb_nets: int = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#nbNets",
        description="Number of nets",
    )
    nb_straps: int = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#nbStraps",
        description="Number of straps",
    )
    odln_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#odlnCode",
        description="Contains two designator codes of ODLN or Operational Damage Limit Notices. ODLN code is used to define type of damage after visually check the serviceability of ULDs section 7, Standard Specifications 40/3 or 40/4 in ULD Regulations",
    )
    owner_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#ownerCode",
        description="Owner code of the ULD in aa, an or na format - owner can be an airline or leasing company",
    )
    serial_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#serialNumber",
        description="ULD serial number",
    )
    serviceability_code: str = Field(
        alias="https://onerecord.iata.org/ULD#serviceabilityCode",
        description="Designator of serviceablity condition e.g. SER or DAM",
    )
    tare_weight: "Value" = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#tareWeight",
        description="Tare weight of the empty ULD",
    )
    transport_movements: "list[TransportMovement]" = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#transportMovements",
        description="Transport Movements on which the ULD are transported",
    )
    transport_segments: "list[TransportSegment]" = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#transportSegments",
        description="Segment related to the ULD movement",
    )
    uld_remarks: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#uldRemarks",
        description="Remarks or Supplement Information",
    )
    uld_seal_number: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#uldSealNumber",
        description="ULD seal number if applicable",
    )
    uld_type_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#uldTypeCode",
        description="Standard Unit Load Device type code e.g. AKE - Certified Container - Contoured. Refer to IATA ULD Technical Manual",
    )
    upid: "list[Piece]" = Field(
        default=None,
        alias="https://onerecord.iata.org/ULD#upid",
        description="Details of contained (virtual) piece(s)",
    )


class Waybill(LogisticsObject):
    """
    Waybill details"""

    type: list[str] = Field(
        "https://onerecord.iata.org/Waybill", alias="@type"
    )
    accounting_information: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#accountingInformation",
        description="Indicates the details of accounting information. Free text e.g. PAYMENT BY CERTIFIED CHEQUE etc.",
    )
    booking: "BookingOption" = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#booking",
        description="Refers to the Booking option",
    )
    booking_ref: "Booking" = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#bookingRef",
        description="Refers to the Booking",
    )
    carrier_declaration_date: datetime = Field(
        alias="https://onerecord.iata.org/Waybill#carrierDeclarationDate",
        description="Date upon which the certification is made by the carrier",
    )
    carrier_declaration_place: "Location" = Field(
        alias="https://onerecord.iata.org/Waybill#carrierDeclarationPlace",
        description="Location of individual or company involved in the movement of a consignment or Coded representation of a specific airport/city code",
    )
    carrier_declaration_signature: str = Field(
        alias="https://onerecord.iata.org/Waybill#carrierDeclarationSignature",
        description="Contains the authentication of the Carrier",
    )
    consignor_declaration_signature: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#consignorDeclarationSignature",
        description="Name of consignor signatory",
    )
    contained_waybills: "list[Waybill]" = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#containedWaybills",
        description="Refers to the Waybill(s) contained",
    )
    customs_origin_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#customsOriginCode",
        description="Code indicating the origin of goods for Customs purposes (e.g. For goods in free circulation in the EU) List to be provided by local authorities",
    )
    destination_charges: list[float] = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#destinationCharges",
        description="Charges levied at destination accruing to the last carrier, in destination currency",
    )
    destination_currency_code: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#destinationCurrencyCode",
        description="ISO 3-letter currency code of destination. Refer to ISO 4217",
    )
    destination_currency_rate: float = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#destinationCurrencyRate",
        description="Conversion rate applied",
    )
    optional_shipping_info: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#optionalShippingInfo",
        description="The shipper or its Agent may enter the appropriate optional shipping",
    )
    optional_shipping_ref_no: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#optionalShippingRefNo",
        description="Optional shipping reference number if any",
    )
    origin_currency: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#originCurrency",
        description="ISO alpha 3 Code used to indicate the Origin Currency, refer to ISO 4217 currency codes",
    )
    waybill_number: str = Field(
        alias="https://onerecord.iata.org/Waybill#waybillNumber",
        description="House or Master Waybill unique identifier",
    )
    waybill_prefix: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#waybillPrefix",
        description="Prefix used for the Waybill Number. Refer to IATA Airlines Codes",
    )
    waybill_type: str = Field(
        default=None,
        alias="https://onerecord.iata.org/Waybill#waybillType",
        description="Type of the Waybill: House, Direct or Master",
    )


Address.update_forward_refs()
Booking.update_forward_refs()
BookingOption.update_forward_refs()
BookingOptionRequest.update_forward_refs()
BookingSegment.update_forward_refs()
BookingTimes.update_forward_refs()
Branch.update_forward_refs()
CO2CalcMethod.update_forward_refs()
CO2Emissions.update_forward_refs()
Carrier.update_forward_refs()
CarrierProduct.update_forward_refs()
Characteristics.update_forward_refs()
CommonObjects.update_forward_refs()
Company.update_forward_refs()
CompanyBranch.update_forward_refs()
Contact.update_forward_refs()
ContactOther.update_forward_refs()
Country.update_forward_refs()
CustomsInfo.update_forward_refs()
DgDeclaration.update_forward_refs()
DgProductRadioactive.update_forward_refs()
DgRadioactiveIsotope.update_forward_refs()
Dimensions.update_forward_refs()
EmbeddedObject.update_forward_refs()
EpermitConsignment.update_forward_refs()
EpermitSignature.update_forward_refs()
Event.update_forward_refs()
EventUld.update_forward_refs()
ExternalReference.update_forward_refs()
Geolocation.update_forward_refs()
HandlingInstructions.update_forward_refs()
Insurance.update_forward_refs()
IotDevice.update_forward_refs()
Item.update_forward_refs()
ItemDg.update_forward_refs()
LiveAnimalsEpermit.update_forward_refs()
Location.update_forward_refs()
LogisticsObject.update_forward_refs()
Measurements.update_forward_refs()
MeasurementsGeoloc.update_forward_refs()
MeasurementsOther.update_forward_refs()
MovementTimes.update_forward_refs()
OtherIdentifier.update_forward_refs()
OtherParty.update_forward_refs()
PackagingType.update_forward_refs()
Party.update_forward_refs()
Person.update_forward_refs()
Piece.update_forward_refs()
PieceDg.update_forward_refs()
PieceLiveAnimals.update_forward_refs()
Price.update_forward_refs()
Product.update_forward_refs()
ProductDg.update_forward_refs()
Ranges.update_forward_refs()
Ratings.update_forward_refs()
RegulatedEntity.update_forward_refs()
Request.update_forward_refs()
Routing.update_forward_refs()
Schedule.update_forward_refs()
ScheduledLegs.update_forward_refs()
SecurityDeclaration.update_forward_refs()
Sensor.update_forward_refs()
SensorGeoloc.update_forward_refs()
SensorOther.update_forward_refs()
ServiceRequest.update_forward_refs()
Shipment.update_forward_refs()
SpecialHandling.update_forward_refs()
TransportMeans.update_forward_refs()
TransportMovement.update_forward_refs()
TransportSegment.update_forward_refs()
ULD.update_forward_refs()
Value.update_forward_refs()
VolumetricWeight.update_forward_refs()
Waybill.update_forward_refs()
