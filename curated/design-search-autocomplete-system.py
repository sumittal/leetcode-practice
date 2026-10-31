from typing import Dict, List, Optional, Union


class AutocompleteSystem:
    # Prefix candidate sets limit each suggestion query to matching sentences.
    # Ranking uses current frequency and then lexical order for deterministic ties.
    # Sentence completion updates both the count map and every indexed prefix.
    def __init__(self, sentences: List[str], times: List[int]):
        # Counts define ranking while each prefix stores candidate membership.
        self.counts: Dict[str, int] = dict(zip(sentences, times))
        self.prefixes: Dict[str, set] = {}
        self.current = ""
        # Initial sentences populate every prefix they can answer.
        for sentence in sentences:
            self._index(sentence)

    def _index(self, sentence: str) -> None:
        prefix = ""
        for character in sentence:
            prefix += character
            # Inserting a sentence touches each prefix once, proportional to length.
            # Each prefix set contains precisely the sentences beginning there.
            self.prefixes.setdefault(prefix, set()).add(sentence)

    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.current:
                # A completed sentence gains one occurrence and becomes searchable.
                self.counts[self.current] = self.counts.get(self.current, 0) + 1
                self._index(self.current)
            self.current = ""
            # The next call starts a fresh query after sentence submission.
            return []
        self.current += c
        # Prefix lookup avoids examining sentences that cannot match the query.
        candidates = self.prefixes.get(self.current, set())
        # Frequency descends first; lexical order breaks every tie deterministically.
        # Truncating after sorting returns only the requested three suggestions.
        return sorted(candidates, key=lambda item: (-self.counts[item], item))[:3]


def replay(
    ops: List[str], args: List[list]
) -> List[Optional[Union[List[str], int]]]:
    outputs: List[Optional[Union[List[str], int]]] = []
    system = None
    for operation, values in zip(ops, args):
        if operation == "AutocompleteSystem":
            system = AutocompleteSystem(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(system, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["AutocompleteSystem", "input", "input", "input", "input"],
        [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]],
         ["i"], [" "], ["a"], ["#"]],
    ) == [
        None,
        ["i love you", "island", "i love leetcode"],
        ["i love you", "i love leetcode"],
        [],
        [],
    ]
    assert replay(
        ["AutocompleteSystem", "input", "input", "input", "input"],
        [[["abc"], [2]], ["a"], ["b"], ["#"], ["a"]],
    ) == [None, ["abc"], ["abc"], [], ["abc", "ab"]]
    print("All tests passed")
