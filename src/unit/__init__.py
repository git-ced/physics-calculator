import re
from .variables import *


def trim(value):
    clean = value.replace(',', '')
    return clean.replace(' ', '')


def split_unit(value):
    if (any(map(str.isalpha, value))):
        compile = re.compile("{}{}".format(
            variables.number_regex,
            variables.alphabet_regex
        ))
        match = compile.match(value)
        if match:
            return match.groups()
    else:
        return [value]


def base(value):
    clean = trim(value)
    split = split_unit(clean)

    number = float(split[0])
    suffix = split[1] if len(split) == 2 else 'base'

    return number * variables.units[suffix]['value']


def convert(original, target):
    base_original = base(original)
    return base_original / variables.units[target]['value']


if __name__ == "__main__":
    convert()
