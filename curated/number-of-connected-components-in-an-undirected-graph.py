from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # parent[x] points toward a root shared by every member of x's component.
        parent = list(range(n))

        # Initially each labeled vertex is its own disjoint component.
        def find(x: int) -> int:
            # Following parent links reaches the representative of this component.
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path halving shortens later lookups.
                x = parent[x]
            return x

        components = n
        # A component count of zero is valid only for the empty vertex set.
        # Processing each edge either joins two sets or leaves their count unchanged.
        for a, b in edges:
            # An edge reduces the count only when it joins distinct components.
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb  # Joining two roots merges exactly two components.
                components -= 1
        return components


if __name__ == "__main__":
    solution = Solution()
    assert solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert solution.countComponents(4, [[0, 1], [1, 2], [2, 3]]) == 1
    assert solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert solution.countComponents(3, []) == 3
    print("All tests passed")
