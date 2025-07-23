"""Analysis to determine the average number of passengers flying daily."""

import camia_engine as engine

import aviation

passengers_per_year = 9_000_000_000.0
days_per_year = 365.25

inputs = {"days_per_year": days_per_year, "passengers_per_year": passengers_per_year}
output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)

print(f"Passengers Per Day = {passengers_per_day:.0f}")
