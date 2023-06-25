def read(x: str) -> str:
    return x


def eval(x: str) -> str:
    return x


def print(x: str) -> str:
    return x


def rep(x: str) -> str:
    return print(eval(read(x)))
