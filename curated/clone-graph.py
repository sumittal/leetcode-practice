from typing import Dict, List, Optional, Set


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None) -> None:
        # Use a fresh list so nodes with omitted neighbors do not share mutable state.
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Test helper: convert adjacency lists into a cyclic graph whose node values are 1-based.
def build_graph(adj: List[List[int]]) -> Optional[Node]:
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    # LeetCode adjacency values are one-based references into this node array.
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        copies: Dict[Node, Node] = {}

        def clone(current: Node) -> Node:
            # The helper returns the unique copy corresponding to each source node.
            # Reuse the mapped copy whenever a cycle reaches an already seen node.
            if current in copies:
                return copies[current]
            copies[current] = Node(
                current.val
            )  # Register before edges to break cycles.
            # Recursively cloning each edge preserves adjacency and cycles in the copy.
            copies[current].neighbors = [clone(n) for n in current.neighbors]
            # Neighbor order and repeated edges mirror the source adjacency list.
            return copies[current]

        return clone(node)


if __name__ == "__main__":
    for adj in ([[2, 4], [1, 3], [2, 4], [1, 3]], [[]], []):
        original = build_graph(adj)
        copied = Solution().cloneGraph(original)
        if original is None:
            assert copied is None
            continue
        seen_o = set()
        stack = [original]
        while stack:
            n = stack.pop()
            if n in seen_o:
                continue
            seen_o.add(n)
            stack.extend(n.neighbors)
        seen_c = set()
        stack = [copied]
        while stack:
            n = stack.pop()
            if n in seen_c:
                continue
            seen_c.add(n)
            stack.extend(n.neighbors)
        assert not (seen_o & seen_c)
        assert {n.val: [x.val for x in n.neighbors] for n in seen_o} == {
            n.val: [x.val for x in n.neighbors] for n in seen_c
        }
    print("All tests passed")
