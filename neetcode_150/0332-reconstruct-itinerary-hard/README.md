# 332. Reconstruct Itinerary

**Difficulty:** Hard  
**Tags:** Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit, Eulerian Path, Semi-Eulerian Graph  
**Pattern:** Advanced Graphs  
**LeetCode:** [https://leetcode.com/problems/reconstruct-itinerary/](https://leetcode.com/problems/reconstruct-itinerary/)

## Problem

You are given a list of airline `tickets` where `tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)

```

**Input:** tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
**Output:** ["JFK","MUC","LHR","SFO","SJC"]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)

```

**Input:** tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
**Output:** ["JFK","ATL","JFK","SFO","ATL","SFO"]
**Explanation:** Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

```

**Constraints:**

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`
- `from<sub>i</sub>.length == 3`
- `to<sub>i</sub>.length == 3`
- `from<sub>i</sub>` and `to<sub>i</sub>` consist of uppercase English letters.
- `from<sub>i</sub> != to<sub>i</sub>`

## Video Explanation

[Reconstruct Itinerary - Leetcode 332 - Python](https://www.youtube.com/watch?v=ZyB_gQ8vqGA)

## Approach

### Intuition

Use every ticket once while always choosing the smallest available destination; Hierholzer's traversal handles detours and cycles.

### Brute Force

Try ticket permutations from JFK in lexical order until a route consumes every ticket.

### Optimal

Sort adjacency in reverse lexical order, run iterative Hierholzer traversal, and reverse the postorder route.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(E!) | O(E) |
| Optimal | O(E log E) | O(E) |

### Edge cases

- Several tickets may share the same origin and destination.
- A valid itinerary may revisit airports and contain cycles.
