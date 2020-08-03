# Ep19
# Generators
# There is a lot of overhead in building an iterator in Python, 
# We have to implement a class with __iter__() and __next__() method, keep track of internal states, 
# raise "StopIteration" when there was no value to be returned.

# This is lengthy and counter-intuitive. 
# Generator comes into rescue in such situations.

# Python generators are a simple way of creating iterators.

# Decorators

# Python has an interesting feature called decorators to add functionality to an existing code. This is also called metaprogramming as a 
# part of the program tries to modify another part of the program at compile time.