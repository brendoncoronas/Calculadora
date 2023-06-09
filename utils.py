import re

# numero ou ponto
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def convertToNumber(string: str):
    Number = float(string)

    # se esse numero poder ser um inteiro
    if Number.is_integer():
        Number = int(Number)

    return Number


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0
