# 52. N-Queens II

**Difficulty:** Hard  
**Tags:** Backtracking, Algorithm X  
**Companies:** Zenefits, Liftoff, Deutsche Bank, Snowflake, Bloomberg, Amazon, Microsoft, Google, Meta  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/n-queens-ii/](https://leetcode.com/problems/n-queens-ii/)

## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```

**Input:** n = 4
**Output:** 2
**Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

```

**Example 2:**

```

**Input:** n = 1
**Output:** 1

```

**Constraints:**

- `1 <= n <= 9`

## Video Explanation

[N-Queens II - Leetcode 52 - Python](https://www.youtube.com/watch?v=nalYyLZgvCY)

## Approach

### Intuition

Place one queen per row and count only arrangements whose columns and diagonals are unused.

### Brute Force

Enumerate every column permutation and reject arrangements with diagonal conflicts.

### Optimal

Backtrack row by row while tracking occupied columns and the two diagonal keys in sets.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n! * n) | O(n) |
| Optimal | O(n!) worst case | O(n) |

### Edge cases

- A one-cell board has one valid arrangement.
- Boards of size two or three have no valid arrangement.
- Count solutions without constructing board strings.
