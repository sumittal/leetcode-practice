# 221. Maximal Square

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Matrix  
**Companies:** GSA Capital, Wise, PayPal, eBay, Qualtrics, Airbnb, Karat, PhonePe, Whatnot, Zomato, ByteDance, Apple, Google, Booking.com, Oracle (+10 more)  
**Pattern:** 2-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/maximal-square/](https://leetcode.com/problems/maximal-square/)

## Problem

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, *find the largest square containing only* `1`'s *and return its area*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

```

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 4

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

```

**Input:** matrix = [["0","1"],["1","0"]]
**Output:** 1

```

**Example 3:**

```

**Input:** matrix = [["0"]]
**Output:** 0

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.

## Video Explanation

[Maximal Square - Top Down Memoization - Leetcode 221](https://www.youtube.com/watch?v=6X7Ha2PrDmM)

## Approach

### Intuition

A square ending at a cell can extend only as far as its top, left, and top-left neighbors allow.

### Brute Force

Try every top-left cell and expand candidate squares while checking their borders.

### Optimal

Use a one-dimensional DP row where each one-cell stores one plus the minimum of its three neighboring square sizes.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(m n min(m,n)^2) | O(1) |
| Optimal | O(m n) | O(n) |

### Edge cases

- An empty matrix or one with no ones has area zero.
- A one-cell matrix containing one has area one.
- Track the side length and return its square.
