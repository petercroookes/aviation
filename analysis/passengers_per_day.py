"""Analysis to determine the average number of passengers flying daily."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import passenger

passengers_per_year = 9_000_000_000.0 * passenger / year
days_per_year = 365.25 * day / year

inputs = {"days_per_year": days_per_year, "passengers_per_year": passengers_per_year}
output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)

print(f"Passengers Per Day = {passengers_per_day.value}")
