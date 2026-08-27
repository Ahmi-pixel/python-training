# Day 9: Files, Paths, Encoding, Regex, and Testing

> **Big idea:** Turn raw file data into useful Python objects, process it, and test the result.

## Learning Goals

By the end of this lesson, you should be able to:

- Work with file and folder paths using `pathlib`.
- Understand the difference between text (`str`) and bytes (`bytes`).
- Encode and decode text safely.
- Read and write text and binary files.
- Clean and split strings.
- Use regular expressions to find and extract data.
- Build a small log-file processing pipeline.
- Write and run tests with `pytest`.

## The Day 9 Pipeline

We start with a raw CSV-like line:

```text
ERROR,2026-08-25,Ali,Database connection failed
```

The parser turns it into a dictionary:

```python
{
    "level": "ERROR",
    "date": "2026-08-25",
    "user": "Ali",
    "message": "Database connection failed",
}
```

The complete flow is:

```text
read file -> split into lines -> parse lines -> dictionaries
         -> filter ERROR records -> build CSV lines -> write output
```

## 1. `pathlib.Path`

Instead of building paths by joining strings manually, Python provides `Path` objects.

```python
from pathlib import Path

# This path is relative to the folder where the program is run.
path = Path("day09/logs.csv")

# Path objects can be used to read and write files.
content = path.read_text(encoding="utf-8")
path.write_text("Hello Python", encoding="utf-8")
```

### Useful operations

| Expression | Meaning |
| --- | --- |
| `path.exists()` | Checks whether the path exists |
| `path.resolve()` | Returns the absolute path |
| `path.name` | Returns the file name, such as `logs.csv` |
| `path.parent` | Returns the containing folder |
| `folder / "file.txt"` | Safely joins path parts |

```python
folder = Path("day09")
path = folder / "logs.csv"
```

The `/` operator joins paths in a platform-independent way. Avoid manually writing `"day09/" + "logs.csv"`.

## 2. Text and Bytes

Python uses two important types when dealing with files and external data:

| Type | Meaning | Example |
| --- | --- | --- |
| `str` | Human-readable text | `"Hello Python"` |
| `bytes` | Raw binary data | `b"Hello Python"` |

```python
text = "Hello Python"
data = b"Hello Python"

print(type(text))
# <class 'str'>
print(type(data))
# <class 'bytes'>
```

Remember this conversion pattern:

```text
str --encode()--> bytes --decode()--> str
```

### Encoding and decoding

Encoding converts text into bytes. Decoding converts bytes back into text.

```python
text = "café"

# UTF-8 represents the text as bytes.
data = text.encode("utf-8")
print(data)

# Use the same encoding to turn the bytes back into text.
text_again = data.decode("utf-8")
print(text_again)
```

## 3. Encoding

Computers store file data as bytes. An encoding tells Python how those bytes represent characters.

UTF-8 is a good default because it supports characters from many languages:

```python
examples = "English café پاکستان 中文 日本語"
data = examples.encode("utf-8")
text_again = data.decode("utf-8")
```

When opening text files, state the encoding explicitly:

```python
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## 4. Unicode Decode Errors and Latin-1

If a file was created with a different encoding, reading it as UTF-8 can raise `UnicodeDecodeError`.

A reader can try UTF-8 first and use Latin-1 as a fallback:

```python
def read_file(path):
    try:
        # utf-8-sig also handles a UTF-8 BOM if one is present.
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.read()
    except UnicodeDecodeError:
        # Latin-1 can read every byte value, but it may not give the
        # correct characters unless the file was actually Latin-1.
        with open(path, "r", encoding="latin1") as file:
            return file.read()
```

The important lesson is not “always use Latin-1.” First find out which encoding the file actually uses. UTF-8 should normally be the first choice for modern text.

## 5. UTF-8 BOM

Some programs add a **Byte Order Mark**, or BOM, at the beginning of a UTF-8 file.

```python
bom_data = b"\xef\xbb\xbfINFO,2026-08-25,Ahmad,Login successful"

# Normal UTF-8 decoding keeps the BOM as the invisible character \ufeff.
text = bom_data.decode("utf-8")
print(repr(text))

# utf-8-sig removes the BOM while decoding.
text = bom_data.decode("utf-8-sig")
print(repr(text))
```

Use `encoding="utf-8-sig"` when a UTF-8 file may contain a BOM, especially files produced by some Windows applications.

## 6. Newline Characters and `strip()`

A newline is a real character written as `\n`. It moves output to the next line but is not obvious when printed normally.

```python
line = "ERROR,2026-08-25,Ali,Database connection failed\n"

# repr() makes hidden characters visible.
print(repr(line))
# 'ERROR,2026-08-25,Ali,Database connection failed\n'

# strip() removes whitespace from both ends, including the newline.
clean = line.strip()
print(clean)
```

`strip()` removes more than only newlines. It also removes surrounding spaces and tabs.

## 7. `splitlines()` and `split()`

Use `splitlines()` to turn a block of text into separate lines:

```python
content = """Hello
Python
World"""

lines = content.splitlines()
print(lines)
# ['Hello', 'Python', 'World']
```

Use `split()` when you want to separate one line around a delimiter:

```python
line = "INFO,2026-08-25,Ahmad,Success"
parts = line.split(",")
print(parts)
# ['INFO', '2026-08-25', 'Ahmad', 'Success']
```

The log-processing pipeline uses both operations:

```python
content = read_file(path)
for line in content.splitlines():
    parts = line.strip().split(",")
```

## 8. Joining Strings

`join()` puts a separator between every string in a collection.

```python
values = ["ERROR", "2026-08-25", "Ali"]

print(",".join(values))
# ERROR,2026-08-25,Ali
print("-".join(["2026", "08", "25"]))
# 2026-08-25
print(" ".join(["Hello", "Python"]))
# Hello Python
```

Every item must already be a string. Use `str(value)` when necessary.

## 9. Regular Expressions

A regular expression, or regex, describes a pattern to search for in text.

```python
import re

# \d+ means one or more digits.
pattern = re.compile(r"\d+")
result = pattern.search("Error code: 404")

print(result.group())
# 404
```

### Common regex symbols

| Pattern | Meaning | Example match |
| --- | --- | --- |
| `\d` | One digit | `4` |
| `\d+` | One or more digits | `404` |
| `\w` | One word character | `A` |
| `\w+` | One or more word characters | `Ahmad` |
| `.` | Almost any character except newline | `E` |
| `.+` | One or more non-newline characters | `Error` |
| `|` | OR | `INFO|ERROR` |

Use a raw string, written with `r"..."`, for regex patterns so backslashes are easier to read.

### Named groups

A named group captures a part of the match with a useful label:

```python
text = "User: Ahmad"
pattern = re.compile(r"User: (?P<name>\w+)")
result = pattern.search(text)

print(result.group())
# User: Ahmad
print(result.group("name"))
# Ahmad
print(result.groupdict())
# {'name': 'Ahmad'}
```

### `match()` versus `search()`

- `match()` checks only at the beginning of a string.
- `search()` can find a match anywhere in a string.

```python
pattern = re.compile(r"ERROR")

print(pattern.match("ERROR: database failed"))
# Match found
print(pattern.match("2026-08-25 ERROR: database failed"))
# None
print(pattern.search("2026-08-25 ERROR: database failed"))
# Match found
```

### `findall()` and `sub()`

```python
# findall() returns every match as a list.
text = "User 123 logged in. User 456 logged out."
ids = re.compile(r"\d+").findall(text)
print(ids)
# ['123', '456']

# sub() replaces every match.
phones = "Phone: 03001234567, Backup: 03111234567"
redacted = re.sub(r"\d+", "REDACTED", phones)
print(redacted)
# Phone: REDACTED, Backup: REDACTED
```

## 10. Parsing Log Records

This pattern allows only the levels `INFO`, `ERROR`, and `WARNING`:

```python
LOG_PATTERN = re.compile(
    r"(?P<level>INFO|ERROR|WARNING),"
    r"(?P<date>\d+-\d+-\d+),"
    r"(?P<user>\w+),"
    r"(?P<message>.+)"
)
```

The named groups describe the four fields in every record:

- `level`
- `date`
- `user`
- `message`

### `group()` and `groupdict()`

```python
line = "ERROR,2026-08-25,Ali,Database connection failed"
result = LOG_PATTERN.search(line)

print(result.group())
print(result.group("level"))
# ERROR
print(result.groupdict())
# {
#     'level': 'ERROR',
#     'date': '2026-08-25',
#     'user': 'Ali',
#     'message': 'Database connection failed'
# }
```

### `parse_line()`

```python
def parse_line(line):
    # search() returns a match object for valid input, or None otherwise.
    result = LOG_PATTERN.search(line)

    if result:
        # Convert the named groups directly into a dictionary.
        return result.groupdict()

    # Invalid lines are ignored by returning None.
    return None
```

Example:

```python
valid_line = "ERROR,2026-08-25,Ali,Database connection failed"
invalid_line = "BANANA,2026-08-25,Ali,Something happened"

print(parse_line(valid_line))
print(parse_line(invalid_line))
# None
```

## 11. Parsing a Whole File

`parse_file()` reads the file, processes one line at a time, and stores valid records.

```python
def parse_file(path):
    content = read_file(path)
    records = []

    for line in content.splitlines():
        record = parse_line(line)

        # Do not add malformed lines to the result.
        if record is not None:
            records.append(record)

    return records
```

For a file containing four valid lines, the result is a list of four dictionaries. This is easier to work with than raw text.

### Why process one line at a time?

The regex uses `.+` for the message. In regex, `.` normally does not match a newline. Processing each line separately keeps each record independent and avoids needing the `re.DOTALL` option.

## 12. Filtering Records

`filter_errors()` keeps only dictionaries whose `level` is `ERROR`.

```python
def filter_errors(records):
    errors = []

    for record in records:
        if record["level"] == "ERROR":
            errors.append(record)

    return errors
```

The input must contain dictionaries, not raw CSV strings. `record["level"]` works only after `parse_line()` has converted a line into a dictionary.

## 13. Building and Writing CSV Lines

Convert one dictionary into one CSV-style line:

```python
record = {
    "level": "ERROR",
    "date": "2026-08-25",
    "user": "Ali",
    "message": "Database connection failed",
}

values = [
    record["level"],
    record["date"],
    record["user"],
    record["message"],
]

line = ",".join(values)
print(line)
# ERROR,2026-08-25,Ali,Database connection failed
```

Build and write multiple lines:

```python
def write_records(path, records):
    lines = []

    for record in records:
        values = [
            record["level"],
            record["date"],
            record["user"],
            record["message"],
        ]
        lines.append(",".join(values))

    # Join records with newlines and write text using UTF-8.
    path.write_text("\n".join(lines), encoding="utf-8")
    return lines
```

Use `read_text()` and `write_text()` for text. Use `read_bytes()` and `write_bytes()` for binary data.

## 14. Context Managers

A context manager closes a file automatically:

```python
with open(path, "r", encoding="utf-8") as file:
    content = file.read()

# The file is closed after the with block ends.
print(file.closed)
# True
```

Without `with`, you must close the file yourself:

```python
file = open(path, "r", encoding="utf-8")
content = file.read()
file.close()
```

Prefer `with` because it also closes the file if an error occurs inside the block.

## 15. Testing with Pytest

A pytest test function must start with `test_`:

```python
def test_parse_line():
    result = parse_line("ERROR,2026-08-25,Ali,Database connection failed")

    assert result["level"] == "ERROR"
    assert result["user"] == "Ali"
```

Run tests with:

```bash
pytest
pytest day09
pytest day09 -v
```

The `-v` option means verbose and shows each test name.

### What does `1 passed` mean?

`1 passed` means one pytest test function or test case passed. A single test can contain several assertions:

```python
def test_record():
    assert result["level"] == "ERROR"
    assert result["date"] == "2026-08-25"
    assert result["user"] == "Ali"
```

If all three assertions succeed, pytest reports one passed test.

### `pytest.mark.parametrize`

`pytest.mark.parametrize()` runs one test function several times with different inputs. Each tuple creates a separate test case.

```python
import pytest


@pytest.mark.parametrize(
    "line",
    [
        "ERROR,2026-08-25,Ali",
        "BANANA,2026-08-25,Ali,Something happened",
        "ERROR,25/08/2026,Ali,Something happened",
        "ERROR,2026-08-25,,Something happened",
        "",
    ],
)
def test_malformed_lines(line):
    # Every example above should be rejected by the parser.
    assert parse_line(line) is None
```

Five input values create five test cases. This is shorter and clearer than writing five separate functions.

### A common list mistake

Remember the commas between strings:

```python
cases = [
    "case 1",
    "case 2",
    "case 3",
]
```

Without commas, adjacent string literals are combined by Python:

```python
value = "Hello" "World"
print(value)
# HelloWorld
```

## 16. `tmp_path` for Safe File Tests

The `tmp_path` fixture provides a temporary directory for a test. Use it instead of changing real project files.

```python
def test_write_records(tmp_path):
    # This file is temporary and is cleaned up after the test.
    output_path = tmp_path / "errors.csv"
    records = [{
        "level": "WARNING",
        "date": "2026-08-25",
        "user": "Ahmad",
        "message": "Disk space low",
    }]

    write_records(output_path, records)
    content = output_path.read_text(encoding="utf-8")

    assert content == "WARNING,2026-08-25,Ahmad,Disk space low"
```

## 17. The Main Guard

Code at module level runs when the module is imported. To run demonstration code only when a file is executed directly, use the main guard:

```python
if __name__ == "__main__":
    print(parse_file(Path("day09/logs.csv")))
```

This runs with:

```bash
python3 day09/mission.py
```

It does not run when another file imports a function:

```python
from day09.mission import parse_line
```

This keeps reusable functions separate from manual demonstration code and prevents unwanted output during pytest collection.

## 18. Python Package and Import Names

When `day09` contains `__init__.py`, it can be imported as a package:

```text
day09/
├── __init__.py
├── mission.py
└── test_mission.py
```

Use the unambiguous package import from the project root:

```python
from day09.mission import parse_line
```

This matters because another folder may also contain a file named `mission.py`, such as `day08/mission.py`. A plain `from mission import ...` can accidentally import the wrong module depending on the working directory.

## Day 9 Practice Mission

Build and test these functions:

- `read_file(path)`: read UTF-8 and fall back to Latin-1.
- `parse_line(line)`: convert a valid log line into a dictionary.
- `parse_file(path)`: parse every valid line in a file.
- `filter_errors(records)`: keep only `ERROR` records.
- `write_records(path, records)`: write records as CSV-style text.

Your tests should cover:

- A valid log line
- Malformed log lines
- Empty input
- Filtering multiple records
- Parsing a real file
- Writing and reading a temporary output file
- UTF-8, UTF-8 BOM, and Latin-1 input where relevant

## Final Architecture

```text
logs.csv
   |
   v
read_file()
   |
   v
raw text
   |
   v
splitlines()
   |
   v
parse_line()
   |
   v
dictionaries / records
   |
   v
filter_errors()
   |
   v
ERROR records
   |
   v
write_records()
   |
   v
errors.csv
```

## Quick Revision

| Topic | Main idea |
| --- | --- |
| `Path` | Portable file and folder paths |
| `str` and `bytes` | Text versus raw data |
| Encoding | Converts between text and bytes |
| `utf-8-sig` | Reads UTF-8 files and removes a BOM |
| `splitlines()` | Splits a block of text into lines |
| Regex | Finds text that follows a pattern |
| Named groups | Give extracted regex values readable names |
| `groupdict()` | Returns named regex groups as a dictionary |
| `Counter` | Not used here; Day 9 focuses on file processing |
| `tmp_path` | Keeps file tests isolated and safe |
| Main guard | Prevents demo code from running during imports |

## Biggest Lesson

The most important skill is moving between representations:

```text
bytes
  | encode / decode
  v
str
  | splitlines
  v
individual lines
  | regex
  v
dictionaries
  | filtering
  v
list of dictionaries
  | join
  v
CSV strings
  | write
  v
file
```
