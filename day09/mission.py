from pathlib import Path

import re

line = "ERROR,2026-08-25,Ali,Database connection failed"

pattern = re.compile(
    r"(?P<level>INFO|ERROR|WARNING),(?P<date>\d+-\d+-\d+),(?P<user>\w+),(?P<message>.+)"
    )

path = Path("day09/logs.csv")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin1") as file:
            return file.read()
        
def parse_file(path):
    content = read_file(path)
    records = []
    for line in content.splitlines():
        record = parse_line(line)
        if record is not None:
            records.append(record)
    return records

def parse_line(line):
    result = pattern.search(line)
    if result:
        return result.groupdict()
    return None

def filter_errors(records):
    error = []
    for record in records:
        if record["level"] == "ERROR":
            error.append(record)
    return error

def write_records(path, records):
    lines = [] 
    for record in records:   
        values = [
        record["level"],
        record["date"],
        record["user"],
        record["message"]
        ]

        lines.append(",".join(values))
    path.write_text("\n".join(lines), encoding="utf-8")
    return lines

if __name__ == "__main__":


    output_path = Path("day09/errors.csv")

    write_records(
        output_path,
        filter_errors(parse_file(path))
    )
        
    print(parse_file(Path("day09/latin1.txt")))

    print(parse_file(Path("day09/logs.csv")))