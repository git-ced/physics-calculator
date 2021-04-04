import re
from .variables import *


def trim(value):
    clean = value.replace(',', '')
    return clean.replace(' ', '')


def split_unit(value):
    compile = re.compile("{}{}".format(
        variables.number_regex,
        variables.alphabet_regex
    ))
    match = compile.match(value)
    if match:
        return match.groups()


def base(value):
    clean = trim(value)
    split = split_unit(clean)

    number = float(split[0])
    suffix = split[1]

    return number * variables.units[suffix]['value']


def convert(original, target):
    base_original = base(original)
    return base_original / variables.units[target]['value']


if __name__ == "__main__":
    convert()
