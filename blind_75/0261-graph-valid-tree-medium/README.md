# 261. Graph Valid Tree

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory  
**Companies:** Zenefits, Snowflake, LinkedIn, Google, Meta, Uber, Microsoft  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/graph-valid-tree/](https://leetcode.com/problems/graph-valid-tree/)

## Problem

Given `n` labeled vertices and a list of undirected edges, determine whether the graph is a tree. A tree must connect every vertex and contain no cycle; return a boolean indicating whether both properties hold.

**Example 1:**
- Input: `n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]`
- Output: `true`
- Explanation: All five vertices are connected by four edges and no cycle is formed.

**Example 2:**
- Input: `n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`
- Output: `false`
- Explanation: Vertices `1, 2, 3` form a cycle, and the graph is not a tree.

**Constraints:**
- `1 <= n <= 2000`.
- Endpoints are distinct valid labels.
- Duplicate edges are not present.

## Video Explanation

[Graph Valid Tree - Leetcode 261 - Python](https://www.youtube.com/watch?v=bXsUuownnoQ)

## Approach

### Intuition

A tree is connected and has no cycle; equivalently, it has n-1 edges and is connected.

### Brute Force

Traverse while tracking parent edges to detect cycles, then check every vertex was reached.

### Optimal

Reject unless there are n-1 edges, then verify connectivity with DFS/Union-Find.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(V+E) | O(V+E) |
| Optimal | O(V+E) | O(V+E) |

### Edge cases

- A single vertex with no edges is a tree.
- Exactly n-1 edges alone is insufficient when the graph is disconnected.
