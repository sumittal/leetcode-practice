# 64. Minimum Path Sum

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Matrix  
**Companies:** Texas Instruments, Goldman Sachs, General Motors, Waymo, Infosys, Microsoft, Zoho, Nvidia, Amazon, TikTok, Bloomberg, Google, Meta, Apple, Uber  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)

## Problem

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

```

**Input:** grid = [[1,3,1],[1,5,1],[4,2,1]]
**Output:** 7
**Explanation:** Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

```

**Example 2:**

```

**Input:** grid = [[1,2,3],[4,5,6]]
**Output:** 12

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Video Explanation

[Minimum Path Sum - Dynamic Programming - Leetcode 64 - Python](https://www.youtube.com/watch?v=pGMsrvt0fpk)

## Approach

### Intuition

The best path to a cell comes from the cheaper of the cell above and the cell to its left.

### Brute Force

Recursively enumerate every right-and-down path to the bottom-right cell.

### Optimal

Maintain one DP row, combining the saved value from above with the updated value from the left.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential in grid dimensions | O(m + n) recursion |
| Optimal | O(m n) | O(n) |

### Edge cases

- A one-cell grid returns its cell value.
- Single-row and single-column grids have only one path.
- Initialize the first row and column by cumulative sums.
