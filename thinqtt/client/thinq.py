from uplink import Field, Path, Query
from uplink import get, post, delete, json

from thinqtt.client.base import BaseClient
from thinqtt.model.thinq import (
    DeviceCollection,
    DeviceDescriptor,
    ThinQResult,
    ThinQResultSuccess,
    IOTRegistration,
    ModelJsonDescriptor,
)


class ThinQClient(BaseClient):
    """LG ThinQ API client"""

    @get("service/application/dashboard")
    def get_devices(self) -> ThinQResult(DeviceCollection):
        """Retrieves collection of user's registered devices"""

    @get("service/devices/{device_id}")
    def get_device(self, device_id: Path) -> ThinQResult(DeviceDescriptor):
        """Retrieves collection of user's registered devices"""

    @get("service/application/modeljson")
    def get_model_json_descriptor(
        self, device_id: Query("deviceId"), model_name: Query("modelName")
    ) -> ThinQResult(ModelJsonDescriptor):
        """Retrieves ModelJson descriptor for a device"""

    @get("service/users/client")
    def get_registered(self) -> ThinQResultSuccess():
        """Get client registration status"""

    @post("service/users/client")
    def register(self) -> ThinQResultSuccess():
        """Register client ID"""

    @delete("service/users/client")
    def deregister(self) -> ThinQResultSuccess():
        """Deregister client ID"""

    @json
    @post("service/users/client/certificate")
    def register_iot(self, csr: Field) -> ThinQResult(IOTRegistration):
        """Deregister client ID"""
