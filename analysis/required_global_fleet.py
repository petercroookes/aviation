"""Analysis to determine the global fleet requirement based on average passenger and flight data."""

import camia_engine as engine

import aviation

passengers_per_year = 9_000_000_000.0
days_per_year = 365.25
seats_per_aircraft = 181.0
flights_per_aircraft_per_day = 4.0

inputs = {
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
    "seats_per_aircraft": seats_per_aircraft,
    "flights_per_aircraft_per_day": flights_per_aircraft_per_day,
}
output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)
required_global_fleet = systems_model.evaluate(inputs, output)
print(f"Global Fleet Requirement = {required_global_fleet:.0f} Aircraft")
