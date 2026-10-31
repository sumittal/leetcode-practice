# 399. Evaluate Division

**Difficulty:** Medium  
**Tags:** Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path, Bellman–Ford Algorithm, Floyd–Warshall Algorithm  
**Companies:** Tower Research Capital, Urban Company, DP world, Citadel, Nuro, Uber, GE Healthcare, Snap, PhonePe, Bloomberg, Yahoo, Rippling, TikTok, Tesla, Amazon (+5 more)  
**Pattern:** Graphs  
**LeetCode:** [https://leetcode.com/problems/evaluate-division/](https://leetcode.com/problems/evaluate-division/)

## Problem

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [A<sub>i</sub>, B<sub>i</sub>]` and `values[i]` represent the equation `A<sub>i</sub> / B<sub>i</sub> = values[i]`. Each `A<sub>i</sub>` or `B<sub>i</sub>` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [C<sub>j</sub>, D<sub>j</sub>]` represents the `j^th` query where you must find the answer for `C<sub>j</sub> / D<sub>j</sub> = ?`.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

**Note:** The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

**Example 1:**

```

**Input:** equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
**Output:** [6.00000,0.50000,-1.00000,1.00000,-1.00000]
**Explanation:**
Given: *a / b = 2.0*, *b / c = 3.0*
queries are: *a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ? *
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
```

**Example 2:**

```

**Input:** equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
**Output:** [3.75000,0.40000,5.00000,0.20000]

```

**Example 3:**

```

**Input:** equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
**Output:** [0.50000,2.00000,-1.00000,-1.00000]

```

**Constraints:**

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= A<sub>i</sub>.length, B<sub>i</sub>.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= C<sub>j</sub>.length, D<sub>j</sub>.length <= 5`
- `A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub>` consist of lower case English letters and digits.

## Video Explanation

[Evaluate Division - Leetcode 399 - Python](https://www.youtube.com/watch?v=Uei1fwDoyKk)

## Approach

### Intuition

Each equation is a directed ratio edge, and multiplying edge weights along a path gives the ratio between its endpoints.

### Brute Force

For every query, try all equation sequences until one connects the requested variables.

### Optimal

Build forward and reciprocal weighted edges, then search each query with graph traversal while carrying the product.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | Exponential per query | O(V+E) |
| Optimal | O(Q(V+E)) | O(V+E) |

### Edge cases

- An unknown variable yields -1.0, including an unknown variable queried against itself.
- A known variable divided by itself is 1.0.
- Reciprocal edges use the inverse ratio.
