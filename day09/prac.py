"""Day 9 practice: text, bytes, files, paths, and regular expressions."""

from pathlib import Path
import re


# Build paths from this file's folder so the examples work from any directory.
DAY09_DIR = Path(__file__).parent
SAMPLE_PATH = DAY09_DIR / "sample.txt"
LOG_PATH = DAY09_DIR / "logs.csv"


# -----------------------------------------------------------------------------
# 1. Text and bytes
# -----------------------------------------------------------------------------

# Text is a Python string. Bytes are raw values, often used for file or network data.
text = "Python"
data = b"Python"

print(data)
print(type(text))
print(type(data))

# Encoding converts text into bytes. UTF-8 can represent characters from many languages.
text = "café"
encoded = text.encode("utf-8")

print(text)
print(list(encoded))
print(type(encoded))

# Decoding converts bytes back into readable text using the matching encoding.
decoded = encoded.decode("utf-8")

print(decoded)
print(type(decoded))

# A UTF-8 BOM is a marker sometimes found at the beginning of a file.
bom = b"\xef\xbb\xbf"
content = b"name,city"
data = bom + content

print(data)

# Normal UTF-8 decoding keeps the BOM as the invisible character \ufeff.
text = data.decode("utf-8")
print(repr(text))

# The -sig codec removes the BOM while decoding.
text = data.decode("utf-8-sig")
print(repr(text))


# -----------------------------------------------------------------------------
# 2. Reading and writing text files
# -----------------------------------------------------------------------------

# The with statement closes the file automatically, even if an error occurs.
with SAMPLE_PATH.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.closed)

# Mode "w" creates a file or replaces its old contents.
output_path = DAY09_DIR / "output.txt"
with output_path.open("w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("Day 9\n")

with output_path.open("r", encoding="utf-8") as file:
    print(file.read())

# Mode "a" appends to the end instead of replacing existing contents.
with output_path.open("a", encoding="utf-8") as file:
    file.write("Another line\n")

with output_path.open("r", encoding="utf-8") as file:
    print(file.read())

# Write again to demonstrate that mode "w" clears the previous contents.
with output_path.open("w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("Day 9\n")

with output_path.open("r", encoding="utf-8") as file:
    print(file.read())


# -----------------------------------------------------------------------------
# 3. pathlib
# -----------------------------------------------------------------------------

# Path objects are a portable way to work with files and folders.
path = SAMPLE_PATH

print(type(path))
print(path.exists())
print(path.resolve())

content = path.read_text(encoding="utf-8")
print(content)


# -----------------------------------------------------------------------------
# 4. String cleanup and joining
# -----------------------------------------------------------------------------

line = "  INFO,2026-08-25,Ahmad,Success  \n"

# repr() makes spaces and newline characters visible while learning.
print(repr(line))
print(line.strip())

# strip() removes surrounding whitespace; split() separates a string into a list.
parts = line.strip().split(",")

print(parts)
print(type(parts))

# join() combines strings with a separator.
print(",".join(parts))
print("-".join(["2026", "08", "25"]))
print(" ".join(["Hello", "Python"]))
print("|".join(["Python", "Django", "Flask"]))


# -----------------------------------------------------------------------------
# 5. Replacing text and checking prefixes
# -----------------------------------------------------------------------------

# Strings are immutable, so replace() returns a new string and leaves the original unchanged.
text = "Python is hard"
new = text.replace("hard", "fun")

print(new)
print(text)

line = "ERROR,ERROR,INFO,ERROR"
new_line = line.replace("ERROR", "WARNING")

print(line)
print(new_line)

line = "ERROR,2026-08-25,Database connection failed"
print(line.startswith("ERROR"))
print(line.startswith("INFO"))


# -----------------------------------------------------------------------------
# 6. Regular expressions
# -----------------------------------------------------------------------------

# A regular expression, or regex, describes a text pattern to search for.
text = "Error code: 404"
result = re.search(r"\d+", text)

print(result)
print(result.group())

# \w+ finds one or more word characters.
text = "User_Ahmad123"
result = re.search(r"\w+", text)
print(result.group())

# Named groups make extracted values easier to understand.
text = "User: Ahmad"
result = re.search(r"User: (?P<name>\w+)", text)

print(result.group())
print(result.group("name"))
print(result.groupdict())

# Compile a reusable pattern for comma-separated log records.
LOG_PATTERN = re.compile(
    r"(?P<level>INFO|ERROR|WARNING),"
    r"(?P<date>\d+-\d+-\d+),"
    r"(?P<user>\w+),"
    r"(?P<message>.+)"
)

line = "ERROR,2026-08-25,Ali,Database connection failed"
result = LOG_PATTERN.search(line)

print(result.group())
print(result.groupdict())

# match() checks only at the beginning; search() can find a match later in the text.
ERROR_PATTERN = re.compile(r"ERROR")
text1 = "ERROR: database failed"
text2 = "2026-08-25 ERROR: database failed"

print(ERROR_PATTERN.match(text1))
print(ERROR_PATTERN.match(text2))
print(ERROR_PATTERN.search(text1))
print(ERROR_PATTERN.search(text2))

# findall() returns every matching part as a list.
text = "User 123 logged in. User 456 logged out. User 789 logged in."
ids = re.compile(r"\d+").findall(text)
print(ids)

# sub() replaces every match. This is useful for hiding sensitive values.
text = "Phone: 03001234567, Backup: 03111234567"
result = re.sub(r"\d+", "REDACTED", text)
print(result)


# -----------------------------------------------------------------------------
# 7. Formatted strings
# -----------------------------------------------------------------------------

name = "Ahmad\nAli"
price = 19.98765
a = 10
b = 5

# !r shows the value's representation, while :.2f formats a number to two decimals.
print(f"{name}")
print(f"{name!r}")
print(f"Price: {price:.2f}")
print(f"Total: {a + b}")


# -----------------------------------------------------------------------------
# 8. Binary files and file metadata
# -----------------------------------------------------------------------------

# Write and read non-ASCII text as bytes.
binary_path = DAY09_DIR / "binary.txt"
data = "café پاکستان".encode("utf-8")
binary_path.write_bytes(data)

read_data = binary_path.read_bytes()
print(read_data)
print(read_data.decode("utf-8"))
print(read_data)
print(type(read_data))

# stat() returns metadata such as access time and file size in bytes.
info = binary_path.stat()
print("time:", info.st_atime)
print("size:", info.st_size)


# -----------------------------------------------------------------------------
# 9. Log-file practice functions
# -----------------------------------------------------------------------------

# read_file first tries UTF-8 with optional BOM support, then falls back to Latin-1.
def read_file(path):
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin1")


# parse_line converts one valid CSV-style log line into a dictionary.
def parse_line(line):
    result = LOG_PATTERN.search(line)
    if result:
        return result.groupdict()
    return None


# parse_file reads each line and keeps only lines matching the log pattern.
def parse_file(path):
    records = []
    for line in read_file(path).splitlines():
        record = parse_line(line)
        if record is not None:
            records.append(record)
    return records


# filter_errors selects records whose level is ERROR.
def filter_errors(records):
    errors = []
    for record in records:
        if record["level"] == "ERROR":
            errors.append(record)
    return errors


# write_records converts dictionaries back into CSV-style lines and saves them.
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

    path.write_text("\n".join(lines), encoding="utf-8")
    return lines


# Create a separate output file so the original logs.csv remains available for practice.
errors_path = DAY09_DIR / "errors_practice.csv"
error_records = filter_errors(parse_file(LOG_PATH))
print(write_records(errors_path, error_records))

# Latin-1 is useful for older files that contain characters outside UTF-8.
latin1_path = DAY09_DIR / "latin1_practice.txt"
latin1_path.write_bytes("café".encode("latin-1"))
print(parse_file(latin1_path))

# A BOM-prefixed file can be read because read_file uses utf-8-sig.
bom_path = DAY09_DIR / "bom_practice.csv"
bom_path.write_bytes(
    b"\xef\xbb\xbfINFO,2026-08-25,Ahmad,Login successful"
)
print(parse_file(bom_path))

print(parse_file(LOG_PATH))
print(read_file(errors_path))
print(read_file(LOG_PATH))
print(read_file(bom_path))
