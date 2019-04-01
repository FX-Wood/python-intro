# Exercise 1:
# Write a script that asks for a number and prints whether it is even or odd.

raw = input('Input an integer to check for evenness: \n >> ')

message = raw

if raw.isdigit():
    n = int(raw)
    if n % 2 == 0:
        message += " is even"
    if n % 2 != 0:
        message += " is odd"
    print(message)
else:
    print("not an integer")
