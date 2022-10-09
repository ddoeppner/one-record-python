import pytest

from onerecord.exceptions import ONERecordClientException


def test_one_record_client_exception():
    with pytest.raises(ONERecordClientException):
        raise ONERecordClientException(
            message="Et haett noch immer jot jejange",
            code=4711,
        )
    with pytest.raises(ONERecordClientException):
        raise ONERecordClientException(
            message=str.encode("Et haett noch immer jot jejange")
        )
