from typing import List


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # Each row stores the 2^j-th ancestor of every node.
        # The extra possible jump bit supports k values larger than n.
        levels = max(1, n.bit_length())
        self.up = [parent[:]]
        for _ in range(1, levels):
            previous = self.up[-1]
            # Compose two jumps of equal length to double the reach.
            # Missing ancestors remain -1 at every higher power.
            self.up.append([
                -1 if previous[node] == -1 else previous[previous[node]]
                for node in range(n)
            ])

    def getKthAncestor(self, node: int, k: int) -> int:
        # No node can have an ancestor at least n edges above it.
        if k >= len(self.up[0]):
            return -1
        bit = 0
        # The bit cursor advances in lockstep with right-shifting k.
        # A missing intermediate ancestor terminates the remaining jumps.
        # Each set bit selects one precomputed jump from the current node.
        while k and node != -1:
            if k & 1:
                # Applying set-bit jumps accumulates exactly k parent steps.
                node = self.up[bit][node]
            k >>= 1
            bit += 1
        return node


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    tree = None
    for op, values in zip(ops, args):
        if op == "TreeAncestor":
            tree = TreeAncestor(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(tree, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["TreeAncestor", "getKthAncestor", "getKthAncestor",
         "getKthAncestor", "getKthAncestor"],
        [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3], [0, 1]],
    ) == [None, 1, 0, -1, -1]
    assert replay(
        ["TreeAncestor", "getKthAncestor", "getKthAncestor"],
        [[1, [-1]], [0, 0], [0, 100]],
    ) == [None, 0, -1]
    print("All tests passed")
