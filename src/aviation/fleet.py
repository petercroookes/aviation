"""Modelling of the global fleet using average passenger flight data."""

__all__ = ("passengers_per_day", "required_global_fleet")

import typing

import camia_model as model
from camia_model.units import Quantity, day, year

from aviation.units import aircraft, journey, passenger


@model.transform
def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    days_per_year: typing.Annotated[Quantity, day / year],
) -> typing.Annotated[Quantity, passenger / day]:
    """Calculates the number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers that fly globally.
        days_per_year: The number of days in a year.

    """
    return passengers_per_year / days_per_year


@model.transform
def required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / aircraft],
    flights_per_aircraft_per_day: typing.Annotated[Quantity, journey / (aircraft * day)],
) -> typing.Annotated[Quantity, aircraft]:
    """Calculate the size of the required global fleet.

    Args:
        passengers_per_day: The average number of passengers that fly daily.
        seats_per_aircraft: The average number of seats per aircraft.
        flights_per_aircraft_per_day: The average number of flight per aircraft per day.

    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (
        seats_per_aircraft * flights_per_aircraft_per_day * aircraft_per_journey
    )
