# Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

def occurances(sample, substr):
    i = 0
    count = 0
    print(f"{sample} + {substr}")
    for char in sample:
        if sample[i : i + len(substr)] == substr:
            count += 1
        i += 1
    return count

print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))   # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0