import re
text = "Hello World"
pattern = r"hello"
result = re.match(pattern, text)
print(result)  # Output: <re.Match object; span=(0, 5), match='Hello'>