# Define a function for multiplication/division of two numbers with Global variables:
num1 = 100
num2 = 50
def multiplication():
    
    print("the result of multiplication is:", num1 * num2)
    
multiplication()

def division():
    print("the result of division is:", num1 / num2)
division()

def addition(a, b):
    print ("the result of addition is:", a + b)
addition(10, 20)

def add (a, b):
    return a + b
result = add(10, 20)
print("the result of addition is:", result)

def get_details():
    name = "John"
    age = 30
    return name, age
print(get_details())

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

result = check_even_odd(1)
print("The number is:", result)

def add (a, b):
    return a + b
result = add(10, 20)
print("the result of addition is:", result)