# 63. Unique Paths II

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Matrix  
**Companies:** IMC, Agoda, Nvidia, Bloomberg, Flipkart, Amazon, TikTok, Google, Microsoft, Meta, Goldman Sachs  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/unique-paths-ii/](https://leetcode.com/problems/unique-paths-ii/)

## Problem

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

```

**Input:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** 2
**Explanation:** There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)

```

**Input:** obstacleGrid = [[0,1],[0,0]]
**Output:** 1

```

**Constraints:**

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.

## Video Explanation

[Unique Paths II - Leetcode 63 - Python](https://www.youtube.com/watch?v=d3UOz7zdE4I)

## Approach

### Intuition

Count paths to each open cell by adding paths from above and from the left.

### Brute Force

Recursively explore every right-and-down move unless a cell is blocked.

### Optimal

Use one DP row, clearing a cell at obstacles and accumulating paths from the left.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential | O(m + n) recursion |
| Optimal | O(m n) | O(n) |

### Edge cases

- A blocked start or destination yields zero paths.
- A single open cell has one path.
- Obstacles reset the path count for all routes through that position.
