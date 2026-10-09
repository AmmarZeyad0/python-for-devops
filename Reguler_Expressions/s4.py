import re
pattern = r"\s+"
string = "Python   is   great"
new_string = re.sub(pattern, " ", string)
print(new_string)  # Output: Python is great