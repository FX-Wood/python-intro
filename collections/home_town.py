# Exercise 3
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    "city": "Seattle",
    "state": "Washington",
    "population": "724,000"
}

print(f"I was born in {home_town['city']}, {home_town['state']} (population {home_town['population']})")