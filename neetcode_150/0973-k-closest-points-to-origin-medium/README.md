# 973. K Closest Points to Origin

**Difficulty:** Medium  
**Tags:** Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, K-D Tree  
**Pattern:** Heap / Priority Queue  
**LeetCode:** [https://leetcode.com/problems/k-closest-points-to-origin/](https://leetcode.com/problems/k-closest-points-to-origin/)

## Problem

Given an array of `points` where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x<sub>1</sub> - x<sub>2</sub>)^2 + (y<sub>1</sub> - y<sub>2</sub>)^2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

```

**Input:** points = [[1,3],[-2,2]], k = 1
**Output:** [[-2,2]]
**Explanation:**
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

```

**Example 2:**

```

**Input:** points = [[3,3],[5,-1],[-2,4]], k = 2
**Output:** [[3,3],[-2,4]]
**Explanation:** The answer [[-2,4],[3,3]] would also be accepted.

```

**Constraints:**

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4`

## Video Explanation

[K Closest Points to Origin - Heap / Priority Queue - Leetcode 973 - Python](https://www.youtube.com/watch?v=rI2EBUEMfTk)

## Approach

### Intuition

Distance comparisons need only squared Euclidean distance, avoiding square roots.

### Brute Force

Sort all points by squared distance and return the first k.

### Optimal

Keep a max-heap of the k smallest squared distances, replacing its farthest point when a closer point arrives.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n log n) | O(n) |
| Optimal | O(n log k) | O(k) |

### Edge cases

- A point at the origin has distance zero.
- Several points may tie at the kth distance, and any valid k points may be returned.
