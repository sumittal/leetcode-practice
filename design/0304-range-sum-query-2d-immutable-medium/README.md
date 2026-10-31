# 304. Range Sum Query 2D - Immutable

**Difficulty:** Medium  
**Tags:** Array, Design, Matrix, Prefix Sum  
**Companies:** Okta, Waymo, Upstart, Lyft, Google, Salesforce, Meta, Amazon, Bloomberg, Microsoft  
**Pattern:** Arrays & Hashing  
**LeetCode:** [https://leetcode.com/problems/range-sum-query-2d-immutable/](https://leetcode.com/problems/range-sum-query-2d-immutable/)

## Problem

Given a 2D matrix `matrix`, handle multiple queries of the following type:

- Calculate the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

You must design an algorithm where `sumRegion` works on `O(1)` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg)

```

**Input**
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
**Output**
[null, 8, 11, 12]

**Explanation**
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^4 <= matrix[i][j] <= 10^4`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
- At most `10^4` calls will be made to `sumRegion`.

## Video Explanation

[Range Sum Query 2D - Immutable - Leetcode 304 - Python](https://www.youtube.com/watch?v=KE8MQuwE2yA)

## Approach

### Intuition

A two-dimensional prefix table lets any rectangle be assembled from four prefix sums.

### Brute Force

Visit every cell in the requested rectangle and add its value.

### Optimal

Precompute inclusive rectangle sums from the origin with a leading zero row and column.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | initialization O(1), sumRegion O(area) | O(1) |
| Optimal | initialization O(rows * columns), sumRegion O(1) | O(rows * columns) |

### Edge cases

- A single-cell rectangle returns that cell's value.
- The zero border avoids separate handling when a query touches the first row or column.
