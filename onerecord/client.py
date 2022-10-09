import functools
from typing import Optional

import requests

from onerecord.enums import LogisticsObjectType
from onerecord.exceptions import ONERecordClientException
from onerecord.models.api import Notification
from onerecord.models.cargo import Event, LogisticsObject
from onerecord.utils import (
    json_to_events,
    json_to_logistics_object,
    json_to_logistics_objects,
)


class ONERecordClient:
    """
    ONERecordClient object to interact with an ONE Record API.
    The object holds information necessary to
    connect to an ONE Record API. Requests can be made to the ONE Record API
    directly through the client.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8080,
        company_identifier: str = None,
        ssl: bool = False,
        verify_ssl: bool = True,
        timeout=None,
        proxies=None,
        cert=None,
        session=None,
        headers=None,
    ):
        """Construct a new ONERecordClient object."""
        self._host = host
        self._port = int(port)
        if not company_identifier:
            raise ValueError(
                "company_identifer is required parameter but missing"
            )
        else:
            self._path = f"/companies/{company_identifier}"

        if not session:
            session = requests.Session()

        self._session = session

        self._verify_ssl = verify_ssl
        if self._verify_ssl:
            self._session

        self._scheme = "http"

        if ssl is True:
            self._scheme = "https"

        if proxies is None:
            self._proxies = {}
        else:
            self._proxies = proxies

        if self._session.proxies is None:
            self._session.proxies = self._proxies
        else:
            self._session.proxies.update(self._proxies)

        if cert:
            if not ssl:
                raise ValueError(
                    "Client certificate provided but ssl is disabled."
                )
            else:
                self._session.cert = cert

        self._baseurl = "{}://{}:{}{}".format(
            self._scheme, self._host, self._port, self._path
        )

        if headers is None:
            headers = {}
        headers.setdefault("Content-Type", "application/ld+json")
        headers.setdefault("Accept", "application/ld+json")
        self._headers = headers

        self._session.headers = self._headers

        self._timeout = timeout
        if self._timeout:
            self._session.request = functools.partial(
                self._session.request, timeout=self._timeout
            )

    def create_logistics_object(
        self, logistics_object: LogisticsObject
    ) -> LogisticsObject:
        """Creates a logistics object on a ONE Record server"""
        url = f"{self._baseurl}/los"
        response = requests.request(
            "POST",
            url,
            headers=self._headers,
            data=logistics_object.json(exclude_none=True, by_alias=True),
        )
        if response.status_code == 201 and "location" in response.headers:
            logistics_object.id = response.headers["location"]
            return logistics_object
        else:
            raise ONERecordClientException(
                message="Could not create LogisticsObject",
                code=response.status_code,
            )

    def get_logistics_objects(
        self, logistics_object_type: LogisticsObjectType = None
    ) -> list[LogisticsObject]:
        """Returns a list of logistics objects from a ONE Record API"""
        url = f"{self._baseurl}/los"
        if logistics_object_type:
            url = f"{url}?type={logistics_object_type.value}"
        response = self._session.get(url)
        if response.status_code == 200:
            return json_to_logistics_objects(
                logistics_objects_json=response.text
            )
        else:
            raise ONERecordClientException(
                message="Could not get LogisticsObject",
                code=response.status_code,
            )

    def get_logistics_object_by_uri(
        self, uri: str
    ) -> Optional[LogisticsObject]:
        """Returns a logistics object by URI"""
        response = self._session.get(uri)
        if response.status_code == 200:
            return json_to_logistics_object(
                logistics_object_json=response.text
            )

        elif response.status_code == 404:
            raise ONERecordClientException(
                message="LogisticsObject does not exist",
                code=response.status_code,
            )
        else:
            raise ONERecordClientException(
                message="Could not get LogisticsObject",
                code=response.status_code,
            )

    def create_event(
        self, logistics_object_uri: str, event: Event
    ) -> Optional[bool]:
        """Creates Events object for particular LogisticsObject"""
        url = f"{logistics_object_uri}/events"
        response = self._session.post(
            url=url, data=event.json(exclude_none=True, by_alias=True)
        )

        if response.status_code == 201:
            return True
        else:
            raise ONERecordClientException(
                message=f'Could not create Event for LogisticsObject[@id="{logistics_object_uri}"]',
                code=response.status_code,
            )

    def get_event_by_uri(self, event_uri: str):
        # TODO: not specified in ONE Record API spec yet
        pass

    def get_events_by_logistics_objects_uri(
        self, logistics_object_uri: str
    ) -> list[Event]:
        url = f"{logistics_object_uri}/events"
        response = self._session.get(url=url)

        if response.status_code == 200:
            return json_to_events(events_json=response.text)
        else:
            raise ONERecordClientException(
                message=f'Could not get Events for LogisticsObject[@id="{logistics_object_uri}"]',
                code=response.status_code,
            )

    def send_notification(
        self, callback_url: str, notification: Notification
    ) -> Optional[bool]:
        response = self._session.post(
            url=callback_url,
            data=notification.json(exclude_none=True, by_alias=True),
        )
        if response.status_code == 200:
            return True
        else:
            raise ONERecordClientException(
                message=f"Could not send Notifcation to {callback_url}",
                code=response.status_code,
            )
