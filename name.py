# Exercise 2:
# Write a script that asks a user for their name and age. Print out a string for the user:

# Hello NAME! You are AGE years old.
# Solve it using string concatentation
# Solve it with f-strings

name = input('Please input your name \n> ')
age = input('Please input your age \n> ')

print('Hello ' + name + '! You are ' + age + ' years old' )
print(f"Hello {name}! You are {age} years old.")