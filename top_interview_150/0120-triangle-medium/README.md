# 120. Triangle

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming  
**Companies:** Upstart, Bloomberg, Walmart Labs, Infosys, Amazon, Google, Microsoft, Meta, tcs, Oracle  
**Pattern:** 1-D Dynamic Programming  
**LeetCode:** [https://leetcode.com/problems/triangle/](https://leetcode.com/problems/triangle/)

## Problem

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

**Example 1:**

```

**Input:** triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**Output:** 11
**Explanation:** The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

```

**Example 2:**

```

**Input:** triangle = [[-10]]
**Output:** -10

```

**Constraints:**

- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

## Video Explanation

[Triangle - Dynamic Programming made Easy - Leetcode 120](https://www.youtube.com/watch?v=OM1MTokvxs4)

## Approach

### Intuition

The minimum path from each cell is its value plus the cheaper reachable child below.

### Brute Force

Enumerate every top-to-bottom left-or-right path and track its sum.

### Optimal

Use a one-dimensional bottom-up DP array and overwrite each parent with its minimum child cost.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(2^n) | O(n) |
| Optimal | O(n^2) | O(n) |

### Edge cases

- A one-row triangle returns its only value.
- Negative values are valid and may appear anywhere.
- The array is updated bottom-up so both child states are still available.
