# 308. Range Sum Query 2D - Mutable

> 🔒 LeetCode Premium problem — statement paraphrased.

**Difficulty:** Medium  
**Tags:** Array, Design, Binary Indexed Tree, Segment Tree, Matrix, Sqrt Decomposition  
**Companies:** Google, Bloomberg, Amazon  
**Pattern:** Array  
**LeetCode:** [https://leetcode.com/problems/range-sum-query-2d-mutable/](https://leetcode.com/problems/range-sum-query-2d-mutable/)

## Problem

Store a matrix that supports changing one cell and querying an inclusive rectangular sum. Example 1: for [[3,0,1],[5,6,3]], the sum of rows 0–1 and columns 0–2 is 18. Example 2: after changing cell (0,1) to 2, a query over row 0 and columns 1–2 returns 3. Constraints: the matrix is nonempty and updates and queries stay within its bounds.

## Video Explanation

[YouTube search: Search YouTube for leetcode 308 Range Sum Query 2D - Mutable neetcode](https://www.youtube.com/results?search_query=leetcode+308+Range+Sum+Query+2D+-+Mutable+neetcode)

## Approach

### Intuition

A two-dimensional Fenwick tree supports point deltas and prefix sums without rebuilding a full prefix matrix.

### Brute Force

Store the matrix and scan every cell in each requested rectangle.

### Optimal

Maintain current values and a 2D Fenwick tree; combine four prefix sums for a rectangle.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | update O(1), sumRegion O(rows * columns) | O(rows * columns) |
| Optimal | update O(log rows * log columns), sumRegion O(log rows * log columns) | O(rows * columns) |

### Edge cases

- Updating a cell to its existing value has zero delta.
- A one-cell query returns the current value at that cell.
