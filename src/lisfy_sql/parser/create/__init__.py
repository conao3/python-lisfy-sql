from typing import Optional

import more_itertools
from ... import types


def read(
    input_stream: more_itertools.peekable,
    eof_error_p: bool = True,
    eof_value: Optional[str] = None,
    recursive_p: bool = False,
) -> types.Statement:
    return types.Statement()
