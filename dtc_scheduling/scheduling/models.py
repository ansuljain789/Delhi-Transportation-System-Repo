# scheduling/models.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

@dataclass
class CrewMember:
    crew_id: int
    name: str
    role: str  # 'Driver' or 'TicketCollector'
    preferred_shift: Optional[str] = None
    weekly_shift_sequence: List[str] = field(default_factory=lambda: ['Morning', 'Afternoon', 'Evening'])
    current_shift: Optional[int] = None
    is_resting: bool = False
    is_available: bool = True
    override_shift: Optional[str] = None  # Temporary shift override for the day or week
    last_rest_time: Optional[datetime] = None
    last_assigned_shift: Optional[str] = None


@dataclass
class Bus:
    bus_id: int
    capacity: int
    status: str = 'Active'  # 'Active' or 'Maintenance'
    is_available: bool = True  # Marks temporary availability for the day
    assigned_crew_id: Optional[int] = None
    next_available_time: Optional[datetime] = None

@dataclass
class Shift:
    shift_id: int
    shift_type: str  # 'Morning', 'Afternoon', 'Evening'
    start_time: datetime
    end_time: datetime
    assigned_crew_id: Optional[int] = None