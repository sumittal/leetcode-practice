"""
LeetCode 1724: Checking Existence of Edge Length Limited Paths II
Difficulty: Hard
Pattern: Depth-First Search
Video Reference: https://www.youtube.com/results?search_query=leetcode+1724+Checking+Existence+of+Edge+Length+Limited+Paths+II+neetcode
Complexity:
    - Time: construction O(m log m + n log n), query O(log n)
    - Space: O(n log n + m)
"""

from collections import deque
from typing import Deque, List, Tuple


class DisjointSet:
    def __init__(self, size: int):
        # Initially every graph vertex is its own component.
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            # Path halving shortens future root lookups.
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first: int, second: int) -> bool:
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False
        # Rank keeps the Kruskal disjoint-set forest shallow.
        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1
        return True


class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.n = n
        levels = max(1, n.bit_length())
        adjacency: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        dsu = DisjointSet(n)
        # Kruskal skips cycle edges so the retained graph is a forest.
        # Kruskal's minimum spanning forest preserves minimum path bottlenecks.
        for first, second, weight in sorted(edgeList, key=lambda edge: edge[2]):
            if dsu.union(first, second):
                adjacency[first].append((second, weight))
                adjacency[second].append((first, weight))
        self.component = [-1] * n
        self.depth = [0] * n
        self.up = [[0] * n for _ in range(levels)]
        self.maximum = [[0] * n for _ in range(levels)]
        for root in range(n):
            if self.component[root] != -1:
                continue
            self.component[root] = root
            # Each unvisited vertex starts one forest component traversal.
            self.up[0][root] = root
            queue: Deque[int] = deque([root])
            while queue:
                node = queue.popleft()
                for child, weight in adjacency[node]:
                    # Parent and already assigned neighbors are not revisited.
                    if child == self.up[0][node] and node != root:
                        continue
                    if child == root or self.component[child] != -1:
                        continue
                    self.component[child] = root
                    self.depth[child] = self.depth[node] + 1
                    self.up[0][child] = node
                    self.maximum[0][child] = weight
                    queue.append(child)
        # Each higher row doubles the ancestor jump and stores its path maximum.
        for level in range(1, levels):
            for node in range(n):
                middle = self.up[level - 1][node]
                self.up[level][node] = self.up[level - 1][middle]
                self.maximum[level][node] = max(
                    self.maximum[level - 1][node],
                    self.maximum[level - 1][middle],
                )

    def query(self, p: int, q: int, limit: int) -> bool:
        if self.component[p] != self.component[q]:
            return False
        if p == q:
            return True
        # Lift the deeper endpoint while accumulating the path bottleneck.
        path_max = 0
        if self.depth[p] < self.depth[q]:
            p, q = q, p
        difference = self.depth[p] - self.depth[q]
        bit = 0
        while difference:
            if difference & 1:
                path_max = max(path_max, self.maximum[bit][p])
                p = self.up[bit][p]
            difference >>= 1
            bit += 1
        if p != q:
            # Lift both endpoints until their parents are the lowest common ancestor.
            for level in range(len(self.up) - 1, -1, -1):
                if self.up[level][p] != self.up[level][q]:
                    path_max = max(
                        path_max,
                        self.maximum[level][p],
                        self.maximum[level][q],
                    )
                    p = self.up[level][p]
                    q = self.up[level][q]
            path_max = max(
                path_max, self.maximum[0][p], self.maximum[0][q]
            )
        # The problem requires every traversed edge to be strictly below limit.
        return path_max < limit


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    graph = None
    for op, values in zip(ops, args):
        if op == "DistanceLimitedPathsExist":
            graph = DistanceLimitedPathsExist(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(graph, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["DistanceLimitedPathsExist", "query", "query", "query"],
        [[3, [[0, 1, 2], [1, 2, 5]]], [0, 2, 6], [0, 2, 5], [0, 0, 1]],
    ) == [None, True, False, True]
    assert replay(
        ["DistanceLimitedPathsExist", "query", "query"],
        [[4, [[0, 1, 4], [2, 3, 7]]], [0, 2, 10], [0, 1, 4]],
    ) == [None, False, False]
    print("All tests passed")
