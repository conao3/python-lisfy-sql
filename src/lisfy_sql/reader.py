from typing import Optional
import more_itertools

from . import types


def consume_whitespace(input_stream: more_itertools.peekable) -> None:
    while (peek := input_stream.peek(None)) is not None:
        if not peek.isspace():
            break

        read_char(input_stream)


def read_token(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: Optional[str] = None,
    recursive_p: bool = False,
) -> Optional[str]:
    consume_whitespace(input_stream)

    peek: Optional[str] = input_stream.peek(None)

    if peek is None:
        if eof_error_p:
            raise EOFError('unexpected EOF while reading token')

        return eof_value

    token = ''
    while (peek := input_stream.peek(None)) is not None:
        if peek.isspace():
            break

        char = read_char(input_stream)
        assert char is not None
        token += char

    return token


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

    token = read_token(input_stream)

    return types.Statement()
