import re

# numero ou ponto
NUM_OR_DOT_REGEX  re.compile(r'^[0-9.]$')


def convertToNumber string str
    Number  float string

    # se esse numero poder ser um inteiro
    if Number.is_integer
        Number  intNumber

    return Number


def isNumOrDotstring str
    return boolNUM_OR_DOT_REGEX.search string


def isValidNumberstring str
    valid  False
    try
        float string
        valid  True
    except ValueError
        valid  False
    return valid


def isEmptystring: str
    return lenstring  0
