# 73. Set Matrix Zeroes

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Matrix  
**Companies:** Nykaa, eBay, ZScaler, Walmart Labs, Zoho, Nutanix, Autodesk, Bloomberg, Meta, Microsoft, Amazon, Google, Nvidia, Juspay, tcs (+4 more)  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/set-matrix-zeroes/](https://leetcode.com/problems/set-matrix-zeroes/)

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```

**Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Output:** [[1,0,1],[0,0,0],[1,0,1]]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```

**Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Follow up:**

- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

## Video Explanation

[Set Matrix Zeroes - In-place - Leetcode 73](https://www.youtube.com/watch?v=T41rL0L3Pnw)

## Approach

### Intuition

Remember which rows and columns contain zero, then zero their intersections.

### Brute Force

Record zero coordinates and update a copied matrix.

### Optimal

Use the first row and column as markers, preserving their original zero flags separately.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(1) |

### Edge cases

- The first row and column need separate flags because they are also marker storage.
- Mark before applying zeroes so new zeroes do not spread.
