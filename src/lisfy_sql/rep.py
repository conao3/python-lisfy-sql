from typing import Optional
import more_itertools

from . import reader
from . import types


def read(x: str) -> Optional[types.Statement]:
    stream = more_itertools.peekable(x)
    return reader.read(stream)


def eval(x: Optional[types.Statement]) -> Optional[types.Statement]:
    return x


def print(x: Optional[types.Statement]) -> str:
    return str(x)


def rep(x: str) -> str:
    return print(eval(read(x)))
