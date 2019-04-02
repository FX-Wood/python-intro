# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).

def product(*args):
    val = 1
    for n in args:
        val *= n
    return val

tests = [
    [1], # should return 1
    [0], # should return 0
    [10, 10, 10, 10], # should return 10,000
    [n +1 for n in list(range(5))]
]

for case in tests:
    print(product(*case))
