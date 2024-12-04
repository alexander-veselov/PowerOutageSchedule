import requests
from typing import Optional
from pydantic import BaseModel


class Current(BaseModel):
    note: str
    hasQueue: str
    subqueue: int
    queue: int


class Hour(BaseModel):
    hour: str
    electricity: int
    description: str
    periodLimitValue: int


# Note: This is not the graph from math "graph theory"
# It's just a bad name used by this API developers
class Graph(BaseModel):
    scheduleApprovedSince: str
    eventDate: str
    hoursList: list[Hour]


class Graphs(BaseModel):
    yesterday: Optional[Graph]
    today: Optional[Graph]
    tomorrow: Optional[Graph]


class PowerOutageResponse(BaseModel):
    current: Current
    graphs: Graphs
    showFutureDateUntil: str


def request_power_outage_data(address: str) -> PowerOutageResponse:
    url = 'https://svitlo.oe.if.ua/GAVTurnOff/GavGroupByAccountNumber'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    payload = {'accountNumber': '', 'userSearchChoice': 'pob', 'address': address}
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        return PowerOutageResponse.parse_raw(response.text)
    else:
        raise NotImplementedError(f'Not supported status code: {response.status_code}')