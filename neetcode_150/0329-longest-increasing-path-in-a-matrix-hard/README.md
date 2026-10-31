# 329. Longest Increasing Path in a Matrix

**Difficulty:** Hard  
**Tags:** Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix, Directed Acyclic Graph  
**Companies:** DoorDash, WeRide, Duolingo, Nutanix, Adobe, PhonePe, EPAM Systems, Epic Systems, TikTok, Meta, Infosys, Visa, Google, Apple, Salesforce (+4 more)  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/longest-increasing-path-in-a-matrix/](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Problem

Given an `m x n` integers `matrix`, return *the length of the longest increasing path in* `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

```

**Input:** matrix = [[9,9,4],[6,6,8],[2,1,1]]
**Output:** 4
**Explanation:** The longest increasing path is [1, 2, 6, 9].

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

```

**Input:** matrix = [[3,4,5],[3,2,6],[2,2,1]]
**Output:** 4
**Explanation: **The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

```

**Example 3:**

```

**Input:** matrix = [[1]]
**Output:** 1

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

## Video Explanation

[Longest Increasing Path in a Matrix - Leetcode 329](https://www.youtube.com/watch?v=wCc_nd-GiEc)

## Approach

### Intuition

The strictly increasing rule makes the matrix a directed acyclic graph of moves toward larger neighbors.

### Brute Force

Start a fresh DFS from every cell without caching repeated suffix paths.

### Optimal

Memoize the longest increasing path starting at each cell and recurse only to larger four-directional neighbors.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential in the number of cells | O(mn) recursion in the worst case |
| Optimal | O(mn) | O(mn) |

### Edge cases

- A single-cell matrix has path length one.
- A constant-valued matrix has no increasing move.
