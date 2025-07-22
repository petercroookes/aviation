"""A simple model of global aviation.

Modules:
    fleet: Modelling of the global fleet based on average passenger and aircraft data.

"""

__all__ = ("calculate_required_global_fleet", "calculate_passengers_per_day")

from aviation.fleet import (
    calculate_passengers_per_day,
    calculate_required_global_fleet,
)
