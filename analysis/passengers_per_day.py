import aviation

passengers_per_year = 9_000_000_000.0
days_per_yer = 365.25
seats_per_aircraft = 181.0
flights_per_aircraft_per_day = 4.0

passengers_per_day = aviation.calculate_passengers_per_day(
    passengers_per_year=passengers_per_year, days_per_yer=days_per_yer
)

print(f"Passengers Per Day = {passengers_per_day:.0f}")
