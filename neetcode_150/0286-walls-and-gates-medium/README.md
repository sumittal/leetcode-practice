# 286. Walls and Gates

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Breadth-First Search, Matrix  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/walls-and-gates/](https://leetcode.com/problems/walls-and-gates/)

## Problem

Given a grid `rooms`, where `-1` is a wall, `0` is a gate, and `2147483647` (`INF`) is an empty room, replace each empty room with its distance in steps to the nearest gate. Walls block movement, and an empty room with no reachable gate remains `INF`. Modify `rooms` in place and return nothing.

**Example 1:**
- Input: `rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]`
- Output: `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`
- Explanation: Each empty room receives the shortest path length from either gate without crossing a wall.

**Example 2:**
- Input: `rooms = [[0,2147483647],[-1,2147483647]]`
- Output: `[[0,1],[-1,2]]`
- Explanation: The gate itself stays zero, and the two reachable rooms are one and two steps away.

**Constraints:**
- `m == rooms.length` and `n == rooms[i].length`.
- `1 <= m, n <= 250`.
- Each cell is `-1`, `0`, or `2147483647`.

## Video Explanation

[Walls and Gates - Multi-Source BFS - Leetcode 286 - Python](https://www.youtube.com/watch?v=e69C6xhiSQE)

## Approach

### Intuition

All gates are distance-zero sources, so a single breadth-first traversal expands nearest distances outward.

### Brute Force

For every empty room, search for its nearest gate while avoiding walls.

### Optimal

Enqueue every gate first, then use multi-source BFS to fill each empty room the first time it is reached.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((mn)^2) | O(mn) |
| Optimal | O(mn) | O(mn) |

### Edge cases

- A grid with no gates leaves every empty room at INF.
- Walls and gates are never overwritten.
