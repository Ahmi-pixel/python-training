class ParseError(Exception):
    pass


try:
    int("abc")
except ValueError as exc:
    raise ParseError("Could not parse the number") from exc