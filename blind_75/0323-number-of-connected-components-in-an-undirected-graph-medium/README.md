# 323. Number of Connected Components in an Undirected Graph

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory  
**Companies:** General Motors, X, LinkedIn, Amazon, TikTok, Google, Meta  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## Problem

There are `n` vertices labeled from `0` through `n - 1`, along with a list of undirected edges. Return the number of connected components, where two vertices belong to the same component when a path joins them.

**Example 1:**
- Input: `n = 5, edges = [[0,1],[1,2],[3,4]]`
- Output: `2`
- Explanation: Vertices `0, 1, 2` form one component and vertices `3, 4` form another.

**Example 2:**
- Input: `n = 4, edges = [[0,1],[1,2],[2,3]]`
- Output: `1`
- Explanation: Every vertex is reachable from every other vertex.

**Constraints:**
- `1 <= n <= 2000`.
- Edge endpoints are distinct valid labels.
- Duplicate edges are not present.

## Video Explanation

[Number of Connected Components in an Undirected Graph - Union Find - Leetcode 323 - Python](https://www.youtube.com/watch?v=8f1XPm4WOUc)

## Approach

### Intuition

Each unvisited vertex begins exactly one connected component.

### Brute Force

For every vertex, search all reachable vertices and count new traversals.

### Optimal

Build adjacency lists and DFS/BFS once from each unvisited vertex.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(V*(V+E)) | O(V) |
| Optimal | O(V+E) | O(V+E) |

### Edge cases

- Isolated vertices each count as components.
- An empty edge list gives n components.
