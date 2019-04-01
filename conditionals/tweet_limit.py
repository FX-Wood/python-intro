# Exercise 2:
# Take in a string and print it only if it is less than 140 characters, else return an error and the length of the string entered.

s = input('Input string to check the length of \n>>')

if len(s) < 140:
    print(f"Your string:\n{s}")
else:
    raise Exception("Your string should be less than 140 characters long. Input length was {}")