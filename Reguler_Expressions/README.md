# Python Regular Expressions (Regex) for DevOps 🚀

Regular Expressions (Regex) are an essential superpower for DevOps engineers. Whether you are parsing unstructured system logs, checking CI/CD pipeline outputs, or filtering command-line results (`kubectl`, `docker`), regex lets you search, extract, and manipulate text instantly without writing complex string-splitting logic.

---

## 1. The Core `re` Functions

Python’s built-in `re` module provides powerful tools for pattern matching:

| Function | Description | Best Used For |
| :--- | :--- | :--- |
| **`re.search()`** | Scans the string and returns the **first occurrence** anywhere. | Checking if a log line contains an error keyword. |
| **`re.match()`** | Checks for a match **only at the very beginning** of the string. | Validating strict prefixes or formats from index 0. |
| **`re.findall()`** | Finds **all non-overlapping matches** and returns them as a list. | Extracting all IP addresses, error codes, or IDs. |
| **`re.sub()`** | Finds occurrences of a pattern and **replaces** them. | Sanitizing logs, masking API keys, or updating configs. |
| **`re.finditer()`** | Returns an **iterator of match objects** (including start/end indices). | Extracting matches along with their exact positions. |
| **`re.split()`** | Splits a string using a **regex pattern** as the delimiter. | Splitting logs by complex delimiters (multiple spaces, punctuation). |

---

## 2. Cheat Sheet: Special Characters & Quantifiers

### Special Characters
* **`.`** — Any character except a newline.
* **`^`** — Start of the string or line.
* **`$`** — End of the string or line.
* **`\d`** — Any digit (`0-9`).
* **`\s`** — Any whitespace character (spaces, tabs, newlines).
* **`\w`** — Any word character (letters, numbers, underscores).
* **`\\`** — Escape character for special symbols (e.g., `\.` matches an actual dot).

### Quantifiers
* **`+`** — 1 or more times (e.g., `\d+` matches multi-digit numbers).
* **`*`** — 0 or more times.
* **`?`** — 0 or 1 time (makes things optional or non-greedy).
* **`{n,m}`** — Between `n` and `m` times.

---

## 3. Real-World DevOps Example: Parsing Nginx Logs

Here is how you can use Python and regex to extract specific data (like HTTP status codes) by giving your pattern **context**:

```python
import re

log_lines = """
192.168.1.10 - - [10/Oct/2026:13:55:02 +0000] "GET /api/v1/health HTTP/1.1" 200 1234
10.0.0.5 - - [10/Oct/2026:13:55:04 +0000] "POST /api/v1/deploy HTTP/1.1" 500 452
192.168.1.22 - - [10/Oct/2026:13:55:08 +0000] "GET /favicon.ico HTTP/1.1" 404 509
"""  

# Pattern: Match "HTTP/1.1" followed by a space, then capture 3 digits using a capture group
pattern = r'HTTP/\d\.\d"\s(\d{3})'

status_codes = re.findall(pattern, log_lines)
print(status_codes)  # Output: ['200', '500', '404']