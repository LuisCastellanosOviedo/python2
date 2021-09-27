travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country, visits, cities_list):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities_list
    })


add_new_country("Russia", 2, ["Moscow"])
print(travel_log)
