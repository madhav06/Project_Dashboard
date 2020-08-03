#

# A string is a sequence of characters.
# many ways we can create string.

new_String = 'Hey'
print(new_String)

new_String = "Heyy"
print(new_String)

new_String = '''Heyy'''
print(new_String)

# Ep6and7
# triple quotes string can extend multiple lines.
# accssing characters using indexing

str = "Happy Birthday"
print("Greetings: ", str)
print('str[0] : ', str[0])
print('str[-1] : ', str[-1])

#slicing 2nd to 5th character
print(str[1:5])

# Strings are immutable. You cannot change elements of a string once it is assigned. 
# However, you can assign one string to another. Also, you can delete the string using del operator.

# Concatenation is probably the most common string operation.
#  To concatenate strings, you use + operator. Similarly, the * operator can be used to repeat the string for a given number of times.