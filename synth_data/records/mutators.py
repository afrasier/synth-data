import re
import random


from typing import Callable

def mistyped(probability: float) -> Callable:
    '''
    Creates a function which permutes a string to have a mistyped key
    '''

    rand = random.SystemRandom()

    mistyped_dict = {
        "a": ["q", "s", "z"],
        "b": ["v", "g", "h", "n"],
        "c": ["x", "d", "v", "f"],
        "d": ["s", "e", "f", "c"],
        "e": ["w", "d", "r"],
        "f": ["d", "r", "g", "v"],
        "g": ["f", "t", "h", "b"],
        "h": ["g", "y", "j", "n"],
        "i": ["u", "k", "o"],
        "j": ["h", "k", "u", "m"],
        "k": ["j", "i", "l"],
        "l": ["o", "k", "p"],
        "m": ["n", "j", "k"],
        "n": ["b", "h", "j", "m"],
        "o": ["i", "l", "p"],
        "p": ["o", "l"],
        "q": ["w", "a", "s"],
        "r": ["e", "f", "t"],
        "s": ["a", "w", "d", "x"],
        "t": ["r", "g", "y"],
        "u": ["y", "j", "i"],
        "v": ["c", "f", "g", "b"],
        "w": ["q", "s", "e"],
        "x": ["z", "s", "d", "c"],
        "y": ["t", "h", "u"],
        "z": ["a", "s", "x"],
    }

    def mutator(string: str) -> str:
        if rand.random() <= probability and len(str) >= 3:
            index = rand.randint(0, len(string) - 2)
            char = string[index]

            if char.lower() not in mistyped_dict.keys():
                return string

            new_char = rand.choice(mistyped_dict[char.lower()])

            if char.isupper():
                new_char = new_char.upper()

            string = f"{string[:index]}{new_char}{string[index + 1:]}"

        return string

    return mutator
