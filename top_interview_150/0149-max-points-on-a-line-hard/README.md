# 149. Max Points on a Line

**Difficulty:** Hard  
**Tags:** Array, Hash Table, Math, Geometry, Euclidean Algorithm, Greatest Common Divisor  
**Companies:** Waymo, X, Zoox, Meesho, LinkedIn, Sprinklr, Apple, Cisco, Citadel, Nvidia, Meta, Bloomberg, Google, Amazon, Microsoft  
**Pattern:** Math & Geometry  
**LeetCode:** [https://leetcode.com/problems/max-points-on-a-line/](https://leetcode.com/problems/max-points-on-a-line/)

## Problem

Given an array of `points` where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```

**Input:** points = [[1,1],[2,2],[3,3]]
**Output:** 3

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

```

**Input:** points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
**Output:** 4

```

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4`
- All the `points` are **unique**.

## Video Explanation

[Leetcode 149 - Maximum Points on a Line - Python](https://www.youtube.com/watch?v=Bb9lOXUOnFw)

## Approach

### Intuition

For each anchor point, points on the same line share one reduced slope.

### Brute Force

Choose pairs of points, form each line, and count all points satisfying its equation.

### Optimal

For each anchor, count gcd-reduced integer slopes and separately count duplicates.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^3) | O(1) |
| Optimal | O(n^2) | O(n) |

### Edge cases

- Duplicate points add to every line through their anchor.
- Vertical and horizontal slopes need canonical keys.
- A single point is trivially collinear.
