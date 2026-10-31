from collections import defaultdict
from typing import Dict, List, Set


class MagicDictionary:
    # Pattern buckets limit each search to the query's character positions.
    # Bucket values retain the character hidden by each wildcard.
    def __init__(self):
        self.patterns: Dict[str, Set[str]] = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        # A wildcard at each position groups equal-length words by all other chars.
        for word in dictionary:
            # Different lengths cannot share a wildcard position pattern.
            for index, char in enumerate(word):
                pattern = word[:index] + "*" + word[index + 1:]
                # Store the omitted character to enforce a real substitution.
                self.patterns[pattern].add(char)

    def search(self, searchWord: str) -> bool:
        # Testing one wildcard pattern per position checks all substitutions.
        for index, char in enumerate(searchWord):
            pattern = searchWord[:index] + "*" + searchWord[index + 1:]
            # A different stored character means exactly one substitution works.
            if any(other != char for other in self.patterns.get(pattern, set())):
                return True
        # Equal words alone do not satisfy the exactly-one-character rule.
        return False


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    dictionary = None
    for op, values in zip(ops, args):
        if op == "MagicDictionary":
            dictionary = MagicDictionary()
            outputs.append(None)
        elif op == "buildDict":
            dictionary.buildDict(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(dictionary, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MagicDictionary", "buildDict", "search", "search", "search",
         "search"],
        [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"],
         ["leetcoded"]],
    ) == [None, None, False, True, False, False]
    print("All tests passed")
