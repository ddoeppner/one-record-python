import enum


class LogisticsObjectType(enum.Enum):
    BOOKING = "https://onerecord.iata.org/Booking"
    BOOKINGOPTION = "https://onerecord.iata.org/BookingOption"
    BOOKINGOPTIONREQUEST = "https://onerecord.iata.org/BookingOptionRequest"
    BOOKINGTIMES = "https://onerecord.iata.org/BookingTimes"
    CO2CALCMETHOD = "https://onerecord.iata.org/CO2CalcMethod"
    CO2EMISSIONS = "https://onerecord.iata.org/CO2Emissions"
    CARRIERPRODUCT = "https://onerecord.iata.org/CarrierProduct"
    CHARACTERISTICS = "https://onerecord.iata.org/Characteristics"
    CUSTOMSINFO = "https://onerecord.iata.org/CustomsInfo"
    DGDECLARATION = "https://onerecord.iata.org/DgDeclaration"
    DGPRODUCTRADIOACTIVE = "https://onerecord.iata.org/DgProductRadioactive"
    DGRADIOACTIVEISOTOPE = "https://onerecord.iata.org/DgRadioactiveIsotope"
    EPERMITCONSIGNMENT = "https://onerecord.iata.org/EpermitConsignment"
    EPERMITSIGNATURE = "https://onerecord.iata.org/EpermitSignature"
    INSURANCE = "https://onerecord.iata.org/Insurance"
    IOTDEVICE = "https://onerecord.iata.org/IotDevice"
    ITEM = "https://onerecord.iata.org/Item"
    ITEMDG = "https://onerecord.iata.org/ItemDg"
    LIVEANIMALSEPERMIT = "https://onerecord.iata.org/LiveAnimalsEpermit"
    PACKAGINGTYPE = "https://onerecord.iata.org/PackagingType"
    PIECE = "https://onerecord.iata.org/Piece"
    PIECEDG = "https://onerecord.iata.org/PieceDg"
    PIECELIVEANIMALS = "https://onerecord.iata.org/PieceLiveAnimals"
    PRICE = "https://onerecord.iata.org/Price"
    PRODUCT = "https://onerecord.iata.org/Product"
    PRODUCTDG = "https://onerecord.iata.org/ProductDg"
    RANGES = "https://onerecord.iata.org/Ranges"
    RATINGS = "https://onerecord.iata.org/Ratings"
    REQUEST = "https://onerecord.iata.org/Request"
    ROUTING = "https://onerecord.iata.org/Routing"
    SCHEDULE = "https://onerecord.iata.org/Schedule"
    SECURITYDECLARATION = "https://onerecord.iata.org/SecurityDeclaration"
    SENSOR = "https://onerecord.iata.org/Sensor"
    SENSORGEOLOC = "https://onerecord.iata.org/SensorGeoloc"
    SENSOROTHER = "https://onerecord.iata.org/SensorOther"
    SERVICEREQUEST = "https://onerecord.iata.org/ServiceRequest"
    SHIPMENT = "https://onerecord.iata.org/Shipment"
    SPECIALHANDLING = "https://onerecord.iata.org/SpecialHandling"
    TRANSPORTMEANS = "https://onerecord.iata.org/TransportMeans"
    TRANSPORTMOVEMENT = "https://onerecord.iata.org/TransportMovement"
    TRANSPORTSEGMENT = "https://onerecord.iata.org/TransportSegment"
    ULD = "https://onerecord.iata.org/ULD"
    WAYBILL = "https://onerecord.iata.org/Waybill"


class NotificationEventType(enum.Enum):
    OBJECT_CREATED = "OBJECT_CREATED"
    OBJECT_UPDATED = "OBJECT_UPDATED"


class ChangeRequestStatus(enum.Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


class BookingStatus(enum.Enum):
    BOOKED = "Booked"
    QUOTED = "Quoted"


class ShipmentSecurityStatus(enum.Enum):
    NOT_SCREENED = "NCR"
    SCREENED = "SCR"


class RequestType(enum.Enum):
    BOOKING = "Booking"
    QUOTE = "Quote"


class EventTypeIndicator(enum.Enum):
    ACTUAL = "Actual"
    EXPECTED = "Expected"
    PLANNED = "Planned"
    REQUESTED = "Requested"


class TransactionPurposeCode(enum.Enum):
    B = "B"
    E = "E"
    G = "G"
    H = "H"
    L = "L"
    M = "M"
    N = "N"
    P = "P"
    Q = "Q"
    S = "S"
    T = "T"
    Z = "Z"


class Direction(enum.Enum):
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class TimeType(enum.Enum):
    ACTUAL = "Actual"
    DEPARTED = "Departed"
    SCHEDULED = "Scheduled"


class PartyRole(enum.Enum):
    AGENT = "Agent"
    AIRLINE = "Airline"
    AIRPORT_AUTHORITY = "Airport Authority"
    BROKER = "Broker"
    COMMISSIONABLE_AGENT = "Commissionable Agent"
    CONSIGNEE = "Consignee"
    CUSTOMS = "Customs"
    DECLARANT = "Declarant"
    DECONSOLIDATOR = "Deconsolidator"
    FREIGHT_FORWARDER = "Freight Forwarder"
    GROUND_HANDLING_AGENT = "Ground Handling Agent"
    NOMINATED_FREIGHT_COMPANY = "Nominated freight company"
    NOTIFY_PARTY = "Notify Party"
    OTHER_PARTICIPANT_IDENTIFIER = "Other Participant Identifier"
    POST_OFFICE = "Post Office"
    SHIPPER = "Shipper"
    TRUCKER = "Trucker"


class PersonContactType(enum.Enum):
    CUSTOMER_CONTACT = "Customer contact"
    CUSTOMS_CONTACT = "Customs contact"
    EMERGENCY_CONTACT = "Emergency contact"
    OTHER = "Other"


class ContactContactType(enum.Enum):
    ALTERNATE_EMAIL_ADDRESS = "Alternate email address"
    ALTERNATE_PHONE_NUMBER = "Alternate phone number"
    EMAIL_ADDRESS = "Email address"
    FAX_NUMBER = "Fax number"
    OTHER = "Other"
    PHONE_NUMBER = "Phone number"
    TELEX = "Telex"
    WEBSITE = "Website"


class Salutation(enum.Enum):
    DR = "Dr."
    MR = "Mr."
    MS = "Ms."
    PR = "Pr."


class LoadType(enum.Enum):
    BULK = "Bulk"
    PALLET = "Pallet"
    ULD = "ULD"


class PackageMarkCoded(enum.Enum):
    OTHER = "Other"
    SSCC18 = "SSCC-18"
    UPC = "UPC"


class GoodsTypeCode(enum.Enum):
    TYPE_I = "I"
    TYPE_II = "II"
    TYPE_III = "III"


class GoodsTypeExtensionCode(enum.Enum):
    A = "A"
    C = "C"
    D = "D"
    F = "F"
    I = "I"  # noqa: E741
    O = "O"  # noqa: E741
    R = "R"
    U = "U"
    W = "W"


class ChargePaymentType(enum.Enum):
    COLLECT = "C"
    PREPAID = "P"


class OtherChargesIndicator(enum.Enum):
    PREPAID = "P"
    COLLECT = "C"


class Entitlement(enum.Enum):
    CARRIER = "C"
    AGENT = "A"


class RegulatedEntityCategory(enum.Enum):
    AIRCRAFT_OPERATOR = "AO - Aircraft Operator"
    KNOWN_COSIGNOR = "KC - Known Consignor"
    REGULATED_AGENT = "RA - Regulated Agent"
    REGULATED_CARRIER = "RC - Regulated Carrier"


class GroundsForExemption(enum.Enum):
    BIOMEDICAL_SAMPLES = "BIOM"
    DIPLOMATIC_BAGS = "DIPL"
    LIFESAVING_MATERIALS = "LFSM"
    SMALL_UNDERSIZED_SHIPMENTS = "SMUS"
    TRANSFER_TRANSSHIPMENT = "TRNS"


class ScreeningMethod(enum.Enum):
    ANY_OTHER_MEANS = "AOM"
    CARGO_METAL_DETECTION = "CMD"
    EXPLOSIVE_DETECTION_SYSTEM = "EDS"
    EXPLOSIVE_DETECTION_DOGS = "EDD"
    EXPLOSIVE_TRACE_DETECTION = "ETD"
    PHYSICAL_INSPECTION_HAND_SEARCH = "PHS"
    VISUAL_CHECK = "VCK"
    XRAY = "XRY"


class SecurityStatus(enum.Enum):
    NSC = "NSC"
    SCO = "SCO"
    SHR = "SHR"
    SPX = "SPX"


class SensorType(enum.Enum):
    ACCELEROMETER = "Accelerometer"
    GEOLOCATION = "Geolocation"
    HUMIDITY = "Humidity"
    LIGHT = "Light"
    PRESSURE = "Pressure"
    THERMOMETER = "Thermometer"
    TILT = "Tilt"
    VIBRATION = "Vibration"


class WeightValuationIndicator(enum.Enum):
    COLLECT = "C"
    PREPAID = "P"


class ModeCode(enum.Enum):
    NOT_SPECIFIED = "0"
    MARITIME = "1"
    RAIL = "2"
    ROAD = "3"
    AIR = "4"
    MAIL = "5"
    MULTIMODAL = "6"
    FIXED = "7"
    INLAND_WATER = "8"
    NOT_APPLICABLE = "9"


class ModeQualifier(enum.Enum):
    MAIN_CARRIAGE = "Main-Carriage"
    ON_CARRIAGE = "On-Carriage"
    PRE_CARRIAGE = "Pre-Carriage"


class ServiceabilityCode(enum.Enum):
    DAMAGED = "DAM"
    SERVICEABLE = "SER"


class WaybillType(enum.Enum):
    DIRECT = "Direct"
    HOUSE = "House"
    MASTER = "Master"


class DgRaTypeCode(enum.Enum):
    I_WHITE = "I=-White"
    II_YELLOW = "II-Yellow"
    III_YELLOW = "III-Yellow"


class PhysicalChemicalForm(enum.Enum):
    LOW_DISPERSIBLE = "LowDispersible"
    PHYSICAL_CHEMICAL_FORM = "PhysicalChemicalForm"
    SPECIAL_FORM = "SpecialForm"


class SignatoryRole(enum.Enum):
    APPLICANT = "Applicant"
    EXAMINING_AUTHORITY = "Examining Authority"
    ISSUING_AUTHORITY = "Issuing Authority"
    MANAGEMENT_AUTHORITY = "Management Authority"
    PERMIT_ISSUER = "Permit issuer"


class SignatureTypeCode(enum.Enum):
    DETENTION = "Detention"
    FUMIGATION = "Fumigaton"
    INSPECTION = "Inspection"
    SECURITY = "Security"


class ServiceType(enum.Enum):
    SPECIAL_SERVICE_REQUEST = "SSR"
    SPECIAL_HANDLING_CODE = "SPH"
    OTHER_SERVICE_INFORMATION = "OSI"


class RatingsType(enum.Enum):
    FACE = "F"
    PUBLISHED = "P"
    ACTUAL = "A"
