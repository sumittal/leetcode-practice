# 200. Number of Islands

**Difficulty:** Medium  
**Tags:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix  
**Companies:** Snap, Anduril, Wix, Zenefits, Moloco, Rivian, Splunk, Hive, OKX, CrowdStrike, Walmart Labs, Siemens, TikTok, Qualcomm, BitGo (+66 more)  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

## Problem

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

```

**Example 2:**

```

**Input:** grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
**Output:** 3

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Video Explanation

[NUMBER OF ISLANDS - Leetcode 200 - Python](https://www.youtube.com/watch?v=pV2kpPD66nE)

## Approach

### Intuition

Each connected group of land is one island; mark a group as soon as it is discovered.

### Brute Force

For each land cell, recount its connected component.

### Optimal

Scan the grid and flood-fill each unseen land component, marking cells as water.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((R*C)^2) | O(R*C) |
| Optimal | O(R*C) | O(R*C) |

### Edge cases

- Water cells never start a search.
- Mark before visiting neighbors to prevent cycles.
