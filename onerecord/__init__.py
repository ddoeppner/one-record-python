import logging

from onerecord.client import ONERecordClient

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s.%(funcName)s:%(lineno)d -  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

__all__ = [
    "ONERecordClient",
]

__version__ = "0.1.0"
