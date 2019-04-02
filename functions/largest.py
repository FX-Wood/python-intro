# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:
# largest([10, 4, 2, 231, 91, 54])  # returns 231
# largest([1,2,3,4,0])  # returns 4

def largest(arr):
    max = 0
    for n in arr:
        if n > max:
            max = n
    return max


tests = [
    [0,10,0,0], # 0
    [1,0,0,0], # 1
    [0,0,0,1], # 1
    [10, 4, 2, 231, 91, 54], # 231
    [1, 2, 3, 4, 0] # 4
]

for case in tests:
    print(f" finding the largest for {case}: {largest(case)}")