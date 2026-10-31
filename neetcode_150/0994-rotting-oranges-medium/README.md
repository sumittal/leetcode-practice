# 994. Rotting Oranges

**Difficulty:** Medium  
**Tags:** Array, Breadth-First Search, Matrix  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)

## Problem

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

```

**Input:** grid = [[2,1,1],[1,1,0],[0,1,1]]
**Output:** 4

```

**Example 2:**

```

**Input:** grid = [[2,1,1],[0,1,1],[1,0,1]]
**Output:** -1
**Explanation:** The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

```

**Example 3:**

```

**Input:** grid = [[0,2]]
**Output:** 0
**Explanation:** Since there are already no fresh oranges at minute 0, the answer is just 0.

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Video Explanation

[Rotting Oranges - Leetcode 994 - Python](https://www.youtube.com/watch?v=y704fEOx0s0)

## Approach

### Intuition

Rotting spreads one grid step per minute from all currently rotten oranges.

### Brute Force

For each minute, repeatedly scan the whole grid and rot fresh oranges adjacent to rotten ones.

### Optimal

Use multi-source BFS from all rotten oranges and measure the greatest distance needed to reach fresh ones.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((mn)^2) | O(mn) |
| Optimal | O(mn) | O(mn) |

### Edge cases

- No fresh oranges means zero minutes.
- A fresh orange unreachable from every rotten orange makes the result -1.
