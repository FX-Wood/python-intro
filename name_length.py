# Exercise 3:
# Write a script that asks for a name and prints out, "Your name is X characters in length." 
# Replace X with the length of the name without the spaces!!!

name = input('Please enter your name: \n  > ')

print(f"Your name is {len(name.replace(' ', ''))} characters in length")