from typing import Optional
import more_itertools

from . import types


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
    
    return peek


def read(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: str = '',
    recursive_p: bool = False,
) -> types.Statement:
    return types.Statement()
