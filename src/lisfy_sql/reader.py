import more_itertools

from . import types


def read(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: str = '',
    recursive_p: bool = False,
) -> types.Statement:
    return types.Statement()
