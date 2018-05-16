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
        "0": ["1", "2", "3", "9"],
        "1": ["0", "2", "4"],
        "2": ["1", "0", "3", "5"],
        "3": ["2", "6", "4"],
        "4": ["3", "5", "7", "1"],
        "5": ["4", "6", "2", "8"],
        "6": ["5", "7"],
        "7": ["4", "8", "6"],
        "8": ["7", "9", "5"],
        "9": ["8", "6"],
    }

    def mutator(string: str) -> str:
        if rand.random() <= probability and len(string) >= 3:
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


def misheard(probability: float) -> Callable:
    '''
    Creates a function which permutes a string to have a mistyped key
    '''

    rand = random.SystemRandom()

    misheard_dict = {
        "b": ["c", "g", "v"],
        "c": ["b", "g", "v"],
        "g": ["p", "t", "z"],
        "i": ["y"],
        "m": ["n"],
        "n": ["m"],
        "p": ["t", "g"],
        "t": ["p", "g"],
        "v": ["z"],
        "y": ["i"],
        "z": ["g", "v"],
        "5": ["9"],
        "9": ["5"],
    }

    def mutator(string: str) -> str:
        if rand.random() <= probability and len(string) >= 3:
            index = rand.randint(0, len(string) - 2)
            char = string[index]

            if char.lower() not in misheard_dict.keys():
                return string

            new_char = rand.choice(misheard_dict[char.lower()])

            if char.isupper():
                new_char = new_char.upper()

            string = f"{string[:index]}{new_char}{string[index + 1:]}"

        return string

    return mutator


def misread(probability: float) -> Callable:
    '''
    Creates a function which permutes a string to have a mistyped key
    '''

    rand = random.SystemRandom()

    misread_dict = {
        "l": ["b", "i"],
        "b": ["l"],
        "g": ["q"],
        "q": ["g"],
        "m": ["n"],
        "n": ["m"],
        "y": ["z"],
        "z": ["y"],
        "c": ["e"],
        "e": ["c", "i"],
        "i": ["e", "l"],
        "a": ["o"],
        "o": ["a"],
        "T": ["I"],
        "I": ["T"],
        "D": ["O"],
        "O": ["D"],
        "E": ["F"],
        "F": ["E"]
    }

    def mutator(string: str) -> str:
        if rand.random() <= probability and len(string) >= 3:
            index = rand.randint(0, len(string) - 2)
            char = string[index]

            if char not in misread_dict.keys():
                return string

            new_char = rand.choice(misread_dict[char])

            string = f"{string[:index]}{new_char}{string[index + 1:]}"

        return string

    return mutator
