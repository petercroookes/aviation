def calculate_passengers_per_day(passengers_per_year, days_per_yer):
    return passengers_per_year / days_per_yer

def calculate_required_global_fleet(passengers_per_day, seats_per_aircraft, flights_per_aircraft_per_day):
    return passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)    