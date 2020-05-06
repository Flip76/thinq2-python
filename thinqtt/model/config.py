from marshmallow_dataclass import dataclass

from thinqtt.model.auth import ThinQSession
from thinqtt.model.common import Route
from thinqtt.model.thinq import IOTRegistration


@dataclass
class MQTTConfiguration:
    route: Route
    registration: IOTRegistration
    ca_cert: str
    private_key: str
    csr: str


@dataclass
class ThinQConfiguration:
    auth: ThinQSession
    mqtt: MQTTConfiguration
