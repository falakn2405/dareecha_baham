from enum import Enum

class VehicleType(Enum):
    AUTO_RICKSHAW = "Auto Rickshaw"
    SEDAN = "Sedan"
    HATCHBACK = "Hatch Back"
    SUV = "Sub-Urban Vehicle"
    VAN = "Van"
    HIGH_ROOF = "High Roof"
    MOTORCYCLE = "Motor Cycle / Scooter"

    def __str__(self):
        return super.value

class VehicleStatus(Enum):
    AVAILABLE = "Available"
    FULL = "Full"
    INACTIVE = "Inactive"
    REMOVED = "Removed"