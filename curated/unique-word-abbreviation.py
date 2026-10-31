from collections import defaultdict
from typing import Dict, List, Set


def abbreviate(word: str) -> str:
    # Short strings have no interior characters to replace with a count.
    if len(word) <= 2:
        return word
    return word[0] + str(len(word) - 2) + word[-1]


class ValidWordAbbr:
    # Distinct words, rather than dictionary occurrences, determine ambiguity.
    # Each query inspects only the set for its computed abbreviation.
    # Abbreviations are deterministic functions of their source words.
    def __init__(self, dictionary: List[str]):
        self.words_by_abbr: Dict[str, Set[str]] = defaultdict(set)
        # Sets prevent duplicate dictionary entries from creating false conflicts.
        for word in dictionary:
            self.words_by_abbr[abbreviate(word)].add(word)
        # Construction cost is linear in total dictionary characters.

    def isUnique(self, word: str) -> bool:
        # A distinct dictionary word with the same abbreviation is a conflict.
        # An abbreviation is unique when absent or owned only by this word.
        return self.words_by_abbr.get(abbreviate(word), set()) <= {word}


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    dictionary = None
    for op, values in zip(ops, args):
        if op == "ValidWordAbbr":
            dictionary = ValidWordAbbr(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(dictionary, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique"],
        [[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"],
         ["make"]],
    ) == [None, False, True, False, True]
    assert replay(
        ["ValidWordAbbr", "isUnique", "isUnique"],
        [[["a", "a", "it"]], ["a"], ["to"]],
    ) == [None, True, True]
    print("All tests passed")
