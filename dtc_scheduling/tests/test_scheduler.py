import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from tabulate import tabulate
from scheduling.models import CrewMember, Bus, Shift
from scheduling.scheduler import schedule_crews, modify_crew_shift
from datetime import datetime, timedelta

class TestScheduler(unittest.TestCase):
    def test_schedule_crews(self):
        print("\nCreating sample data...")
        
        # Create sample crews
        crews = [
            CrewMember(crew_id=i, name=f"Driver-{i}", role="Driver", preferred_shift="Morning") for i in range(1, 11)
        ] + [
            CrewMember(crew_id=i, name=f"Driver-{i}", role="Driver", preferred_shift="Afternoon") for i in range(11, 21)
        ] + [
            CrewMember(crew_id=i, name=f"Driver-{i}", role="Driver", preferred_shift="Evening") for i in range(21, 26)
        ] + [
            CrewMember(crew_id=i, name=f"Collector-{i-25}", role="TicketCollector", preferred_shift="Morning") for i in range(26, 36)
        ] + [
            CrewMember(crew_id=i, name=f"Collector-{i-25}", role="TicketCollector", preferred_shift="Afternoon") for i in range(36, 46)
        ] + [
            CrewMember(crew_id=i, name=f"Collector-{i-25}", role="TicketCollector", preferred_shift="Evening") for i in range(46, 51)
        ]

        # Create sample buses
        buses = [
            Bus(bus_id=i, capacity=50) for i in range(1, 11)
        ]

        # Create sample shifts
        now = datetime.now()
        shifts = [
            Shift(shift_id=1, shift_type="Morning", start_time=now, end_time=now + timedelta(hours=8)),
            Shift(shift_id=2, shift_type="Afternoon", start_time=now + timedelta(hours=8), end_time=now + timedelta(hours=16)),
            Shift(shift_id=3, shift_type="Evening", start_time=now + timedelta(hours=16), end_time=now + timedelta(hours=24)),
        ]

        # Run the scheduler
        print("\nRunning scheduler...")
        assignments = schedule_crews(crews, buses, shifts)

        # Display the final assignments in a table
        print("\nFinal Assignments:")
        print(tabulate(assignments, headers="keys", tablefmt="grid"))

        # Modify a crew's shift
        print("\nRequesting shift change for Driver-1 to Afternoon...")
        modify_crew_shift(crews[0], "Afternoon", shifts, assignments)

        # Display the updated assignments
        print("\nUpdated Assignments:")
        print(tabulate(assignments, headers="keys", tablefmt="grid"))


if __name__ == '__main__':
    unittest.main()