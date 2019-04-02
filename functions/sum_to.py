# Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
    acc = 0
    for n in range(n):
        acc += n + 1
    return acc

for n in range(0,12,3):
    print(f" {n} sum_to = {sum_to(n)}")