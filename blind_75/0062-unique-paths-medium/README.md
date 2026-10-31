# 62. Unique Paths

**Difficulty:** Medium  
**Tags:** Math, Dynamic Programming, Combinatorics  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)

## Problem

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```

**Input:** m = 3, n = 7
**Output:** 28

```

**Example 2:**

```

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

**Constraints:**

- `1 <= m, n <= 100`

## Video Explanation

[Unique Paths - Dynamic Programming - Leetcode 62](https://www.youtube.com/watch?v=IlEsdxuD4lY)

## Approach

### Intuition

A cell's paths are the sum of paths arriving from above and from the left.

### Brute Force

Recursively enumerate every right/down route.

### Optimal

Use one DP row, updating each cell from its left and prior-row value.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(m+n) |
| Optimal | O(m*n) | O(n) |

### Edge cases

- A one-row or one-column grid has exactly one path.
- The start cell initializes the first row.
