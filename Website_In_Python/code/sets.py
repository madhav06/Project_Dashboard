# Ep16
# A set is an unordered collection of items where every element is unique (no duplicates).

# You can also use set() function to create sets.

# Sets are mutable. You can add, remove and delete elements of a set. However, you cannot replace one item of a set with another as they are unordered and indexing have no meaning.

my_set = {1, 3, 5}
print(my_set)

my_mixed_set = {2.0, "Hello", (4, 6, 9)}
print(my_mixed_set)

my_set = {1, 3, 5}
my_set.add(7)
my_set.add(9)
print(my_set)

# some more on set:
A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B)
print(A | B)

# Equivalent to A.intersection(B)
print(A & B)

# Set difference 
print(A - B)

# Set symmetric difference
print(A ^ B)