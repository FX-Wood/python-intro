# Exercise 4
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

home_town = {
    "city": "Seattle",
    "state": "Washington",
    "population": 724000
}

for key,val in home_town.items():
    print(f"{key} = {val}")