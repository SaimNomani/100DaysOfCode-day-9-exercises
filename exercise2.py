# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
#
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
#
# You've been to Moscow and Saint Petersburg
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


def add_travel_log():
    want_to_add = 'yes'
    while want_to_add == 'yes':
        travel_dict = {}
        country = input("enter country you visited: ")
        cities_visited = (input(f"enter list of cities you visited in {country} (separated by comma): ")).split(',')
        total_visits = int(input(f"enter total visits: "))
        travel_dict["country"] = country
        travel_dict["visits"] = total_visits
        travel_dict["cities"] = cities_visited
        travel_log.append(travel_dict)
        want_to_add = (input('Type "yes" to add another travel log or "no" to go back: ')).lower()
        if want_to_add == 'no':
            print("Thank You!!")
            break


add_travel_log()
print(travel_log)
