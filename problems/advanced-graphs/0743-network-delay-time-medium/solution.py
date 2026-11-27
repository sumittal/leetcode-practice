"""
LeetCode 743: Network Delay Time
Difficulty: Medium
Pattern: Advanced Graphs
Video Reference: https://www.youtube.com/watch?v=EaphyqKU4PQ
Complexity:
    - Time: O((V + E) log V)
    - Space: O(V + E)
"""

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Directed adjacency preserves the direction of each weighted signal edge.
        graph = [[] for _ in range(n + 1)]
        # Node labels are one-based, leaving index zero unused.
        for source, destination, weight in times:
            graph[source].append((destination, weight))
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        # Heap entries are tentative arrival times ordered from earliest to latest.
        # The source is the sole initial frontier entry at time zero.
        frontier = [(0, k)]
        while frontier:
            arrival, node = heapq.heappop(frontier)
            if arrival > distances[node]:
                # Ignore stale entries superseded by a shorter route.
                continue
            for neighbor, travel_time in graph[node]:
                candidate = arrival + travel_time
                if candidate < distances[neighbor]:
                    # Relax only when this path improves the best known arrival.
                    distances[neighbor] = candidate
                    heapq.heappush(frontier, (candidate, neighbor))
                # Nonnegative travel times make finalized distances safe to retain.
        # Every node must be reachable; otherwise the signal cannot reach the network.
        latest = max(distances[1:])
        return int(latest) if latest != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert solution.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert solution.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    assert solution.networkDelayTime([], 1, 1) == 0
    print("All tests passed")
