# 1584. Min Cost to Connect All Points

**Difficulty:** Medium  
**Tags:** Array, Union-Find, Graph Theory, Minimum Spanning Tree, Prim's Algorithm, Kruskal's Algorithm, Borůvka's Algorithm  
**Companies:** Directi, PayPay, Nutanix, TikTok, Uber, IBM, Amazon, Google, Microsoft, Meta  
**Pattern:** Advanced Graphs  
**LeetCode:** [https://leetcode.com/problems/min-cost-to-connect-all-points/](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Problem

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]`.

The cost of connecting two points `[x<sub>i</sub>, y<sub>i</sub>]` and `[x<sub>j</sub>, y<sub>j</sub>]` is the **manhattan distance** between them: `|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```

**Input:** points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
**Output:** 20
**Explanation:**
![](https://assets.leetcode.com/uploads/2020/08/26/c.png)
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

```

**Example 2:**

```

**Input:** points = [[3,12],[-2,5],[-4,1]]
**Output:** 18

```

**Constraints:**

- `1 <= points.length <= 1000`
- `-10^6 <= x<sub>i</sub>, y<sub>i</sub> <= 10^6`
- All pairs `(x<sub>i</sub>, y<sub>i</sub>)` are distinct.

## Video Explanation

[Prim's Algorithm - Minimum Spanning Tree - Min Cost to Connect all Points - Leetcode 1584 - Python](https://www.youtube.com/watch?v=f7JOBJIC-NA)

## Approach

### Intuition

The minimum total connection cost is a minimum spanning tree under Manhattan distances.

### Brute Force

Enumerate spanning trees and select the one with minimum total edge weight.

### Optimal

Run Prim's algorithm, repeatedly adding the closest unvisited point to the growing tree.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n^(n-2)) | O(n) |
| Optimal | O(n^2) | O(n) |

### Edge cases

- One point requires no connection and costs zero.
- Duplicate coordinates can be connected at zero cost.
