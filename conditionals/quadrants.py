# Exercise 4:
# Prompt for letter and number. A and B are columns (left and right). 1 and 2 are rows (top and bottom):

#     A    B
#   -----------
# 1 | UL | UR |
#   -----------
# 2 | LL | LR |
#   -----------
# Print out which quadrant corresponds to what the user entered: "upper right", "upper left", "lower right", "lower left".

col = input('Please choose a column (A-B)\n>> ')

row = input('Please choose a row (1-2)\n>> ')




g = {
    "a1": "00",
    "a2": "00",
    "b1": "00",
    "b2": "00"
}

g[col + row] = 'XX'

print(g[f"{col + row}"])

print(g)

print('     A    B')
print('  -----------')
print(f"1 | {g['a1']} | {g['b1']} |")
print('  -----------')
print(f"2 | {g['a2']} | {g['b2']} |")