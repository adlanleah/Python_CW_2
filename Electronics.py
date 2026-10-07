from datetime import datetime, timezone
import uuid


class Devices:
    def __init__(self, devicetype: str, fault: str, owner_email: str = ""):
        self.id = str(uuid.uuid4())
        self.type = devicetype
        self.fault = fault
        self.owner = owner_email
        self.brought_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    def to_dict(self) -> dict:
        return dict(self.__dict__)

    def __str__(self) -> str:
        return f"{self.type} ({self.fault}) at {self.brought_at}"
