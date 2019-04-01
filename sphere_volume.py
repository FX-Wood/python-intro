# Exercise 4:
# Write a program that asks a user for a radius and then calculates the volume of a sphere.

# Sphere volume = 4/3 x Pi x radius x radius x radius

# Print the calculated volume for the user. Be sure to use the Python exponentiation operator.

import math

r = int(input('please input radius for volume computation: \n>> '))

print( f"A sphere with radius {r} has volume {4/3 * 3.14159 * r ** 3} (6 digits of pi)")
print( f"Here is the volume with more precision: { 4/3 * math.pi * r ** 3} (math.pi digits of pi)")