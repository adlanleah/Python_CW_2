import uuid


class users:
    def __init__(self, name: str, email: str, phone: str, device=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.device = device

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }
        if self.device is not None:
            data["device"] = self.device.to_dict() if hasattr(self.device, "to_dict") else self.device
        return data

    def __str__(self) -> str:
        return f"{self.name} | {self.email} | {self.phone} | {self.id}"
