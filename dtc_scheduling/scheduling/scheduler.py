from scheduling.models import CrewMember, Bus, Shift
from datetime import datetime, timedelta
from typing import List
from tabulate import tabulate

def schedule_crews(crews: List[CrewMember], buses: List[Bus], shifts: List[Shift]):
    """
    Assigns crew members to buses and shifts dynamically, avoiding repeated shift assignments across weeks.
    """
    assignments = []

    # Separate crews by role
    drivers = [crew for crew in crews if crew.role == 'Driver']
    ticket_collectors = [crew for crew in crews if crew.role == 'TicketCollector']

    # Iterate over shifts
    for shift in shifts:
        print(f"\nScheduling for Shift ID: {shift.shift_id} ({shift.shift_type})")

        # Find available drivers and ticket collectors for the shift
        available_drivers = [
            driver for driver in drivers
            if driver.is_available
            and not driver.is_resting
            and (driver.override_shift == shift.shift_type or driver.preferred_shift == shift.shift_type)
            and driver.current_shift is None
            and driver.last_assigned_shift != shift.shift_type
        ]
        available_ticket_collectors = [
            collector for collector in ticket_collectors
            if collector.is_available
            and not collector.is_resting
            and (collector.override_shift == shift.shift_type or collector.preferred_shift == shift.shift_type)
            and collector.current_shift is None
            and collector.last_assigned_shift != shift.shift_type
        ]

        # Find buses available for the shift
        available_buses = [
            bus for bus in buses
            if bus.is_available
            and bus.status == 'Active'
            and (bus.next_available_time is None or bus.next_available_time <= shift.start_time)
        ]

        # Assign one driver and one ticket collector to each bus
        for bus in available_buses:
            if available_drivers and available_ticket_collectors:
                driver = available_drivers.pop(0)
                collector = available_ticket_collectors.pop(0)

                # Assign the driver and ticket collector
                shift.assigned_crew_id = driver.crew_id
                bus.assigned_crew_id = driver.crew_id
                driver.current_shift = shift.shift_id
                collector.current_shift = shift.shift_id
                bus.next_available_time = shift.end_time  # Update bus availability

                # Update last assigned shift
                driver.last_assigned_shift = shift.shift_type
                collector.last_assigned_shift = shift.shift_type

                # Record the assignment
                assignments.append({
                    'Shift ID': shift.shift_id,
                    'Shift Type': shift.shift_type,
                    'Bus ID': bus.bus_id,
                    'Driver': driver.name,
                    'Ticket Collector': collector.name,
                })

    # Print the final assignments in a table format
    print("\nFinal Assignments:")
    print(tabulate(assignments, headers="keys", tablefmt="grid"))

    return assignments


def modify_crew_shift(crew: CrewMember, new_shift_type: str, shifts: List[Shift], assignments: List[dict]):
    """
    Modify the shift assignment for a specific crew member.
    Ensures no collisions occur after the shift change.
    """
    from tabulate import tabulate

    # Find the current assignment for the crew
    current_assignment = next((a for a in assignments if a['Driver'] == crew.name or a['Ticket Collector'] == crew.name), None)
    if current_assignment:
        print(f"Removing crew {crew.name} from Shift ID: {current_assignment['Shift ID']}")
        assignments.remove(current_assignment)

    # Check for shift collision
    existing_shift = next((s for s in shifts if s.shift_type == new_shift_type and s.assigned_crew_id == crew.crew_id), None)
    if existing_shift:
        print(f"Shift collision detected for Crew {crew.name} on {new_shift_type}. Cannot reassign.")
        return False

    # Assign the crew to the new shift
    for shift in shifts:
        if shift.shift_type == new_shift_type and shift.assigned_crew_id is None:
            shift.assigned_crew_id = crew.crew_id
            crew.current_shift = shift.shift_id
            crew.last_assigned_shift = new_shift_type
            assignments.append({
                'Shift ID': shift.shift_id,
                'Shift Type': new_shift_type,
                'Bus ID': None,  # Bus can be assigned dynamically later
                'Driver': crew.name if crew.role == 'Driver' else None,
                'Ticket Collector': crew.name if crew.role == 'TicketCollector' else None,
            })
            print("\nUpdated Assignments:")
            print(tabulate(assignments, headers="keys", tablefmt="grid"))
            return True

    print(f"No available slots for {new_shift_type} shift for Crew {crew.name}.")
    return False