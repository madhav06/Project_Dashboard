# Ep13and14
# Dictionary is an un-ordered collection of items. A dictionary has key:value pair.

my_dict = {} # empty dict

my_dict = {1: 'cricket', 2: 'hockey'} # keys are integers

my_dict = {'name': 'Mukesh', 1: [23,24, 45]}
print(my_dict)

# you can also use dict() function to create dictionary.

# to access values from dict, use keys.

person = {'name': 'Mukesh', 'age': 24, 'sal': 42000}
print(person)
print(person['sal'])
print(person['name'])

# Changing age to 32
person['age'] = 32
print(person)

# Adding job key value pair
person['job'] = 'Accountant'
print(person)

# Deleting salary
del person['sal']
print(person)

# Deleting entire dictionary
del person