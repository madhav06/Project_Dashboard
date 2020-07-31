# A file operation takes place in the following order.

# Open a file
# Read or write (perform operation)
# Close the file

# You can use open() function to open a file.
f = open("test.txt") # open file in current directory
f = open("C:/Python34/README.txt") # specifying full path

f = open("test.txt") # equivalent to 'r or 'rt'
f = open("test.txt", 'w') # write in text mode
f = open("img.bmp", 'r+b') # read and write in binary mode

# To close a file you use close() method.

f = open("test.txt", encoding='utf-8')
# perform file operations
f.close()

# In order to write a file in python, we need to open it in 'w', append 'a' 
# or exclusive creation 'x' mode.
# 
with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

# To read a file, you must open the file in reading mode.
f = open("test.txt", 'r', encoding='utf-8')
f.read(4) # read first 4 data 