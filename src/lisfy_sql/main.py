import typing
from typing import Any, Literal, Optional


def fn0(text: str, eof_error_p: bool = True, eof_value: Optional[str] = None) -> Optional[str]:
    if text.isspace():
        if eof_error_p:
            raise Exception()
        return eof_value
    return text


res = fn0("a")
reveal_type(res)

res = fn0("a", eof_error_p=False)
reveal_type(res)

res = fn0("a", eof_error_p=False, eof_value="b")
reveal_type(res)


###


@typing.overload
def fn1(text: str, eof_error_p: Literal[True] = True, eof_value: Any = None) -> str: ...

T = typing.TypeVar('T', bound=Optional[str])
@typing.overload
def fn1(text: str, eof_error_p: Literal[False] = False, eof_value: T = None) -> str | T: ...

def fn1(text: str, eof_error_p: bool = True, eof_value: Optional[str] = None) -> Optional[str]:
    if text.isspace():
        if eof_error_p:
            raise Exception()
        return eof_value
    return text


res = fn1("a")
reveal_type(res)

res = fn1("a", eof_error_p=False)
reveal_type(res)

res = fn1("a", eof_error_p=False, eof_value="b")
reveal_type(res)
