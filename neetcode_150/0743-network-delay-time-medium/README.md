# 743. Network Delay Time

**Difficulty:** Medium  
**Tags:** Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm  
**Pattern:** Advanced Graphs  
**LeetCode:** [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)

## Problem

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)`, where `u<sub>i</sub>` is the source node, `v<sub>i</sub>` is the target node, and `w<sub>i</sub>` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```

**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2

```

**Example 2:**

```

**Input:** times = [[1,2,1]], n = 2, k = 1
**Output:** 1

```

**Example 3:**

```

**Input:** times = [[1,2,1]], n = 2, k = 2
**Output:** -1

```

**Constraints:**

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u<sub>i</sub>, v<sub>i</sub> <= n`
- `u<sub>i</sub> != v<sub>i</sub>`
- `0 <= w<sub>i</sub> <= 100`
- All the pairs `(u<sub>i</sub>, v<sub>i</sub>)` are **unique**. (i.e., no multiple edges.)

## Video Explanation

[Network Delay Time - Dijkstra's algorithm - Leetcode 743](https://www.youtube.com/watch?v=EaphyqKU4PQ)

## Approach

### Intuition

The delay is the longest shortest-path distance from the source to any node.

### Brute Force

Run a graph traversal from the source and enumerate possible paths to every node.

### Optimal

Use Dijkstra's algorithm with a min-heap to finalize shortest distances for nonnegative edge weights.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential in the number of vertices in the worst case | O(V + E) |
| Optimal | O((V + E) log V) | O(V + E) |

### Edge cases

- A node unreachable from the source makes the answer -1.
- A one-node network has delay zero.
