from dataclasses import dataclass

@dataclass
class CreateVnfRequest:
    vnfdId: str = None
    vnfInstanceName: str = None
    vnfInstanceDescription: str = None
    metadata: dict = None
