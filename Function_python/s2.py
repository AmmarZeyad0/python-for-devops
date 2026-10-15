# Function for addition
def add(a, b):
    return a + b

add_result = add(10, 5)
print(f"Addition: {add_result}")
# Function for Subtraction
def subtract(a, b):
    return a - b
 
subtract_result = subtract(10, 5)
print(f"Subtraction: {subtract_result}")
# Function for Multiplication
def multiply(a, b):
    return a * b
multiply_result = multiply(10, 5)
print(f"Multiplication: {multiply_result}")
# Function for Division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
divide_result = divide(10, 5) 
print(f"Division: {divide_result}")

# 1
def greet(name):
    print(f"Hello, {name}!")
    
greet("Ammar")
#2
greet("John")

#3 
# Function for addition

def add(a, b):
     return a + b

# call the function
result = add(10, 20)

# Print the result
print(f"The result of addition is: {result}")