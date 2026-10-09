import re
text = "Hello World!"
pattern = r"World!"
result = re.search(pattern, text)
print(result)  # Output: []