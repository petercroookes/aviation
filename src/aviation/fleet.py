"""Modelling of the global fleet using average passenger flight data."""

__all__ = ("calculate_passengers_per_day", "calculate_required_global_fleet")

from aviation._model import transform


@transform
def calculate_passengers_per_day(passengers_per_year: float, days_per_year: float) -> float:
    """Calculates the number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers that fly globally.
        days_per_year: The number of days in a year.

    """
    return passengers_per_year / days_per_year


@transform
def calculate_required_global_fleet(
    passengers_per_day: float, seats_per_aircraft: float, flights_per_aircraft_per_day: float
) -> float:
    """Calculate the size of the required global fleet.

    Args:
        passengers_per_day: The average number of passengers that fly daily.
        seats_per_aircraft: The average number of seats per aircraft.
        flights_per_aircraft_per_day: The average number of flight per aircraft per day.

    """
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)
