from collections import Counter
from typing import Dict, List, Optional, Union


class Encrypter:
    def __init__(
        self, keys: List[str], values: List[str], dictionary: List[str]
    ):
        # Each plaintext character maps to one fixed two-character code.
        self.forward: Dict[str, str] = dict(zip(keys, values))
        # The static dictionary lets decrypt answer without exploring branches.
        self.encrypted_counts = Counter()
        for word in dictionary:
            encrypted = self.encrypt(word)
            if encrypted:
                self.encrypted_counts[encrypted] += 1
        # Dictionary counts preserve multiple plaintexts with identical output.

    def encrypt(self, word1: str) -> str:
        result = []
        # Concatenation preserves source order and adds no separators.
        for character in word1:
            code = self.forward.get(character)
            if code is None:
                # One unmapped character makes the whole word unencryptionable.
                return ""
            result.append(code)
        return "".join(result)

    def decrypt(self, word2: str) -> int:
        # Count only plaintexts in the permitted dictionary.
        # The preprocessing work replaces exponential code branching with a lookup.
        # Arbitrary segmentations are excluded unless a dictionary word matched.
        return self.encrypted_counts[word2]


def replay(
    ops: List[str], args: List[List[object]]
) -> List[Optional[Union[str, int]]]:
    outputs: List[Optional[Union[str, int]]] = []
    encrypter = None
    for operation, values in zip(ops, args):
        if operation == "Encrypter":
            encrypter = Encrypter(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(encrypter, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Encrypter", "encrypt", "decrypt"],
        [
            [["a", "b", "c", "d"], ["ei", "zf", "ei", "am"],
             ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda",
              "abad"]],
            ["abcd"],
            ["eizfeiam"],
        ],
    ) == [None, "eizfeiam", 2]
    assert replay(
        ["Encrypter", "encrypt", "decrypt", "decrypt"],
        [[["a", "b"], ["xy", "xy"], ["a", "b", "aa"]], ["c"], ["xy"], ["x"]],
    ) == [None, "", 2, 0]
    print("All tests passed")
