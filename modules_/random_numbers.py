import random

lower_bound = 1
upper_bound = 100

random_float = random.random()
random_integer = random.randint(lower_bound, upper_bound)

print(f"Random float between 0 and 1: {random_float}")
print(f"Random integer between {lower_bound} and {upper_bound}: {random_integer}")
