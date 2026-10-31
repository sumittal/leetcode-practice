import heapq
from typing import List, Optional


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # Directed edges are stored only at their source vertex.
        self.graph: List[List[tuple]] = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        source, target, cost = edge
        # Appending preserves parallel edges; Dijkstra chooses the cheapest route.
        self.graph[source].append((target, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # Positive weights let Dijkstra finalize a node when its best path is popped.
        distances = {node1: 0}
        queue = [(0, node1)]
        # The queue always expands the cheapest currently known path first.
        while queue:
            distance, node = heapq.heappop(queue)
            # Ignore an older, more expensive candidate left in the heap.
            if distance != distances.get(node):
                continue
            if node == node2:
                # The minimum queue key is final because all edge costs are positive.
                return distance
            for neighbor, cost in self.graph[node]:
                # Relax only strict improvements to avoid redundant heap entries.
                candidate = distance + cost
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))
        # Exhausting reachable vertices proves there is no path to node2.
        return -1


def replay(ops: List[str], args: List[List[object]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    graph = None
    for operation, values in zip(ops, args):
        if operation == "Graph":
            graph = Graph(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(graph, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"],
        [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]],
         [3, 2], [0, 3], [[1, 3, 4]], [0, 3]],
    ) == [None, 6, -1, None, 6]
    assert replay(
        ["Graph", "shortestPath", "addEdge", "shortestPath"],
        [[2, []], [0, 1], [[0, 1, 7]], [0, 1]],
    ) == [None, -1, None, 7]
    print("All tests passed")
