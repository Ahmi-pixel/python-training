from day09.mission import parse_line, filter_errors, parse_file, write_records

from pathlib import Path

import pytest

line = "ERROR,2026-08-25,Ali,Database connection failed"

def test_parse_line():
    result = parse_line(line)
    assert result["level"] == "ERROR"
    assert result["date"] == "2026-08-25"
    assert result["user"] == "Ali"
    assert result["message"] == "Database connection failed"

@pytest.mark.parametrize("line", [
    "ERROR,2026-08-25,Ali",
    "BANANA,2026-08-25,Ali,Something happened",
    "ERROR,25/08/2026,Ali,Something happened",
    "ERROR,2026-08-25,,Something happened",
    ""
])
def test_malformed_lines(line):
    assert parse_line(line) is None

def test_filter_errors():
    records = [
        {"level": "INFO",
        "date": "2026-08-25",
        "user": "Ahmad",
        "message": "Login successful",},
        {
        "level": "ERROR",
        "date": "2026-08-25",
        "user": "Ali",
        "message": "Database connection failed",
        },
        {
        "level": "ERROR",
        "date": "2026-08-25",
        "user": "Sara",
        "message": "Database connection failed",
        },
        {
        "level": "WARNING",
        "date": "2026-08-25",
        "user": "Ahmad",
        "message": "Database connection failed",
        }
    ]
    result = filter_errors(records)
    assert len(result) == 2
    assert result[0]["level"] == "ERROR"
    assert result[1]["level"] == "ERROR"

def test_parse_file():
    path = Path("day09/logs.csv")
    records = parse_file(path)
    assert len(records) > 0
    for record in records:
        assert "level" in record
        assert "user" in record
        assert "date" in record
        assert "message" in record

def test_write_records(tmp_path):
    output_path = tmp_path / "errors.csv"
    one = [{
        "level": "WARNING",
        "date": "2026-08-25",
        "user": "Ahmad",
        "message": "Database connection failed",
    }]
    write_records(output_path, one)
    content = output_path.read_text(encoding="utf-8")
    assert content == "WARNING,2026-08-25,Ahmad,Database connection failed"