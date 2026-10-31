# 48. Rotate Image

**Difficulty:** Medium  
**Tags:** Array, Math, Matrix  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/rotate-image/](https://leetcode.com/problems/rotate-image/)

## Problem

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [[7,4,1],[8,5,2],[9,6,3]]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```

**Input:** matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
**Output:** [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Video Explanation

[Rotate Image - Matrix - Leetcode 48](https://www.youtube.com/watch?v=fMSJSS7eO1w)

## Approach

### Intuition

A clockwise rotation maps each cell to the mirrored column of its original row.

### Brute Force

Write every value into a separately allocated rotated matrix.

### Optimal

Transpose across the diagonal, then reverse each row in place.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^2) | O(n^2) |
| Optimal | O(n^2) | O(1) |

### Edge cases

- A one-cell matrix is unchanged.
- The method must mutate the supplied matrix and return None.
