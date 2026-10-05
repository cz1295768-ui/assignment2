from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

@dataclass
class Appointment:
    appID: int
    dateTime: datetime
    _status: AppointmentStatus

    @property
    def status(self)-> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        if self.status != AppointmentStatus.SCHEDULED:
           raise ValueError(
               f"Illegal state transition: cannot cancel appointment with status{self.status.name}"
            )
        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        if self.status != AppointmentStatus.SCHEDULED:
            raise ValueError(
                f"Illegal state transition: cannot complete appointment with status {self.status.name}"
            )
        self._status = AppointmentStatus.COMPLETED

    def __post_init__(self):
        if self.appID <= 0:
            raise ValueError("appID must be a positive integer")