# 54. Spiral Matrix

**Difficulty:** Medium  
**Tags:** Array, Matrix, Simulation  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/spiral-matrix/](https://leetcode.com/problems/spiral-matrix/)

## Problem

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Video Explanation

[Spiral Matrix - Microsoft Interview Question - Leetcode 54](https://www.youtube.com/watch?v=BJnMZNwUk1M)

## Approach

### Intuition

Peel the outer boundary in four directions, shrinking it after each side is emitted.

### Brute Force

Track visited cells and walk forward, turning when blocked.

### Optimal

Maintain top, bottom, left, and right bounds and traverse each current edge once.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(m*n) | O(m*n) |
| Optimal | O(m*n) | O(1) extra |

### Edge cases

- Check bounds before traversing bottom/left after shrinking.
- A single row or column must not be emitted twice.
