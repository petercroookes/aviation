"""Analysis to determine the average number of passengers flying daily."""

import aviation

passengers_per_year = 9_000_000_000.0
days_per_year = 365.25

passengers_per_day = aviation.passengers_per_day(
    passengers_per_year=passengers_per_year, days_per_year=days_per_year
)

print(f"Passengers Per Day = {passengers_per_day:.0f}")
