from typing import List


class CombinationIterator:
    # A compact index tuple generates combinations without materializing them.
    def __init__(self, characters: str, combinationLength: int):
        # Input characters arrive sorted, so index order is lexicographic order.
        self.characters = characters
        self.length = combinationLength
        # The increasing index tuple represents the next lexicographic choice.
        self.indices: List[int] = list(range(combinationLength))

    def next(self) -> str:
        result = "".join(self.characters[index] for index in self.indices)
        # Save the current combination before moving the cursor forward.
        # Advance the rightmost position that still leaves room for successors.
        pivot = self.length - 1
        while (
            pivot >= 0
            and self.indices[pivot] == len(self.characters) - self.length + pivot
        ):
            pivot -= 1
        if pivot >= 0:
            self.indices[pivot] += 1
            for index in range(pivot + 1, self.length):
                self.indices[index] = self.indices[index - 1] + 1
        else:
            # An empty tuple is a compact terminal state after the final result.
            self.indices = []
        return result

    def hasNext(self) -> bool:
        # Exhaustion is represented by an empty index tuple.
        return bool(self.indices)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "CombinationIterator":
            iterator = CombinationIterator(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    iterator = CombinationIterator("abc", 2)
    # The generator emits combinations in dictionary order without storing all.
    values = []
    while iterator.hasNext():
        values.append(iterator.next())
    assert values == ["ab", "ac", "bc"]
    iterator = CombinationIterator("abcd", 3)
    assert [iterator.next(), iterator.next()] == ["abc", "abd"]
    print("All tests passed")
