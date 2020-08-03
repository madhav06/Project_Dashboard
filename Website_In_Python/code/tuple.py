# Ep15
# Tuple is similar to a list except you cannot change elements of a tuple once it is defined. Whereas in a list, items can be modified.

# Basically, list is mutable whereas tuple is immutable.

language = ("Hindi", "Punjabi", "Tamil", "Odia", "Kannada")
print(language)

# tuple() function can also be used to create tuple.

# access elements:
language = ("Hindi", "Punjabi", "Tamil", "Odia", "Kannada")
print(language[0])
print(language[1])
print(language[-1])

language = ("Hindi", "Punjabi", "Tamil", "Odia", "Kannada")
del language # elements can not be deleted, however tuple itself can be.

print(language) # NameError: name 'language' is not defined.

