import re
import random

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
