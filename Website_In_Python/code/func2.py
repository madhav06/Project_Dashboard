# Ep11
# some more about functions

# A function that calls itself is known as recursive function and 
# this process is called recursion.
# Every recursive function must have base condition that stops the recursion 
# or else the function calls itself infinitely.
# 
def fact_(x):
    if x == 1:
        return 1
    else:
        return (x*fact_(x-1))

num = 6
print("factorial of", num, "is", fact_(num))


# lambda function- a function without a name.
# to create lambda function, use keyword lambda.

square = lambda x: x **2
print(square(5))