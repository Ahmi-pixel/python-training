import re
from datetime import date
from pathlib import Path
from contextlib import suppress

pattern = re.compile(
    r"(?P<level>INFO|ERROR|WARNING),"
    r"(?P<date>\d+-\d+-\d+),"
    r"(?P<user>\w+),"
    r"(?P<message>.+)"
)

class ParseError(Exception):
    def __init__(self, message, line_no):
        super().__init__(message)
        self.message = message
        self.line_no = line_no

    def __str__(self):
        return f"Line no: {self.line_no}, {self.message}"

class InvalidDateError(ParseError):
    pass

class InvalidFormatError(ParseError):
    pass

def parse_date(date_text, line_no):
    try:
        year, month, day = map(int, date_text.split("-"))
        return date(year, month, day)
    except ValueError as exc:
        raise InvalidDateError(
            "Invalid date",
            line_no
        )from exc

def parse_line(line, line_no):
    result = pattern.search(line)
    if not result:
        raise InvalidFormatError(
            "Invalid log format",
            line_no
        )
    record = result.groupdict()
    parse_date(record["date"], line_no)
    return record

def parse_file(path):
    with suppress(FileNotFoundError):
        content = read_file(path)
        records = []

        for line_no, line in enumerate(content.splitlines(), start=1):
            record = parse_line(line, line_no)
            records.append(record)
        return records
    print(f"Waning {path} not found.")
    return []

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin1") as file:
            return file.read()

def del_file():
    with suppress(FileNotFoundError):
        Path("temporary.csv").unlink()
        print("File deleted.")

# print(del_file())

# path = Path("day09/logs.csv")
# print(parse_file(path))

# print(parse_file("day10/badlogs.csv"))
# print(parse_file("day10/doesnt_matter.csv"))

# try:
#     print(parse_file(Path("day10/badlogs.csv")))
# except ParseError as exc:
#     print(exc)
#     print(type(exc))
#     print(exc.__cause__)

# print(parse_line(
#     "ERROR,2026-08-25,Ali,Database connection failed", 1))
# try:
#     parse_line("ERROR,2026-99-95,Ali,Database connection failed", 1)

# except InvalidDateError as exc:
#     print(exc)
#     print(type(exc))
#     print(type(exc.__cause__))

try:
    parse_line("Invalid log format", 5)

except InvalidFormatError as exc:
    print(exc)
    print(type(exc.__cause__))
