from typing import Optional
import more_itertools

from . import create
from .. import reader
from .. import types


mapping = {
    'create': create.read,
}

def read(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: types.Statement = types.Statement(),
    recursive_p: bool = False,
) -> types.Statement:
    reader.consume_whitespace(input_stream)

    token = reader.read_token(input_stream)
    reveal_type(token)

    if token is None:
        if eof_error_p:
            raise EOFError('unexpected EOF while reading token')

        return eof_value

    if (fn := mapping.get(token)) is None:
        raise ValueError(f'unknown token: {token}')

    return types.Statement()
