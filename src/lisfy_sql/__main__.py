from . import rep


def main():
    while True:
        try:
            text = input('lisfy-sql > ')
        except EOFError:
            break

        if (res := rep.rep(text)):
            print(res)
