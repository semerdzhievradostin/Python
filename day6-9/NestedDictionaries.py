travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country():
    add_dict = {
        "country": "Russia",
        "visits": 2,
        "cities": ["Moscow", "Saint Petersburg"]
    }
    travel_log.append(add_dict)


#🚨 Do not change the code below
add_new_country()
print(travel_log)
