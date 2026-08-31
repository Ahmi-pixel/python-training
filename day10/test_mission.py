import pytest
from pathlib import Path
from mission import(
    ParseError,
    InvalidFormatError,
    InvalidDateError,
    parse_date,
    parse_line,
    parse_file,
    read_file,
    del_file
)

@pytest.mark.parametrize("date_text", [
    "2026-09-23",
    "2025-12-20",
    "2023-11-13",
    "2024-02-29"
])

def test_parse_date(date_text):
    result = parse_date(date_text, 1)

    assert result.isoformat() == date_text

@pytest.mark.parametrize("date_text",[
    "2026-22-90",
    "1897-45-33",
    "12-09-2029",
    "3033-200-30"
])

def test_invalid_date(date_text):
    with pytest.raises(InvalidDateError) as exc_info:
            parse_date(date_text, 8)
    exc = exc_info.value

    assert exc.line_no == 8
    assert isinstance(exc.__cause__, ValueError)

@pytest.mark.parametrize("line", [
    "BANANA,2026-08-25,Ali,Something happened",
    "ERROR,2026-08-25,Ali",
    "ERROR,25/08/2026,Ali,Something happened",
    "ERROR,2026-08-25,,Something happened",
    "",
    "This is completely invalid",
])

def test_invalid_log(line):
    with pytest.raises(InvalidFormatError) as exc_inf0:
        parse_line(line, 5)

    exc = exc_inf0.value
    assert exc.line_no == 5
    assert exc.__cause__ is None

def test_parse_file():
    path = Path("day09/logs.csv")

    records = parse_file(path)

    assert len(records) > 0

    for record in records:
        assert "level" in record
        assert "user" in record
        assert "date" in record
        assert "message" in record

def test_missing_file():
    path = Path("doesnt_matter.csv")

    result = parse_file(path)

    assert result == []
