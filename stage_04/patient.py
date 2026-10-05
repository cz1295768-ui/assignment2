from dataclasses import dataclass
from datetime import datetime

@dataclass
class Patient:
    patient_id: str
    name: str
    contract: str
    def __post_init__(self):
        if not self.patient_id.strip():
            raise ValueError("Patient id cannot be empty")
        if not self.name.strip():
            raise  ValueError("Patient name cannot be empty")