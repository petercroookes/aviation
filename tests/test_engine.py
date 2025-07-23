import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_year",
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"required_global_fleet": 25_000.0 * aircraft},
            "required_global_fleet",
            25_000.0 * aircraft,
        ),
        (
            {
                "passengers_per_year": 9_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            24_640_657.0 * passenger / day,
        ),
        (
            {
                "passengers_per_year": 9_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 181.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 4.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            34_000.0 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: float,
) -> None:
    result = systems_model.evaluate(inputs, output)
    assert result == pytest_camia.approx(expected, rtol=0.1)
