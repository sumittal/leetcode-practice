from collections import Counter
from typing import Dict


class TwoSum:
    # Complement checks use the frequency map as both membership and multiplicity.
    # Values can be added repeatedly, so a plain set would lose valid pairs.
    # The find operation intentionally scans distinct keys only.
    def __init__(self):
        # The frequency table compresses repeated values without losing pairs.
        self.counts: Dict[int, int] = Counter()

    def add(self, number: int) -> None:
        # Frequencies preserve duplicate values needed for equal complements.
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        # Scanning distinct values is cheaper than enumerating all stored pairs.
        for number, count in self.counts.items():
            # Checking each complement pair once is sufficient for existence.
            complement = value - number
            if complement not in self.counts:
                continue
            # Equal endpoints need two copies, not one occurrence used twice.
            if complement != number or count > 1:
                return True
        return False


def replay(ops: list, args: list) -> list:
    outputs = []
    structure = None
    for op, values in zip(ops, args):
        if op == "TwoSum":
            structure = TwoSum()
            outputs.append(None)
        else:
            result = getattr(structure, op)(*values)
            outputs.append(result)
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TwoSum", "add", "add", "add", "find", "find"],
        [[], [1], [3], [5], [4], [7]],
    ) == [None, None, None, None, True, False]
    assert replay(
        ["TwoSum", "add", "find", "add", "find"],
        [[], [3], [6], [3], [6]],
    ) == [None, None, False, None, True]
    print("All tests passed")
