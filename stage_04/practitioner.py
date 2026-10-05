from dataclasses import dataclass
from datetime import datetime

@dataclass
class Practitioner:
    identifier: str
    name: str
    specialty: str

    def __post_init__(self):
        if not self.identifier.strip():
            raise ValueError("Practitioner identifier cannot be empty")
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        if not self.specialty.strip():
            raise ValueError("Specialty cannot be empty")