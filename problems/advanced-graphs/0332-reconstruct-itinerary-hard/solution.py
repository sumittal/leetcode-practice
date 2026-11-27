"""
LeetCode 332: Reconstruct Itinerary
Difficulty: Hard
Pattern: Advanced Graphs
Video Reference: https://www.youtube.com/watch?v=ZyB_gQ8vqGA
Complexity:
    - Time: O(E log E)
    - Space: O(E)
"""

from typing import Dict, List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Reverse-sorted adjacency lets each airport pop its smallest destination.
        flights: Dict[str, List[str]] = {}
        # Multiple tickets to the same destination remain separate list entries.
        for origin, destination in tickets:
            flights.setdefault(origin, []).append(destination)
        for destinations in flights.values():
            destinations.sort(reverse=True)
        # Sorting costs O(E log E); popping each ticket afterward is constant time.
        # Airports without outgoing tickets need no adjacency entry until visited.
        # Hierholzer's stack follows unused tickets until a route dead-ends.
        route_stack = ["JFK"]
        reverse_route = []
        while route_stack:
            airport = route_stack[-1]
            if flights.get(airport):
                # Consume each ticket once; smallest lexical edges are explored first.
                # The top remains at this airport until its outgoing tickets run out.
                route_stack.append(flights[airport].pop())
            else:
                # A dead-end airport belongs at the end of the final Eulerian route.
                reverse_route.append(route_stack.pop())
            # Backtracking occurs only after the current node has no unused edge.
            # Each ticket removed during forward traversal appears in one final step.
        # Dead-end insertion order is postorder, so reverse to recover itinerary order.
        reverse_route.reverse()
        # Postorder insertion also correctly splices cycles into earlier route segments.
        # The problem guarantees a valid itinerary using every ticket.
        return reverse_route


if __name__ == "__main__":
    solution = Solution()
    assert solution.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    ) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert solution.findItinerary(
        [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    ) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    itinerary = solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    assert itinerary == ["JFK", "NRT", "JFK", "KUL"]
    print("All tests passed")
