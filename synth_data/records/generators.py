import re
import random

from dateutil.parser import parse
from datetime import timedelta

from typing import Callable


def number_generator(format: str = '###-###-####') -> Callable:
    '''
    Creates a generator which creates numbers in the specified format

    Format is specified as a string, where all occurances of # will be replaced
    with an integer. For example, 1-###-###-#### or (###) ###-####
    '''
    rand = random.SystemRandom()

    # Generates a random integer from 0-9
    def random_integer(param: str) -> str:
        return str(rand.randint(0, 9))

    def generator():
        while True:
            yield re.sub('#', random_integer, format)

    return generator()


def range_generator(start: int = 0, end: int = 10) -> Callable:
    '''
    Creates a generator which creates numbers in the specified range
    '''
    rand = random.SystemRandom()

    def generator():
        while True:
            yield str(rand.randint(start, end))

    return generator()


def date_generator(range_start: str, range_end: str) -> Callable:
    '''
    Creates a generator which generates date strings within a given range (inclusive)
    Ranges are specified as ISO strings
    '''
    rand = random.SystemRandom()

    range_start = parse(range_start)
    range_end = parse(range_end)

    spread = (range_end - range_start).total_seconds()

    def generator():
        while True:
            yield str(range_start + timedelta(seconds=rand.randint(0, spread)))

    return generator()
