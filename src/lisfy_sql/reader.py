from typing import Optional
import more_itertools

from . import types


def consume_whitespace(input_stream: more_itertools.peekable) -> None:
    while (peek := input_stream.peek(None)) is not None:
        if not peek.isspace():
            break

        read_char(input_stream)


def read_char(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: Optional[str] = None,
    recursive_p: bool = False,
) -> Optional[str]:
    peek: Optional[str] = input_stream.peek(None)
    if peek is None:
        if eof_error_p:
            raise EOFError('unexpected EOF while reading character')

        return eof_value

    return next(input_stream)


def read(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: str = '',
    recursive_p: bool = False,
) -> types.Statement:
    consume_whitespace(input_stream)
    return types.Statement()
