"""Analysis to determine the global fleet requirement based on average passenger and flight data."""

import aviation

passengers_per_year = 9_000_000_000.0
days_per_yer = 365.25
seats_per_aircraft = 181.0
flights_per_aircraft_per_day = 4.0

passengers_per_day = aviation.calculate_passengers_per_day(
    passengers_per_year=passengers_per_year, days_per_yer=days_per_yer
)
required_global_fleet = aviation.calculate_required_global_fleet(
    passengers_per_day=passengers_per_day,
    seats_per_aircraft=seats_per_aircraft,
    flights_per_aircraft_per_day=flights_per_aircraft_per_day,
)

print(f"Global Fleet Requirement = {required_global_fleet:.0f} Aircraft")
