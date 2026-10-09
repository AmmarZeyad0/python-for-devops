import re 

text = "Hello World \
    My name is Ammar \
        I love programming in Python \
            Python is a great programming language "
pattern = r"Python"
result = re.findall(pattern, text)
print(result)  # Output: []