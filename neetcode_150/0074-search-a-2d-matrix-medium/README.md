# 74. Search a 2D Matrix

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Matrix  
**Companies:** Wissen Technology, SAP, Nutanix, Adobe, Paytm, Amazon, Microsoft, Bloomberg, DE Shaw, Goldman Sachs, Google, Meta, Oracle, tcs, TikTok (+2 more)  
**Pattern:** Binary Search  
**LeetCode:** [https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

You must write a solution in `O(log(m * n))` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
**Output:** true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
**Output:** false

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Video Explanation

[Search a 2D Matrix - Leetcode 74 - Python](https://www.youtube.com/watch?v=Ber2pi2C0j0)

## Approach

### Intuition

The row-major ordering makes the matrix behave like one sorted array.

### Brute Force

Inspect each matrix value until the target is found.

### Optimal

Binary search indices from zero to m*n-1 and map each midpoint to a row and column.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(mn) | O(1) |
| Optimal | O(log(mn)) | O(1) |

### Edge cases

- A one-cell matrix is either a match or a miss.
- The target may be smaller than the first value or larger than the last.
