# range() returns an immutable sequence of numbers between 
# the given start integer to the stop integer.

print(range(1, 10))
# the output is an iterable and you can convert it to list, set, tuple etc.
numbers = range(1, 6)

print(list(numbers)) # Output: [1,2,3,4,5]
print(tuple(numbers)) # Output: (1,2,3,4,5)
print(set(numbers)) # Output: {1,2,3,4,5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99}
print(dict.fromkeys(numbers, 99))

# Some more on range
numbers1 = range(1, 6, 1)
print(list(numbers1)) # Output: [1,2,3,4,5]

numbers2 = range(1, 6, 2)
print(list(numbers2)) # Output: [1,3,5]

numbers3 = range(5, 0, -1)
print(list(numbers3)) # Output: [5, 4, 3, 2, 1]