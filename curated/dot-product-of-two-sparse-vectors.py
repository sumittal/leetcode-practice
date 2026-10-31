from typing import Dict, List


class SparseVector:
    # Nonzero values are indexed by original position in a sparse map.
    # Dot product work is proportional to the smaller map's nonzero count.
    # Missing indices contribute zero without being materialized.
    def __init__(self, nums: List[int]):
        # Zero entries cannot contribute and are omitted from the representation.
        self.values: Dict[int, int] = {
            index: value for index, value in enumerate(nums) if value
        }

    def dotProduct(self, vec: "SparseVector") -> int:
        # Both maps retain original vector indices, not compacted positions.
        smaller, larger = self.values, vec.values
        if len(smaller) > len(larger):
            smaller, larger = larger, smaller
        # Missing indices are zero, so only stored nonzero positions need visits.
        total = 0
        for index, value in smaller.items():
            total += value * larger.get(index, 0)
        # A shared zero-free index is the only possible nonzero contribution.
        # Iterating the smaller map minimizes lookups for differently sparse inputs.
        return total


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs = []
    vectors = []
    for operation, values in zip(ops, args):
        if operation == "SparseVector":
            vector = SparseVector(*values)
            vectors.append(vector)
            outputs.append(None)
        else:
            outputs.append(vectors[0].dotProduct(vectors[1]))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SparseVector", "SparseVector", "dotProduct"],
        [[[1, 0, 0, 2, 3]], [[0, 3, 0, 4, 0]], []],
    ) == [None, None, 8]
    assert replay(
        ["SparseVector", "SparseVector", "dotProduct"],
        [[[-1, 0, 0, 0, 0]], [[0, 0, 0, 0, 2]], []],
    ) == [None, None, 0]
    assert replay(
        ["SparseVector", "SparseVector", "dotProduct"],
        [[[2, -3]], [[-4, 5]], []],
    ) == [None, None, -23]
    print("All tests passed")
