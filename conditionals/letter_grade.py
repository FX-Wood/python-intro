# Exercise 3:
# Ask for a numeric grade score. Print the letter grade that the number corresponds to. You can make up the grading scale or use the traditional. Remember, Python has no switch construct.

raw = input('Input numeric grade for conversion to letter grade: \n>> ')
n = 0
try:
    n = float(raw)
    if n < 0: raise Exception('input must be greater than 0')
except ValueError:
    print("Error: input must be numeric")
except Exception as msg:
    print(f"Error: {msg}")

else:

    g = ''

    if n > 90:
        g = 'A'

    elif n > 80:
        g = 'B'

    elif n > 70:
        g = 'C'

    elif n > 60:
        g = 'D'

    else:
        g = 'F'

    print(f"Grade: {g}, Score: {n}")