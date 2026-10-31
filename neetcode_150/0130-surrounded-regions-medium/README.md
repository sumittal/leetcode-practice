# 130. Surrounded Regions

**Difficulty:** Medium  
**Tags:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix  
**Companies:** PornHub, Nutanix, Anduril, Amazon, Adobe, Bloomberg, Google, Microsoft, Oracle, Meta, TikTok, Uber  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/surrounded-regions/](https://leetcode.com/problems/surrounded-regions/)

## Problem

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.
- **Region**: To form a region **connect every** `'O'` cell.
- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed** by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

## Video Explanation

[Surrounded Regions - Graph - Leetcode 130 - Python](https://www.youtube.com/watch?v=9z2BunfoZ5Y)

## Approach

### Intuition

Only open cells connected to the border can avoid capture; all other open cells are enclosed.

### Brute Force

For every open cell, search its component and determine whether it touches a border.

### Optimal

Mark open cells reachable from the border, flip unmarked open cells, and restore marked cells.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O((mn)^2) | O(mn) |
| Optimal | O(mn) | O(mn) |

### Edge cases

- A one-row or one-column board has no enclosed open region.
- An open region touching any border must remain unchanged.
