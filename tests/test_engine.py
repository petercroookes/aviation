import typing

import pytest

import aviation
from aviation import _engine as engine


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 5_000_000_000.0}, "passengers_per_year", 5_000_000_000.0),
        ({"required_global_fleet": 25_000.0}, "required_global_fleet", 25_000.0),
        (
            {"passengers_per_year": 9_000_000_000.0, "days_per_year": 365.25},
            "passengers_per_day",
            24_640_657.0,
        ),
        (
            {
                "days_per_year": 365.25,
                "passengers_per_year": 9_000_000_000.0,
                "seats_per_aircraft": 181.0,
                "flights_per_aircraft_per_day": 4.0,
            },
            "required_global_fleet",
            34_000.0,
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
    assert result == pytest.approx(expected, rel=0.1)
