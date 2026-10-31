# 684. Redundant Connection

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/redundant-connection/](https://leetcode.com/problems/redundant-connection/)

## Problem

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of* `n`* nodes*. If there are multiple answers, return the answer that occurs last in the input.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)

```

**Input:** edges = [[1,2],[1,3],[2,3]]
**Output:** [2,3]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg)

```

**Input:** edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
**Output:** [1,4]

```

**Constraints:**

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= a<sub>i</sub> < b<sub>i</sub> <= edges.length`
- `a<sub>i</sub> != b<sub>i</sub>`
- There are no repeated edges.
- The given graph is connected.

## Video Explanation

[Redundant Connection - Union Find - Leetcode 684 - Python](https://www.youtube.com/watch?v=FXWRE67PLL0)

## Approach

### Intuition

The extra edge is the first edge whose endpoints are already connected.

### Brute Force

Remove each edge in reverse order and search whether the remaining graph stays connected.

### Optimal

Process edges with a disjoint-set union structure and return the edge whose endpoints already share a root.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(E(V + E)) | O(V + E) |
| Optimal | O(E alpha(V)) | O(V) |

### Edge cases

- The cycle may contain all vertices.
- Return the last edge in the input that closes the cycle.
