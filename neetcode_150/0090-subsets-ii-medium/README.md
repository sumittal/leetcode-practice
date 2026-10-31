# 90. Subsets II

**Difficulty:** Medium  
**Tags:** Array, Backtracking, Bit Manipulation  
**Pattern:** Backtracking  
**LeetCode:** [https://leetcode.com/problems/subsets-ii/](https://leetcode.com/problems/subsets-ii/)

## Problem

Given an integer array `nums` that may contain duplicates, return *all possible* *subsets** (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
**Input:** nums = [1,2,2]
**Output:** [[],[1],[1,2],[1,2,2],[2],[2,2]]

```

**Example 2:**

```
**Input:** nums = [0]
**Output:** [[],[0]]

```

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Video Explanation

[Subsets II - Backtracking - Leetcode 90 - Python](https://www.youtube.com/watch?v=Vn2v6ajA7U0)

## Approach

### Intuition

Sorting groups equal values together so one recursion level can skip duplicate choices.

### Brute Force

Generate all index-based subsets, then deduplicate their value sequences.

### Optimal

Backtrack over sorted values and skip equal candidates at the same depth.

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n 2^n) | O(n 2^n) |
| Optimal | O(n 2^n) | O(n) besides output |

### Edge cases

- An empty input produces one empty subset.
- All-equal values produce one subset for each possible length.
